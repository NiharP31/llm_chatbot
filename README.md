## README for Flask Content Generation and Summarization Tool

### Project Overview

This project is a web application built using Flask that integrates with the OpenAI API to provide content generation and text summarization services. Users can input a prompt to generate content or provide text to receive a summary. The application leverages environment variables for secure API key management.

### Features

- **Content Generation**: Users can generate text content based on a given prompt using OpenAI's GPT-3.5-turbo model.
- **Text Summarization**: Users can summarize large blocks of text efficiently.
- **Web Interface**: A simple HTML interface to interact with the application.

### Prerequisites

- Python 3.x
- Flask
- OpenAI Python Client
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
     OPENAI_API_KEY=your_openai_api_key
     ```
     
### Usage

1. **Run the Application**:
   ```bash
   flask run

   The application will start on 'http://127.0.0.1:5000/'.

2. **Access the Web Interface**:
   - Open a web browser and go to `http://127.0.0.1:5000/`.
   - Use the interface to generate content or summarize text by providing the necessary input.

### Code Structure

- **`app.py`**: Main application file containing the Flask routes and logic for content generation and summarization.
- **`templates/index.html`**: HTML template for the web interface.
- **`.env`**: File to store environment variables securely.
