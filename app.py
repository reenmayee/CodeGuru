from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not found!")

client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "CodeGuru Backend Running!"})


@app.route("/review", methods=["POST"])
def review():

    try:
        data = request.get_json()

        code = data.get("code", "")
        language = data.get("language", "javascript")
        action = data.get("action", "explain")

        if not code:
            return jsonify({"error": "No code provided"}), 400

        if action == "explain":
            prompt = f"""
Explain the following {language} code in very simple language.

Do NOT repeat the code.

Explain:
• What the code does
• How it works
• Give a simple example

Code:

{code}
"""

        elif action == "debug":
            prompt = f"""
Debug this {language} code.

Return:

1. Corrected code
2. Explain each bug you fixed

Code:

{code}
"""

        elif action == "optimize":
            prompt = f"""
Optimize this {language} code.

Return:

1. Optimized code
2. Explain every optimization

Code:

{code}
"""

        else:
            return jsonify({"error": "Invalid action"}), 400

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        return jsonify({
            "result": response.text
        })

    except Exception as e:
        print(e)
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
