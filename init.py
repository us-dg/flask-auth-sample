from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import api.basic_apis as ba

app = Flask(__name__)

@app.route('/')
def hello():
    return ba.heartbeat()

@app.route('/search')
def search():
    return 'Hello world!'

@app.route('/headers')
def headers():
    return ba.headers()

@app.route('/custom_response')
def custom_response():
    return ba.custom_response()

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Flask API Boilerplate"
    }
)

app.register_blueprint(swaggerui_blueprint)

app.run()