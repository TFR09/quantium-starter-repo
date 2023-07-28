from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 

app = Dash(__name__)

df = pd.read_csv("pink_morsels_sales_data.csv")

fig = px.scatter(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children="Pink Morsels Sales"),
    dcc.Graph(
        id = "pink morsel sale graph",
        figure = fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)