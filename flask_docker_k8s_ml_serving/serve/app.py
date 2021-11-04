from flask import Flask, request, jsonify
import numpy as np
import pickle as p
from google.cloud import storage

# initialize the app
app = Flask(__name__)

# when the user sends a POST request


@app.route('/api', methods=['POST'])
def makecalc():
    # get the data from the user
    data = request.get_json()
    data = np.array(data).reshape(1, -1)

    # uses the model and the input data to predict
    pred = model.predict(data)
    prediction = np.array2string(pred)
    return jsonify(prediction)


if __name__ == '__main__':
    # to download from Google Cloud Storage the pickle file
    storage_client = storage.Client()
    bucket = storage_client.bucket('fp_farefain')
    # loads the pickle file
    blob = bucket.blob('prediction.pickle')
    # saves temporarily the pickle file
    temp_model_location = './temp_model.pickle'
    blob.download_to_filename(temp_model_location)
    with open(temp_model_location, "rb") as f:
        model = p.load(f)

    # runs the app
    # to run the app locally use host='127.0.0.1'
    app.run(debug=False, host='0.0.0.0')
