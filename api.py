import flask

api = flask.Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def api_index():
    return 'API index page'
