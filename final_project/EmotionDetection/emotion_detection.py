import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    emotion_list = formatted_response['emotionPredictions'][0]['emotion']
    scores = {
        'anger': emotion_list['anger'],
        'disgust': emotion_list['disgust'],
        'fear': emotion_list['fear'], 
        'joy': emotion_list['joy'],
        'sadness': emotion_list['sadness']
    }
    emotion_scores = [
        {'emotion':'anger', 'score': scores['anger']}, 
        {'emotion':'disgust', 'score': scores['disgust']},
        {'emotion': 'fear', 'score': scores['fear']},
        {'emotion':'joy', 'score': scores['joy']},
        {'emotion':'sadness', 'score': scores['sadness']}
    ]
    emotion_scores.sort(key=lambda x: x['score'], reverse=True)
    result = {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': emotion_scores[0]['emotion'],
    }
    return result