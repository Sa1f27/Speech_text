from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_transcription', methods=['POST'])
def save_transcription():
    transcription = request.json.get('transcription')
    with open('transcriptions.txt', 'a') as f:
        f.write(transcription + '\n') #to write
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
