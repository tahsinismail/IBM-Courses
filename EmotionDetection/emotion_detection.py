import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    reqObj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=reqObj, headers=headers)
    if response.status_code == 400:
        return None
    else:
        formatted_response = json.loads(response.text)
        emotions =  formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion_value = max(emotions.values())
        dominant_emotion = [k for k,v in emotions.items() if v == dominant_emotion_value]
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion[0]
            }
        
