from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("sales_model.pkl")

@app.route("/")
def home():
    return "Sales Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    future_dates = pd.date_range(start=data["start_date"], periods=int(data["days"]), freq="W")
    future_df = pd.DataFrame({"ds": future_dates})

    # Add placeholder values for regressors
    future_df["Temperature"] = 60
    future_df["Fuel_Price"] = 3.5
    future_df["CPI"] = 220
    future_df["Size"] = 150000

    forecast = model.predict(future_df)
    forecast = forecast[["ds", "yhat"]].rename(columns={"ds": "Date", "yhat": "Predicted_Sales"})

    return jsonify(forecast.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)