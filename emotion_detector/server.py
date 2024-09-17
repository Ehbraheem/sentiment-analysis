''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the emotions and their 
        corresponding confidence score for the provided text.
    '''
    text = request.args.get('textToAnalyze')

    response = detector(text)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    statement = (
        f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust':"
        f" {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and"
        f" 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"
    )

    return statement

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)