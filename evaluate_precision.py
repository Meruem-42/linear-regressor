import pandas as pd
import math
import json

class EvaluateModel:
    def __init__(self) :
        pass

    @staticmethod    
    def mae(theta0, theta1, df):
        error = abs(theta0 + theta1*df["km"] - df["price"])
        return error.mean()
    
    @staticmethod
    def mse(theta0, theta1, df):
        error = pow(theta0 + theta1*df["km"] - df["price"], 2)
        return error.mean()

    @staticmethod
    def rmse(theta0, theta1, df):
        return math.sqrt(EvaluateModel.mse(theta0, theta1, df))

    @staticmethod
    def r_score(theta0, theta1, df):
        error_real = pow(theta0 + theta1*df["km"] - df["price"], 2)
        error_mean = pow(df["price"] - df["price"].mean(), 2)
        return 1 - (error_real.sum() / error_mean.sum())

def main() :
    with open("thetas.json", "r") as f :
        thetas = json.load(f)

    theta0 = thetas["theta0"]
    theta1 = thetas["theta1"]
    with open("data.csv", "r") as f :
        data = pd.read_csv(f)
    print("MAE : ", EvaluateModel.mae(theta0, theta1, data))
    print("MSE : ", EvaluateModel.mse(theta0, theta1, data))
    print("RMSE : ", EvaluateModel.rmse(theta0, theta1, data))
    print("R2 : ", EvaluateModel.r_score(theta0, theta1, data))

if __name__ == "__main__" :
    main()