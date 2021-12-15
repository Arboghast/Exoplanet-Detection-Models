from flask import Flask, jsonify, request, send_file, Response, json
import base64
from PIL import Image
import io
import inputlightcurve
import json
import inference
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
'''
json would look like
selection = {
            "input" = "KIC 3733346"
            "training_data" = "kaggle"
            "processing" = "tsfresh"
            "models" = ["rnn", "lstm", "gru"] }
'''
results = {"RNN": {"Probability":50, "Exoplanet exists?": "Yes"},
        "LSTM": {"Probability":69, "Exoplanet exists?": "Yes"},
        "GRU": {"Probability":70, "Exoplanet exists?": "Yes"}}
@app.route('/', methods=['GET'])
def data():
    input = request.args.get('input')
    training_data = request.args.get('training_data')
    processing = request.args.get('processing')
    models = request.args.get('models')

    #function that takes input, training, processing and models and returns the results object
    dict_data = {
    "targetpixelfile" : inputlightcurve.getTPFimg(input),
    "lightcurve" : inputlightcurve.getLCimg(input),
    "results" : inference.predict(input, training_data, processing, models)
    }
    return dict_data
'''
@app.route('/get_image')
def get_image():
    imgdata = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(imgdata))
    return send_file(imgdata, mimetype='image/png')
'''

'''
RETURN:
    {
    "targetpixelfile" : encoded_image_of_byte_code_of_targetpixelfile
    "lightcurve" : encoded_image_of_byte_code_of_lightcurve
    "results" : {
        "RNN" : {"Probability":50, "classification": "Yes"}
        "LSTM" : {"Probability":69, ""classification": "Yes"}
        "GRU" : {"Probability":70, ""classification": "Yes"}}
    }
    
    targetPixelFile object
    MAYBE: Also want to send back the light curve

    Results:

    Model_Name:
        Probability as a percentage
        50% or Higher = Yes
        Lower than 50% = No
'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=False)