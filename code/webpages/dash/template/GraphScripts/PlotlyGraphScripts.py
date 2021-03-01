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

teamlist = {"mercedes":'#00D2BE', "red_bull": '#1E41FF', "mclaren":'#FF8700', "racing_point":'#F596C8', "renault":'#FFF500', "ferrari":'#C80000',"alphatauri":'#FFFFFF', "alfa_romeo":'#9B0000', "haas":'#787878', "williams":'#0082FA'}
def get_DriverCareerPoints(name, team):
    teamcolour = teamlist[team]
    df = pd.read_csv("static/Data/DriverStandings.csv")
    points = {}
    for i in range(len(df)):
        j = i+1
        if df.Driver[i] == name:
            Season = df.Season[i]
            Points = df.DriverPoints[i]
            points[Season] = Points
    df = {'Points': points.values(), 'Season': points.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Points", color_discrete_sequence=[teamcolour], title='Driver Points Throughout Career')
    return fig


def get_QualiDiff(code, team):
    teamcolour = teamlist[team]
    df = pd.read_csv("static/Data/QualiComparison/{}.csv".format(code))
    fig = px.bar(df, x="Round", y="Quali Time Difference", color_discrete_sequence=[teamcolour], title='Qualifying Performance Vs Teammate (Lower = Better)')
    return fig

def get_DriverChampionship(name, team):
    teamcolour = teamlist[team]
    df = pd.read_csv("static/Data/DriverStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Driver[i] == name:
            Season = df.Season[i]
            Position = df.DriverStandings[i]
            position[Season] = Position
    df = {'Position': position.values(), 'Season': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Position", color_discrete_sequence=[teamcolour], title='Driver Championship Throughout Career')
    fig.update_layout(yaxis_range=[20,0])
    return fig

def get_DriverSeasonPoints(name, team):
    teamcolour = teamlist[team]
    df = pd.read_csv("static/Data/DriverStandings.csv")
    points = {}
    for i in range(len(df)):
        if df.Driver[i] == name and df.Season[i] == 2020:
            Round = df.Round[i]
            Points = df.DriverPoints[i]
            points[Round] = Points
    df = {'Points': points.values(), 'Round': points.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.bar(df, x="Round", y="Points", color_discrete_sequence=[teamcolour], title='Driver Points Throughout Season')
    return fig

def get_DriverFinishesScatter(name, team):
    teamcolour = teamlist[team]
    df = pd.read_csv("static/Data/DriverRaceFinishes/{}.csv".format(name))
    fig = px.scatter(df, x="Race_Num", y="RaceResult", color_discrete_sequence=[teamcolour], title='Driver Points Throughout History')
    fig.update_layout(yaxis_range=[25,0])
    return fig
