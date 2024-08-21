from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
genai.configure(api_key='AIzaSyDv7Ee-FqnhisBH19Rk2C9f8ByLUpFLzvA')

# Simple in-memory storage for conversation history and feedback
conversations = {}
feedback_store = []

class Conversation:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_context(self):
        # Return the last 5 messages for context
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.history[-5:]])

def generate_content(prompt, context="You are a helpful AI assistant. Provide concise and accurate responses.", max_tokens=150):
    full_prompt = f"{context}\n\nUser: {prompt}\nAssistant:"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(full_prompt)
    return post_process(response.text, max_tokens)

def summarize_text(text):
    prompt = f"Summarize the following text concisely:\n{text}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return post_process(response.text, 100)

def post_process(response, max_tokens):
    # Truncate response to max_tokens
    words = response.split()
    if len(words) > max_tokens:
        return ' '.join(words[:max_tokens]) + "..."
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_id = data.get('user_id', 'default')
    prompt = data.get('prompt', '')

    if user_id not in conversations:
        conversations[user_id] = Conversation()

    conversations[user_id].add_message("User", prompt)
    context = conversations[user_id].get_context()

    content = generate_content(prompt, context)
    conversations[user_id].add_message("Assistant", content)

    return jsonify({'content': content})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary = summarize_text(text)
    return jsonify({'summary': summary})

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    user_id = data.get('user_id', 'default')
    message_id = data.get('message_id', datetime.now().isoformat())
    rating = data.get('rating')

    feedback_store.append({
        'user_id': user_id,
        'message_id': message_id,
        'rating': rating,
        'timestamp': datetime.now().isoformat()
    })

    # Here you could implement logic to use feedback for improving responses
    return jsonify({'status': 'Feedback received'})

if __name__ == '__main__':
    app.run(debug=True)