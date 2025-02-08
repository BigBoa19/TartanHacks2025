from flask import Flask, jsonify
import joblib
import numpy as np
app = Flask(__name__)
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
    tuples = []
    for x,y in zip(X_test.tolist(), y_pred.tolist()):
        if y < 0:
            tuples.append((x,y))
    results = {
        # "pred": X_test.tolist()
        "pred": y_pred.tolist()
    }
    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)