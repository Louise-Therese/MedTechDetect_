from flask import Flask
from flask_restx import Api

from main.apis.prediction import api as PredictionAPI
from flask_cors import CORS

def create_app():

    app = Flask(
        __name__,
        instance_relative_config=True,
    )
    CORS(app)
    # Swagger UI config
    app.config.SWAGGER_UI_JSONEDITOR = True
    app.config.SWAGGER_UI_DOC_EXPANSION = "list"
    
    @app.route('/health', methods=['GET'])
    def check_health():
        return 'OK'
    
    return app


app=create_app()

api = Api(
    app,
    version="1.0",
    title="Prediction Sepsis API",
    description="Rest API for Prediction of patient if is affected with Sepsis Virus",
    doc="/docs")

api.add_namespace(PredictionAPI, path="/v1")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)