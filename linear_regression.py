import numpy as np
import pandas as pd
import linear_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import json

def normalization(feature_list) :
    max = feature_list.max()
    min = feature_list.min()
    norm_list = (feature_list - min)/(max - min)
    return (norm_list)

def persistent_coeff(theta0, theta1) :
    with open("thetas.json", "r") as f :
        data = json.load(f)
    data["theta0"] = theta0
    data["theta1"] = theta1
    with open("thetas.json", "w") as f :
        json.dump(data, f, indent=4)
    print("TEST MY LINEAR REGRESSION: ", (theta0, theta1))

def denormalization(df, theta0, theta1) :
    km_min = df["km"].min()
    km_max = df["km"].max()
    price_min = df["price"].min()
    price_max = df["price"].max()
    km_range = km_max - km_min
    price_range = price_max - price_min
    real_theta1 = theta1 * (price_range / km_range)
    real_theta0 = theta0 * price_range + price_min - real_theta1 * km_min
    persistent_coeff(real_theta0, real_theta1)

def linear_regression_test(df) :
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
    km_norm = normalization(data["km"])
    price_norm = normalization(data["price"])
    for j in range(iterations) :
        predictor = theta0 + theta1*km_norm
        error = predictor - price_norm

        gradient0 = error.mean()
        gradient1 = (error*km_norm).mean()

        theta0 -= step*gradient0
        theta1 -= step*gradient1

    linear_regression_test(data)
    denormalization(data, theta0, theta1)


if __name__ == "__main__" :
    main()