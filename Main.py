import pandas as pd
import pickle
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/predict', methods=['POST'])
def index():
    prediction = None  # Initialize the prediction variable
    flag = False
    if request.method == 'POST':
        user_temp = float(request.form['temperature-input1'])
        user_humidity = float(request.form['humidity-input1'])
        user_eco2 = float(request.form['co2-input1'])
        user_h2 = float(request.form['h2-input1'])

        # Define your columns
        columns = ['Temperature[C]', 'Humidity[%]', 'eCO2[ppm]', 'Raw H2']

        # Define your data
        x = pd.DataFrame(data=[[user_temp, user_humidity, user_eco2, user_h2]], columns=columns)

        filename = "my_model.pickle"
        loaded_model = pickle.load(open(filename, "rb"))

        # Predict the labels for the test data
        y_pred = loaded_model.predict(x)
        prediction = y_pred[0]

    response_data = {'flag': bool(prediction)}  # Convert the prediction to boolean and include it in the JSON response

    return jsonify(response_data)  # Return the response data as JSON


if __name__ == '__main__':  # Fix "__main__" here
    app.run(debug=True)
