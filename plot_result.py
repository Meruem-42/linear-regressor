import plotly.express as px
import pandas as pd
from predictor import predictor
import json

def generate_model_line(data) :
    min = data["km"].min()
    max = data["km"].max()
    with open("thetas.json", "r") as f :
        thetas = json.load(f)

    theta0 = thetas["theta0"]
    theta1 = thetas["theta1"]
    df = pd.DataFrame({
        "km": [min, max], 
        "price": [predictor(theta0, theta1, min), predictor(theta0, theta1, max)]
        })
    return df


def plot_all() :
    with open("data.csv", "r") as f :
        data = pd.read_csv(f)

    fig = px.scatter(data, x="km", y="price", title="Price thanks to mileage")
    df_line = generate_model_line(data)
    fig.add_scatter(x=df_line["km"],y=df_line["price"], mode='lines', name='Prediction model')
    fig.show()

if __name__ == "__main__" :
    plot_all()