from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from phone_prediction import predictPhone

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['GET'])
def predict_phone_api():
    age_str = request.args.get('age')
    wealth_str = request.args.get('wealth')

    if age_str is None or wealth_str is None:
        return jsonify({"error": "Fehlende Parameter: 'age' und 'wealth' sind erforderlich."}), 400

    try:
        age = float(age_str)
        wealth = float(wealth_str)

    except ValueError:
        return jsonify({"error": "Ungueltiger Typ: 'age' und 'wealth' muessen ganze Zahlen sein."}), 400

    predictionData = predictPhone(age, wealth)
    print(predictionData)
   
    return jsonify({
        "input_age": age,
        "input_wealth": wealth,
        "predicted_phone": predictionData["predicted_phone"],
        "prob_apple": predictionData["prob_apple"],
        "prob_android": predictionData["prob_android"]
    })

if __name__ == '__main__':
    app.run()