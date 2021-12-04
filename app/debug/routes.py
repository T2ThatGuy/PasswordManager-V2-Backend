# --- Flask Imports
from flask import current_app

# --- App Imports
from app.debug import bp

# --- Misc Imports
import operator
from flask import jsonify


# --- Debugging route to see what urls are available
@bp.route('/map')
def routes():
    'Display registered routes'
    rules = []
    routes = []

    for rule in current_app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        routes.append(route)

    return jsonify(routes)