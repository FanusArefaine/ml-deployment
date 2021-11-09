from flask import Flask, request, jsonify
import numpy as np
import pickle as p
from ast import literal_eval
from google.cloud import storage
from predict import Predictor
from keras.models import load_model


# initialize the app
app = Flask(__name__)

# when the user sends a POST request


@app.route('/api', methods=['POST'])
def makecalc():
    # get the data from the user
    data = request.get_json()
    data = literal_eval(data)

    # uses the model and the input data to predict
    predictor = Predictor()
    predictions = predictor.generate_notes(model, data)
    #prediction = np.array2string(pred)
    return jsonify(predictions)


if __name__ == '__main__':
    # to download from Google Cloud Storage the pickle file
    storage_client = storage.Client()
    bucket = storage_client.bucket('claudio_pro')
    # loads the pickle file
    blob = bucket.blob('sequence_model.h5')
    # saves temporarily the pickle file
    temp_model_location = './sequence_model.h5'
    blob.download_to_filename(temp_model_location)
    model = load_model(temp_model_location)

    # runs the app
    # to run the app locally use host='127.0.0.1'
    app.run(debug=False, host='0.0.0.0')
