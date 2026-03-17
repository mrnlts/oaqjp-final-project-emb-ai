from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("My Emotion Detector")

@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    response = emotion_detector(request.args.get('textToAnalyze')) 
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

app.run(host="0.0.0.0", port=5000)