## Gemini-AI chatbot

### Project Overview

This project is a web application built using Flask that integrates with Google's Gemini AI API to provide content generation and text summarization services. Users can input prompts to generate content or provide text to receive a summary. The application uses environment variables for secure API key management and maintains conversation history.

### Features

- **Content Generation**: Users can generate text content based on a given prompt using Google's Gemini Pro model.
- **Text Summarization**: Users can summarize large blocks of text efficiently.
- **Conversation History**: The application maintains context for each user's conversation.
- **Feedback System**: Users can provide feedback on generated responses.
- **Web Interface**: A simple HTML interface to interact with the application.

### Prerequisites

- Python 3.x
- Flask
- google-generativeai
- python-dotenv

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependancies**:
   ```bash
   pip install -r requirements.txt

4. **Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```
     
### Usage

1. **Run the Application**:
   ```bash
   flask run
   ```
   The application will start on 'http://127.0.0.1:5000/'.

2. **Access the Web Interface**:
   - Open a web browser and go to `http://127.0.0.1:5000/`.
   - Use the interface to generate content or summarize text by providing the necessary input.

### Code Structure

- **`app.py`**: Main application file containing the Flask routes and logic for content generation, summarization, and feedback handling.
- **`templates/index.html`**: HTML template for the web interface.
- **`.env`**: File to store environment variables securely.
- **`env.yml`**: Conda environment configuration file.

### API Endpoints

- **`/generate`**: POST request for content generation
- **`/summarize`**: POST request for text summarization
- **`/feedback`**: POST request for submitting user feedback
