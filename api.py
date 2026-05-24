from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("food_demand_model.pkl")

@app.get("/")
def home():
    return {
        "message": "Food Demand Forecasting API Running"
    }

@app.post("/predict")
def predict(
    week: int,
    checkout_price: float,
    base_price: float,
    emailer_for_promotion: int,
    homepage_featured: int
):

    features = np.array([
        [
            week,
            checkout_price,
            base_price,
            emailer_for_promotion,
            homepage_featured
        ]
    ])

    prediction = model.predict(features)

    return {
        "predicted_orders": int(prediction[0])
    }