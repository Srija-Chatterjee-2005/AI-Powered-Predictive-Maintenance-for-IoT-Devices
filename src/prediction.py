import joblib

def load_model():
    return joblib.load("models/model.pkl")

def predict(model, temp, vib, curr):
    ratio = temp / (vib + 1)
    data = [[temp, vib, curr, ratio]]
    return model.predict(data)[0]