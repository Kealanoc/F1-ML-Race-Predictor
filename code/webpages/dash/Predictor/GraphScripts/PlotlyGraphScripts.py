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
import plotly.graph_objects as go

driverlist = {
    "hamilton":'#00D2BE',
    "bottas":'#00D2BE', 
    "max_verstappen": '#1E41FF',
    "albon": '#1E41FF', 
    "sainz":'#FF8700',
    "norris":'#FF8700', 
    "perez":'#F596C8',
    "stroll":'#F596C8', 
    "ocon":'#FFF500',
    "ricciardo":'#FFF500', 
    "vettel":'#C80000',
    "leclerc":'#C80000',
    "kvyat":'#004C6C',
    "gasly":'#004C6C', 
    "raikkonen":'#9B0000',
    "giovinazzi":'#9B0000', 
    "kevin_magnussen":'#787878',
    "grosjean":'#787878',  
    "latifi":'#0082FA',
    "russell":'#0082FA'}

def get_prediction(code):
    df = pd.read_csv("static/Data/Predictions/2020_1.csv")
    driver = []
    results = []
    actual = []
    for i in range(len(df.Driver)):
        pos = i+1
        driver.append(df.Driver[i])
        actual.append(df.Podium[i])
        results.append(pos)
    fig = go.Figure(
        data=[
            go.Bar(name='Predicted', x=driver, y=results, yaxis='y', offsetgroup=1),
            go.Bar(name='Actual', x=driver, y=actual, yaxis='y2', offsetgroup=2)
        ],
        layout={
            'yaxis': {'title': 'SF Zoo axis'},
            'yaxis2': {'title': 'LA Zoo axis', 'overlaying': 'y', 'side': 'right'}
        }
    )
    # Change the bar mode
    fig.update_layout(barmode='group')
    return fig
