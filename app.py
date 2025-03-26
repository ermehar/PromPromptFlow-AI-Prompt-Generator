from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS

# Created by Yashwant Mehar
# Email: yashwantmehar@gmail.com
# LinkedIn: https://www.linkedin.com/in/ermehar/
# GitHub: https://github.com/ermehar
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize OpenAI
client = OpenAI(api_key="")  # Replace with your OpenAI API key

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[{"role": "user", "content": prompt}],
            # max_tokens=200
        )

        result = response.choices[0].message.content
        print(result)
        return jsonify({"response": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
