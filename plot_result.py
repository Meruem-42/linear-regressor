import plotly.express as px
import pandas as pd
from predictor import predictor
import json

def generate_model_line(data, theta0, theta1) :
    min = data["km"].min()
    max = data["km"].max()

    df = pd.DataFrame({
        "km": [min, max], 
        "price": [predictor(theta0, theta1, min), predictor(theta0, theta1, max)]
        })
    return df


def plot_all(data, theta0, theta1) :
    fig = px.scatter(data, x="km", y="price", title="Car Price relation with mileage")
    df_line = generate_model_line(data, theta0, theta1)
    fig.add_scatter(x=df_line["km"],y=df_line["price"], mode='lines', name='Prediction model')
    fig.show()

def main() :
    with open("data.csv", "r") as f :
        data = pd.read_csv(f)
    with open("thetas.json", "r") as f :
        thetas = json.load(f)
    plot_all(data, thetas["theta0"], thetas["theta1"])

if __name__ == "__main__" :
    main()