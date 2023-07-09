from main.services.predicting_service import PredictionService
from flask_restx import Namespace, Resource, fields
from flask import current_app
api = Namespace("Prediction Patient", description="Prediction Patient related APIs")

patient_prediction_model = api.model(
    "PatientPredictionModel",
    {
        'age': fields.Integer(required=True, description='Age of the patient', example=50),
        'symptoms': fields.Nested(api.model('Symptoms', {
            'PRG': fields.Float(required=True, description='Presence of PRG symptom', example=6),
            'PL': fields.Float(required=True, description='Presence of PL symptom', example=148),
            'PR': fields.Float(required=True, description='Presence of PR symptom', example=72),
            'SK': fields.Float(required=True, description='Presence of SK symptom', example=35),
            'TS': fields.Float(required=True, description='Presence of TS symptom', example=0),
            'M11': fields.Float(required=True, description='Presence of M11 symptom', example=33.6),
            'BD2': fields.Float(required=True, description='Presence of BD2 symptom', example=0.627),
            'Insurance': fields.Float(required=True, description='Presence of Insurance symptom', example=1)
        }))
    }
)

@api.route("/predict/patient")
class PatientPrediction(Resource):
    def __init__(self, arg):
        super().__init__(arg)
        self.predictionservice = PredictionService()

    @api.expect(patient_prediction_model)
    def post(self):
        data = api.payload

        if not data:
            return {'error': 'Aucune donnée fournie.'}, 422

        # Extract the relevant data from the payload
        age = data['age']
        symptoms = data['symptoms']

        # Create a dictionary with the model keys and corresponding values
        data_dict = {
            'PRG': symptoms['PRG'],
            'PL': symptoms['PL'],
            'PR': symptoms['PR'],
            'SK': symptoms['SK'],
            'TS': symptoms['TS'],
            'M11': symptoms['M11'],
            'BD2': symptoms['BD2'],
            'Age': age,
            'Insurance': symptoms['Insurance']
        }

        # Perform prediction using the PredictionService
        prediction = self.predictionservice.predict_patient(data_dict)
        if prediction:
            return {'prediction': prediction}, 200

        if not prediction:
            return {"error": "Donn\u00e9es d'entr\u00e9e manquantes ou incorrectes."}, 422