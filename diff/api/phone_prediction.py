import json
from data_generator import generateData
from calculate_probabilities import calculateProbabilities

def predictPhone(probAgeYoung, probWealthRich):
    loaded_data = generateData(probAgeYoung, probWealthRich)
    learned_probabilities = calculateProbabilities(loaded_data)
    
    combined_probs = {0: 0, 1: 0}
    for age in range(2):
        for wealth in range(2): 
            prob_age = probAgeYoung if age == 0 else 1 - probAgeYoung
            prob_wealth = probWealthRich if wealth == 1 else 1 - probWealthRich
            for phone in range(2):
                prob_phone = learned_probabilities['P(Phone | Age, Wealth)'][age][wealth].get(phone, 0)
                combined_probs[phone] += prob_age * prob_wealth * prob_phone

    total = combined_probs[0] + combined_probs[1]

    prob_apple = combined_probs[0] / total if total > 0 else 0
    prob_android = combined_probs[1] / total if total > 0 else 0

    phone = 'apple' if prob_android < prob_apple else 'android'
     
    return {
        "predicted_phone": phone,
        "prob_apple": prob_apple,
        "prob_android": prob_android
    }