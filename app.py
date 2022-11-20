import flask

from api import api

app = flask.Flask(__name__)
app.register_blueprint(api)

from api import api

@app.route('/')
def index():
    return flask.render_template('index.html', name = 'Olesya')
