# --- Security
from Crypto.Cipher import AES
import argon2

# --- Misc Imports
import os
import json

def read_config(path):
    with open(path) as f:
        config = json.load(f)

    return config


class Security:

    def __init__(self):

        self.argon2config = read_config('app/config.json')['hashers']['argon2']

    def hash_master_password(self, password):

        config = self.argon2config

        argon2hasher = argon2.PasswordHasher(
            time_cost=config['time_cost'],
            memory_cost=config['memory_cost'],
            parallelism=config['parallelism'],
            hash_len=config['hash_len'],
            salt_len=config['salt_len']
        )

        hashedPassword = argon2hasher.hash(password)

        return hashedPassword

    def check_master_password(self, hashed_password, password):

        config = self.argon2config

        argon2hasher = argon2.PasswordHasher(
            time_cost=config['time_cost'],
            memory_cost=config['memory_cost'],
            parallelism=config['parallelism'],
            hash_len=config['hash_len'],
            salt_len=config['salt_len']
        )

        try:
            argon2hasher.verify(hashed_password, password)
            return True
        
        except argon2.exceptions.VerifyMismatchError:
            return False

    def encrypt_password(self, masterPassword, password):

        config = self.argon2config

        salt = os.urandom(16)

        key = argon2.hash_password_raw(
            time_cost=config['time_cost'],
            memory_cost=config['memory_cost'],
            parallelism=config['parallelism'],
            hash_len=config['hash_len'],
            password=masterPassword.encode(),
            salt=salt,
            type=argon2.low_level.Type.ID
        )

        aesCipher = AES.new(key, AES.MODE_GCM)
        cipherText, authTag = aesCipher.encrypt_and_digest(password.encode())

        return ( cipherText, salt, aesCipher.nonce, authTag )

    def decrypt_password(self, masterPassword, data):

        config = self.argon2config

        cipherText, salt, nonce, authTag = data

        key = argon2.hash_password_raw(
            time_cost=config['time_cost'],
            memory_cost=config['memory_cost'],
            parallelism=config['parallelism'],
            hash_len=config['hash_len'],
            password=masterPassword.encode(),
            salt=salt,
            type=argon2.low_level.Type.ID
        )

        aesCipher = AES.new(key, AES.MODE_GCM, nonce)

        plainText = aesCipher.decrypt_and_verify(cipherText, authTag)

        return plainText

security = Security()
