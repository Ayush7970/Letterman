from flask import Flask, request, jsonify
from weather_data import get_weather
from ml_model import predict_disaster
from email_alert import send_email_alert

app = Flask(__name__)

@app.route("/")
def home():
    return "AI-Powered Disaster Prediction API is running!"

@app.route("/predict", methods=["GET"])
def predict():
    weather = get_weather()
    prediction = predict_disaster(weather["temperature"], weather["humidity"], weather["wind_speed"])

    if "Disaster Warning!" in prediction:
        send_email_alert("🚨 ALERT: Disaster Predicted!", f"{prediction} - Take action immediately.")

    return jsonify({
        "weather": weather,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
