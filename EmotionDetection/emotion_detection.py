import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analiza el texto enviado utilizando la API de Watson NLP,
    extrae las puntuaciones de cada emoción y determina la emoción dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=payload, headers=headers)
    
    # 1. Convertir la respuesta de texto a un diccionario de Python
    response_dict = json.loads(response.text)
    
    # Extraer el diccionario que contiene las emociones
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # 2. Extraer los puntajes individuales
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 3. Determinar la emoción dominante (la que tiene mayor puntaje)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # 4. Retornar el formato requerido
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }