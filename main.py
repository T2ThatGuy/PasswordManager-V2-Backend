from api import make_app


# --- Logging Config
import logging.config
logging.config.fileConfig('api/logging/log-dev.conf')

app = make_app()
