from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
import requests # type: ignore
import os
from dotenv import load_dotenv # type: ignore

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

HF_API_TOKEN = os.getenv("HF_API_KEY")  
if not HF_API_TOKEN:
    raise ValueError("Hugging Face API key not found. Please check your .env file.")

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

HF_MODEL_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

app = Flask(__name__)
CORS(app)

@app.route("/review", methods=["POST"])


def review_code():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "javascript")
    action = data.get("action", "explain")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    prompt_map = {
        "explain": (
            f"Explain what this {language} code does in simple, layman terms without showing the code itself. "
            "Also provide a simple example to illustrate the concept:\n\n"
            f"{code}"
        ),
        
        "debug": (
            f"Find and fix bugs in the following {language} code. "
            "Return only the corrected code with inline comments showing where and what was fixed:\n\n"
            f"{code}"
        ),
        
        "optimize": (
            f"Optimize the following {language} code for performance and readability. "
            "Return only the optimized code with short comments explaining what was optimized and why:\n\n"
            f"{code}"
        ),
    }

    prompt = prompt_map.get(action)
    if not prompt:
        return jsonify({"error": "Invalid action"}), 400

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.7
        }
    }
    
    try:
        response = requests.post(HF_MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and 'generated_text' in result[0]:
            generated_text = result[0]['generated_text']
            if generated_text.startswith(prompt):
                cleaned_output = generated_text[len(prompt):].strip()
            else:
                cleaned_output = generated_text.strip()
        else:
            cleaned_output = str(result)
        
        return jsonify({"result": cleaned_output})  # <-- Indented inside try
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Failed to get response from Hugging Face API"}), 500

if __name__ == "__main__":
    app.run(debug=True)
