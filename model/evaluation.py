from model_loader import load_model

def predict_sales(data):

    model=load_model()

    prediction=model.predict(data)

    return prediction