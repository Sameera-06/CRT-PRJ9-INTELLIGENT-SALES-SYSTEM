import joblib

def load_model():

    return joblib.load(
        "model/sales_forecast_model.pkl"
    )