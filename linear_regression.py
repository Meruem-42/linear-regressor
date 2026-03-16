import numpy as np
import pandas as pd
import linear_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import json

# def mse_calculation(theta0, theta1, mileage) :

def normalization(feature_list) :
    max = feature_list.max()
    min = feature_list.min()
    norm_list = (feature_list - min)/(max - min)
    return (norm_list)

def linear_regression(df) :
    X = df[['km']]
    y = df['price']

    model = LinearRegression()
    model.fit(X, y)

    print("TEST SCIKIT LEARN: ", (model.coef_, model.intercept_))


def main() :
    theta0 = 0
    theta1 = 0
    step = 0.1
    iterations = 10000
    with open("data.csv", "r") as f :
        data = pd.read_csv(f)
    data["km"] = normalization(data["km"])
    # data["price"] = normalization(data["price"])
    for j in range(iterations) :
        gradient0 = np.array([theta0 + theta1*data["km"][i] - data["price"][i] for i in range(len(data["price"]))]).mean()
        gradient1 = np.array([(theta0 + theta1*data["km"][i] - data["price"][i])*data["km"][i] for i in range(len(data["price"]))]).mean()
        theta0 -= step*gradient0
        theta1 -= step*gradient1
    mse_list = [pow(theta0 + theta1*data["km"][i] - data["price"][i], 2) for i in range(len(data["price"]))]    
    mse_result = np.array(mse_list).sum()/(len(data["price"])*2)
    linear_regression(data)
    with open("thetas.json", "r") as f :
        data = json.load(f)
    data["theta0"] = theta0
    data["theta1"] = theta1
    with open("thetas.json", "w") as f :
        json.dump(data, f, indent=4)

    print("TEST MY LINEAR REGRESSION: ", (theta0, theta1))
    print(mse_result)


if __name__ == "__main__" :
    main()