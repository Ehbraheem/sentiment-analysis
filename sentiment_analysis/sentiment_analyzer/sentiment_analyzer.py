import requests
import json

def analyze(text):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = { 'grpc-metadata-mm-model-id': 'sentiment_aggregated-bert-workflow_lang_multi_stock' }
    data = { 'raw_document': { 'text': text } }

    response = requests.post(url, json = data, headers = headers)

    formatted_response =  json.loads(response.text)

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}
