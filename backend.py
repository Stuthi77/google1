from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure API key for Google Generative AI
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Initialize the model with the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=(
        "Assist the teacher in conducting quizzes for students. When the teacher requests questions on a specific topic, "
        "generate questions based on their requirements. Ask the teacher if they do not provide:\n\n"
        "How many questions they need.\n"
        "The number of multiple-choice questions (MCQs) and subjective questions.\n"
        "The students' grade level.\n"
        "The desired difficulty level."
    ),
)

@app.route("/")
def render():
    return jsonify("working...")

@app.route('/bot_chat', methods=['POST'])
def chat():
    try:
        # Get the input message from the request JSON
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid request, 'message' is required"}), 400

        # Start a chat session
        chat_session = model.start_chat()

        # Send the user's message
        user_message = data['message']
        response = chat_session.send_message(user_message)

        # Return the AI's response
        return jsonify({"response": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
