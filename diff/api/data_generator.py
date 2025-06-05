import random
import json
import os

from validate_data import validateData

# young is 0 and old is 1
# poor is 0 and rich is 1
# apple is 0 and android 1

def generateData(age, wealth):
    results = []

    total_cnt = 100000

    ap_cnt = 0
    an_cnt = 0
    y_cnt= 0
    o_cnt = 0
    p_cnt = 0
    r_cnt = 0

    for i in range(total_cnt):
        dataArray = []
        rand = random.random()

        # young or old
        if rand <= age:
            # young
            dataArray.append(0)
            y_cnt += 1
            
        else:
            # old
            dataArray.append(1)
            o_cnt += 1

        # poor or rich
        rand = random.random()

        if rand <= 1 - wealth:
            # poor
            dataArray.append(0)
            p_cnt += 1
        else:
            # rich
            dataArray.append(1)
            r_cnt += 1

        # apple or android
        if dataArray[0] == 0 and dataArray[1] == 0:
            rand = random.random()

            if rand > 0.7:
                ap_cnt += 1
                dataArray.append(0)
            else:
                an_cnt += 1
                dataArray.append(1)

        elif dataArray[0] == 0 and dataArray[1] == 1:
            rand = random.random()

            if rand > 0.05:
                ap_cnt += 1
                dataArray.append(0)
            else:
                an_cnt += 1
                dataArray.append(1)

        elif dataArray[0] == 1 and dataArray[1] == 0:
            rand = random.random()

            if rand > 0.98:
                ap_cnt += 1
                dataArray.append(0)
            else:
                an_cnt += 1
                dataArray.append(1)

        else:
            rand = random.random()

            if rand > 0.2:
                ap_cnt += 1
                dataArray.append(0)
            else:
                an_cnt += 1
                dataArray.append(1)

        results_file = "results.json"

        results.append(dataArray)


    with open(results_file, "w") as file:
        json.dump(results, file)

    validateData()
    return results