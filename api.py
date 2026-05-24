from fastapi import FastAPI, Query
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(
    title="Food Demand Forecasting API",
    description="Predict food order demand using Machine Learning",
    version="1.0"
)

# Load trained model
model = joblib.load("food_demand_model.pkl")


# Home Route
@app.get("/")
def home():
    return {
        "message": "Food Demand Forecasting API Running Successfully"
    }


# Prediction Route
@app.post("/predict")
def predict(
    week: int = Query(..., example=2),
    checkout_price: float = Query(..., example=250),
    base_price: float = Query(..., example=300),
    emailer_for_promotion: int = Query(..., example=1),
    homepage_featured: int = Query(..., example=0)
):

    try:
        # Create feature array
        features = np.array([[
            week,
            checkout_price,
            base_price,
            emailer_for_promotion,
            homepage_featured
        ]])

        # Prediction
        prediction = model.predict(features)

        return {
            "success": True,
            "input": {
                "week": week,
                "checkout_price": checkout_price,
                "base_price": base_price,
                "emailer_for_promotion": emailer_for_promotion,
                "homepage_featured": homepage_featured
            },
            "predicted_orders": int(prediction[0])
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }