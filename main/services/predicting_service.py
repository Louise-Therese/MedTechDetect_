import pandas as pd
import joblib
import os
class PredictionService():
    """Service class for Predicting Patient."""

    def __init__(self):
        super(PredictionService, self).__init__()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.local_model_path = os.path.join(self.script_dir, 'models', 'model.pkl')

    def predict_patient(self, data):
        """Prediction Patient"""
        model = joblib.load(self.local_model_path)

        data = pd.DataFrame([data], columns=['PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age', 'Insurance'])

        predictions = model.predict(data)
        if predictions == np.array([1]):
            prediction = 'Positive'
            return prediction
        elif predictions == np.array([0]):
            prediction = 'Negative'
            return prediction
        else :
            False
