from flask import Flask, jsonify
from flask_cors import CORS
import joblib
import numpy as np
app = Flask(__name__)
CORS(app)
# Load the pre-trained model and test data from disk
model = joblib.load('/home/csinger/cmu/analysis/newmodel.pkl')
X_test = joblib.load('/home/csinger/cmu/analysis/x_test_test.pkl')
# Use the model to predict on the test set
y_pred = model.predict(X_test)
@app.route('/api/get_predictions', methods=['GET'])
def get_predictions():
    """
    Returns the actual target values (y_test) and the model's predictions (y_pred)
    on the test set as JSON.
    """
    entries = []
    dates = []
    for date in range(len(y_pred)):
        dates.append(date)
    # zip(range(len(y_pred.tolist())), y_pred.tolist()):
    padded_temps = X_test.tolist()[0][28:35]
    padded_temps.extend(X_test.tolist()[7][28:35])
    # for idx in range(14):
    #     if idx <= 13:
    #         padded_temps.append(X_test.tolist()[0][0:13][idx])
    #     else:
    #         padded_temps.append(None)
    print(len(padded_temps))
    for date, temp, price in zip(dates[:13], padded_temps, y_pred.tolist()[:13]):
        entries.append(
            {
                "Date": date,
                "Price": price
            }
        )
    results = {
        # "pred": X_test.tolist()
        # "dates": dates[:13],
        # "pred": y_pred.tolist()[:13],
        # "temps": X_test.tolist()[0][28:35]
        "entries": entries
        
    }

    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)