import numpy as np
import json

def predictor(theta0, theta1, mileage_value) :
    return theta0 + theta1*mileage_value
     
# def denormalization(prediction) :
#     max = feature_list.max()
#     min = feature_list.min()
#     real_prediction = (prediction + min) *(max - min)
#     return (real_prediction)

def main():
    with open("thetas.json", "r") as f :
        data = json.load(f)


    theta0 = data["theta0"]
    theta1 = data["theta1"]
    mileage = float(input("Enter a mileage: "))
    predicted_value = predictor(theta0, theta1, mileage)
    print("The expected price is: ", predicted_value)


if __name__ == "__main__" :
    main()
