import pandas as pd
import pickle
import os
from weather_data import get_weather_forecast  # Import forecast function

# Function to load and predict using the trained model
def predict_disaster(temp, humidity, wind_speed):
    # Ensure the model file exists
    if not os.path.exists("disaster_model.pkl"):
        print("❌ Model file not found. Please train the model first.")
        return None

    # Load the trained model
    with open("disaster_model.pkl", "rb") as f:
        loaded_model = pickle.load(f)

    # Convert input into a DataFrame to match training format
    input_data = pd.DataFrame([[temp, humidity, wind_speed]], columns=["temperature", "humidity", "wind_speed"])

    # Make prediction
    prediction = loaded_model.predict(input_data)
    return "🚨 Disaster Warning!" if prediction[0] == 1 else "✅ No Threat"

# Function to process weekly forecast
def check_weekly_forecast():
    forecast = get_weather_forecast()
    if not forecast:
        print("❌ Could not retrieve weather data.")
        return

    for day in forecast:
        prediction = predict_disaster(day["temperature"], day["humidity"], day["wind_speed"])
        print(f"{day['date']}: {prediction}")

        # If a disaster is predicted, send an email alert
        if "Disaster Warning" in prediction:
            from email_alert import send_email_alert
            send_email_alert(f"🚨 ALERT: Disaster Predicted on {day['date']}", f"{prediction}\nTake preventive action.")

# Run daily forecast check
if __name__ == "__main__":
    check_weekly_forecast()
