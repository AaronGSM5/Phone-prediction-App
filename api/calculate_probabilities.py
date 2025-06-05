import json
from utils import writeJsonFile

def calculateProbabilities(loaded_data):
    counts_phone_given_age_wealth = {}
    counts_age_wealth = {}

    for dataArray in loaded_data:
        age = dataArray[0]
        wealth = dataArray[1]
        phone = dataArray[2]

        if age not in counts_age_wealth:
            counts_age_wealth[age] = {}
        counts_age_wealth[age][wealth] = counts_age_wealth[age].get(wealth, 0) + 1

        if age not in counts_phone_given_age_wealth:
            counts_phone_given_age_wealth[age] = {}
        if wealth not in counts_phone_given_age_wealth[age]:
            counts_phone_given_age_wealth[age][wealth] = {}
        counts_phone_given_age_wealth[age][wealth][phone] = counts_phone_given_age_wealth[age][wealth].get(phone, 0) + 1

    learned_probabilities = {
        'P(Phone | Age, Wealth)': {},
    }

    # calculate all probabilities for P(Phone | Age, Wealth )
    for age in range(2):
        learned_probabilities['P(Phone | Age, Wealth)'][age] = {}
        for wealth in range(2):
            total_for_group = counts_age_wealth.get(age, {}).get(wealth, 0)

            learned_probabilities['P(Phone | Age, Wealth)'][age][wealth] = {}
            for phone in range(2):
                count = counts_phone_given_age_wealth.get(age, {}).get(wealth, {}).get(phone, 0)
                if total_for_group == 0:
                    learned_probabilities['P(Phone | Age, Wealth)'][age][wealth][phone] = 0
                else:
                    learned_probabilities['P(Phone | Age, Wealth)'][age][wealth][phone] = count / total_for_group
    
    writeJsonFile('probabilities.json', learned_probabilities)

    return learned_probabilities