from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd
from pydantic import BaseModel
from app.services.recommend_service import recommend_similar

app = FastAPI()
import mlflow

   # or /content/mlruns in Colab





# =========================
# ✅ LOAD MODELS
# =========================

churn_model = mlflow.pyfunc.load_model(
    "file:///app/mlruns/141824655644104764/15c20707bf0d4b57855078c14ff5134f/artifacts"
)

flight_model = mlflow.pyfunc.load_model(
    "file:///app/mlruns/147858462287206006/f004768a09a54a56a13deba1aac0ddcf/artifacts"
)


gender_model = mlflow.pyfunc.load_model(
    "file:///app/mlruns/252158451201714791/5520a218d38946568fafa10a425633f9/artifacts"
)


# 👉 Recommendation models (simple logic placeholders)
# (since these are not pyfunc models)
# you can later replace with saved objects

# =========================
# ✅ ROOT
# =========================

@app.get("/")
def home():
    return {"message": "Voyage Analytics API Running 🚀"}

# =========================
# ✅ CHURN PREDICTION
# =========================
class ChurnInput(BaseModel):
    State: str
    Account_length: int
    Area_code: int
    International_plan: str
    Voice_mail_plan: str
    Number_vmail_messages: int
    Total_day_minutes: float
    Total_day_calls: int
    Total_day_charge: float
    Total_eve_minutes: float
    Total_eve_calls: int
    Total_eve_charge: float
    Total_night_minutes: float
    Total_night_calls: int
    Total_night_charge: float
    Total_intl_minutes: float
    Total_intl_calls: int
    Total_intl_charge: float
    Customer_service_calls: int
@app.post("/predict/churn")
def predict_churn(data: ChurnInput):
    try:
        df = pd.DataFrame([{
            "State": data.State,
            "Account length": data.Account_length,
            "Area code": data.Area_code,
            "International plan": data.International_plan,
            "Voice mail plan": data.Voice_mail_plan,
            "Number vmail messages": data.Number_vmail_messages,
            "Total day minutes": data.Total_day_minutes,
            "Total day calls": data.Total_day_calls,
            "Total day charge": data.Total_day_charge,
            "Total eve minutes": data.Total_eve_minutes,
            "Total eve calls": data.Total_eve_calls,
            "Total eve charge": data.Total_eve_charge,
            "Total night minutes": data.Total_night_minutes,
            "Total night calls": data.Total_night_calls,
            "Total night charge": data.Total_night_charge,
            "Total intl minutes": data.Total_intl_minutes,
            "Total intl calls": data.Total_intl_calls,
            "Total intl charge": data.Total_intl_charge,
            "Customer service calls": data.Customer_service_calls
        }])

        prediction = churn_model.predict(df)[0]

        label_map = {
            0: "Not Churn",
            1: "Churn"
        }

        return {"prediction": label_map.get(prediction)}

    except Exception as e:
        return {"error": str(e)}


# =========================
# ✅ FLIGHT PRICE PREDICTION
# =========================


class FlightInput(BaseModel):
    travelCode: int
    userCode: int
    from_: str
    to: str
    flightType: str
    time: float
    distance: float
    agency: str
    date: str
@app.post("/predict/flight")
def predict_flight(data: FlightInput):
    try:
        import pandas as pd

        df = pd.DataFrame([{
            "travelCode": data.travelCode,
            "userCode": data.userCode,
            "from": data.from_,
            "to": data.to,
            "flightType": data.flightType,
            "time": data.time,
            "distance": data.distance,
            "agency": data.agency,
            "date": data.date
        }])

        print("MODEL:", flight_model)

        prediction = flight_model.predict(df)

        return {"prediction": prediction.tolist()}

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}

# =========================
# ✅ GENDER CLASSIFICATION
# =========================
class GenderInput(BaseModel):
    code: int
    company: str
    name: str
    age: int


@app.post("/predict/gender")
def predict_gender(data: GenderInput):
    try:
        df = pd.DataFrame([{
            "code": data.code,
            "company": data.company,
            "name": data.name,
            "age": data.age
        }])

        prediction = gender_model.predict(df)[0]

        # ✅ Convert numeric → label
        label_map = {
            0: "Female",
            1: "Male"
        }

        result = label_map.get(prediction, "Unknown")

        return {"prediction": result}

    except Exception as e:
        return {"error": str(e)}
# =========================
# ✅ RECOMMENDATION SYSTEM
# =========================

# 👉 Replace with your real logic later
@app.get("/recommend/{index}")
def recommend(index: int):
    try:
        results = recommend_similar(index)
        return {"recommended_places": results}

    except Exception as e:
        return {"error": str(e)}
