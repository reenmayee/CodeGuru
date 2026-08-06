from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "CodeGuru Backend Running!"


@app.route("/review", methods=["POST"])
def review_code():
    try:
        data = request.get_json()

        code = data.get("code", "")
        language = data.get("language", "javascript")
        action = data.get("action", "explain")

        if not code:
            return jsonify({"error": "No code provided"}), 400

        if action == "explain":
            prompt = f"""
Explain the following {language} code in simple English.
Do NOT repeat the code.
Use beginner-friendly language.
Give a simple example.

Code:
{code}
"""

        elif action == "debug":
            prompt = f"""
Debug this {language} code.

Return:
1. Corrected code.
2. Explain every bug you fixed.

Code:
{code}
"""

        elif action == "optimize":
            prompt = f"""
Optimize this {language} code.

Return:
1. Optimized code.
2. Explain every optimization.

Code:
{code}
"""

        else:
            return jsonify({"error": "Invalid action"}), 400

        response = model.generate_content(prompt)

        return jsonify({
            "result": response.text
        })

    except Exception as e:
        print(e)
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
