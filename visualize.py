from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd 


df = pd.read_csv("pink_morsels_sales_data.csv")

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Sales Visualization", style = {
        "text-align": "center", 
        "color": "#F1B6AC"
        }),
    html.H2(children="Pink Morsels Sales",
        style={
        'textAlign': 'center',
        "color": "#FFDDD6"
        }),
    html.Div(children = [
    dcc.RadioItems(
        id = "region",
        options = [
        {'label': 'North', 'value': 'north'},
        {'label': 'South', 'value': 'south'},
        {'label': 'East', 'value': 'east'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'all'},
        ],
        value = 'all',
        labelStyle = {
            "padding": "15px",
            "display": "inline-block"
            }
        ),
    dcc.Graph(
        id = "pink_morsel_sale_graph",
        style = {
            "margin": "auto",
            "width": "95%",
            "height": "90%",
        }
    )],
    style = {
    "margin": "auto",
    "padding": "30px 10px",
    "textAlign": "center"
    })],
    style = {
        "width": "100%",
        "height": "100%",
        "backgroundColor": "#869F77"
    }
)


@callback(
    Output("pink_morsel_sale_graph", "figure"),
    Input("region", "value"))
def update_figure(region):
    new_df = df[df['region'] == region] if region != 'all' else df
    fig = px.line(new_df, x="date", y="sales",
                labels= {
                    "date": "Date",
                    "sales": "Sales"
                })
    fig.update_layout(transition_duration=600)
    
    return fig


if __name__ == "__main__":
    app.run(debug=True)