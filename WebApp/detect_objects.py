import requests, os

def detect_objects(image):
    # Authenticate
    prediction_key = os.environ['prediction_key']
    endpoint = os.environ['prediction_endpoint']

    headers = {
        'Prediction-Key': prediction_key,
        'Content-Type': 'application/octet-stream'
    }

    # Call API
    detection_result = requests.post(url=endpoint, headers=headers, data=image)

    return detection_result