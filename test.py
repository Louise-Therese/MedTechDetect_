import unittest
from flask import Flask
from flask_restx import Api, Namespace
from app import create_app  
from app import PredictionAPI  

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.api = Api(
            self.app,
            version="1.0",
            title="Prediction Sepsis API",
            description="Rest API for Prediction of patient if is affected with Sepsis Virus",
            doc="/docs"
        )
        self.api.add_namespace(PredictionAPI, path="/v1")
        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'OK')

if __name__ == '__main__':
    unittest.main()