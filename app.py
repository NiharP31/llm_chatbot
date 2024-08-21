from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
genai.configure(api_key='AIzaSyDv7Ee-FqnhisBH19Rk2C9f8ByLUpFLzvA')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    content = generate_content(prompt)
    return jsonify({'content': content})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary = summarize_text(text)
    return jsonify({'summary': summary})

def generate_content(prompt, max_tokens=150):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text[:max_tokens]

def summarize_text(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Summarize the following text:\n{text}")
    return response.text[:100]

if __name__ == '__main__':
    app.run(debug=True)