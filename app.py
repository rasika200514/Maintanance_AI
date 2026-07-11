from flask import Flask, render_template, request
from utils.gemini import predict_failure

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    temp = float(request.form["temperature"])
    voltage = float(request.form["voltage"])
    current = float(request.form["current"])
    hours = float(request.form["hours"])
    vibration = request.form["vibration"]

    # Get AI Prediction from Gemini
    result = predict_failure(
        temp,
        voltage,
        current,
        hours,
        vibration
    )

    # Calculate Machine Health Score
    score = 100

    if temp > 80:
        score -= 30

    if current > 20:
        score -= 20

    if vibration == "High":
        score -= 30

    if hours > 1000:
        score -= 20

    if score < 0:
        score = 0

    # Calculate Risk Level
    if score >= 70:
        risk = "LOW"
        color = "green"
    elif score >= 40:
        risk = "MEDIUM"
        color = "orange"
    else:
        risk = "HIGH"
        color = "red"

    # Send data to result page
    return render_template(
        "result.html",
        result=result,
        score=score,
        risk=risk,
        color=color,
        temp=temp,
        voltage=voltage,
        current=current,
        hours=hours,
        vibration=vibration
    )


if __name__ == "__main__":
    app.run(debug=True)