from flask import Flask
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    models = client.models.list()

    result = []

    for model in models:
        result.append(model.name)

    return "<br>".join(result)

if __name__ == "__main__":
    app.run()
