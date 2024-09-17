import requests
import json

def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { 'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock' }
    data = { 'raw_document': { 'text': text } }

    response = requests.post(url, json = data, headers = headers)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    formatted_response =  json.loads(response.text)
    predictions = formatted_response.get('emotionPredictions').pop().get('emotion')
    dominant_emotion = max(predictions, key=predictions.get)

    emotions = {**predictions, 'dominant_emotion': dominant_emotion }

    return emotions

