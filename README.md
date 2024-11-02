
# Flask Speech-to-Text Transcription App

This project is a Flask-based web application that accepts audio input, transcribes it to text, and saves the transcription to a file.

## Features

- Simple web interface
- Converts audio to text using `speech_recognition`
- Saves transcriptions in a text file (`transcriptions.txt`)

## Installation

1. Clone the repository:

   ```
   git clone "https://github.com/Sa1f27/Speech_text.git"
   
   ```

2. Install the required packages:

   ```
   pip install Flask speechrecognition
   ```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Visit `http://127.0.0.1:5000/` in your web browser.

## API Endpoints

- **GET /**: Renders the main interface (`index.html`).

## File Structure

- `app.py`: Main server code
- `templates/index.html`: Frontend interfac
