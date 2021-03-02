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
