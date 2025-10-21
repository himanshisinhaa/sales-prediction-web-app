import pandas as pd
import numpy as np
from prophet import Prophet
import joblib

# Load datasets
train = pd.read_csv("data/train.csv")
features = pd.read_csv("data/features.csv")
stores = pd.read_csv("data/stores.csv")

# Merge all datasets
df = train.merge(features, on=["Store", "Date"], how="left").merge(stores, on="Store", how="left")

# Convert Date to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Prepare data for Prophet
df_prophet = df.groupby("Date").agg({
    "Weekly_Sales": "sum",
    "Temperature": "mean",
    "Fuel_Price": "mean",
    "CPI": "mean",
    "Size": "mean"
}).reset_index()

df_prophet.rename(columns={"Date": "ds", "Weekly_Sales": "y"}, inplace=True)

# Train the Prophet model
model = Prophet()
model.add_regressor("Temperature")
model.add_regressor("Fuel_Price")
model.add_regressor("CPI")
model.add_regressor("Size")

model.fit(df_prophet)

# Save the trained model
joblib.dump(model, "sales_model.pkl")
print("✅ Model training completed and saved as 'sales_model.pkl'!")