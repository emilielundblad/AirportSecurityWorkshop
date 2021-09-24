import requests
from detect_objects import detect_objects
import os, json
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize', methods=['GET', 'POST'])
def recognize():
    if request.method == 'POST':
        # Get image
        image = request.files['image']

        response = detect_objects(image)
        detection_results = json.loads(response.content)
        probability_threshold = int(request.form['probability-slider'])
        
        # Create tmp directory if not existent
        if not os.path.exists(os.path.join('static', 'tmp')):
            os.mkdir(os.path.join('static', 'tmp'))

        # Save image
        image_path = os.path.join('static', 'tmp', image.filename)
        image.seek(0)
        image.save(image_path)

        # Get list of dangerous objects from app settings
        try:
            dangerous_objects = os.environ['dangerous_objects']
            dangerous_objects = [x.strip() for x in dangerous_objects.split(',')]
        except KeyError:
            dangerous_objects = []
            print('Could not find dangerous_objects app setting!')

        return render_template('recognize.html', predictions=detection_results['predictions'], image=url_for('static', filename='tmp/' + image.filename), probability_threshold=probability_threshold, dangerous_objects=dangerous_objects)
    else:
        return render_template('index.html')