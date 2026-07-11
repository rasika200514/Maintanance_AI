import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from .env
load_dotenv()

# Configure Gemini using the environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def predict_failure(temp, voltage, current, hours, vibration):

    prompt = f"""
You are an AI Predictive Maintenance Expert.

Machine Details:
- Temperature: {temp} °C
- Voltage: {voltage} V
- Current: {current} A
- Running Hours: {hours}
- Vibration: {vibration}

Analyze the machine and provide:
1. Risk Level
2. Reason
3. Maintenance Recommendation.
"""

    response = model.generate_content(prompt)
    return response.text