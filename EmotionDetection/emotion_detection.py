import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    request_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=request_json, headers=headers, timeout=(5, 10))

    response_json = response.json()

    emotion_preditions_root = response_json.get("emotionPredictions")
    emotion_predictions_first = emotion_preditions_root[0]
    emotion_scores = emotion_predictions_first.get("emotion")

    anger_score = emotion_scores.get("anger")
    disgust_score = emotion_scores.get("disgust")
    fear_score = emotion_scores.get("fear")
    joy_score = emotion_scores.get("joy")
    sadness_score = emotion_scores.get("sadness")

    dominant_emotion_score = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_score
    }
