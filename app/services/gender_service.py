import pandas as pd
import mlflow.pyfunc
from app.config import *

model = mlflow.pyfunc.load_model("models:/GenderModel/1")

def predict_gender(data: dict):
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return int(pred)