import requests
import json

def emotion_detector(text_to_analyze):
    # Return None if the input text is empty or only contains whitespace
    if not text_to_analyze.strip():  # Check for empty or blank input
        return None

    # API endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Payload for the POST request
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Headers for the POST request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make the POST request to the API
    response = requests.post(url, json=myobj, headers=header)

    # Parse the JSON response
    formatted_response = json.loads(response.text)

    # Extract emotion predictions from the response
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion based on the highest score
    dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

    # Return the emotion predictions and the dominant emotion
    return {
        "anger": emotion_predictions["anger"],
        "disgust": emotion_predictions["disgust"],
        "fear": emotion_predictions["fear"],
        "joy": emotion_predictions["joy"],
        "sadness": emotion_predictions["sadness"],
        "dominant_emotion": dominant_emotion
    }
