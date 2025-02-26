''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from sentiment_analyzer.sentiment_analyzer import analyze


app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args.get('textToAnalyze')

    response = analyze(text)
    label, score = response['label'], response['score']

    if label is None:
        return "Invalid input! Try again."

    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
