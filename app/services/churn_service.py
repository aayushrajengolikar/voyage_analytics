import pandas as pd
import mlflow.pyfunc
from app.config import *

model = mlflow.pyfunc.load_model("models:/ChurnModel/1")

def predict_churn(data: dict):
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return int(pred)