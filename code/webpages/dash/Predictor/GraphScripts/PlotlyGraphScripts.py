import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from formulaml_dash import app
from driver_json import driver_json as dj
import flask
from urllib.parse import urlparse
from dash.dependencies import Input, Output, State
from markupsafe import escape
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=17, cols=2, shared_yaxes=True, column_widths=[0.5, 0.5])
fig.update_layout(showlegend=False, title_text="Model Prediciton Data Compared with Real Results")
def get_prediction(code):
    for i in range(16):
        num = i+1
        df = pd.read_csv("static/Data/Predictions/2020_{}.csv".format(str(num)))
        driver = []
        actual = []
        results = []
        for i in range(len(df.Driver)):
            pos = i+1
            driver.append(df.Driver[i])
            actual.append(df.Podium[i])
            results.append(pos)
        get_plot(driver,results,actual, num)
    return fig

def get_plot(driver,results, actual, num):

    fig.add_trace(go.Bar(x=driver, y=results, name="Predicted"),
                row=num, col=1)
    fig.add_trace(go.Bar(x=driver, y=actual, name="Actual"),
                row=num, col=2)

def get_FeatureImportance():
    df = pd.read_csv("static/Data/Predictions/2020_FeatureImportance")
    params = []
    vals = []
    for i in range(len(df.columns)):
        params.append(df.columns[i])
        vals.append(df[df.columns[i]][0])
    graph = go.Figure([go.Bar(x=params, y=vals, name="Feature Importance For the 2020 Season")])
    return graph
