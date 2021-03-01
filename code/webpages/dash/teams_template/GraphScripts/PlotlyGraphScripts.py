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

teamlist = ["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"]
teamcolour = ['#00D2BE', '#1E41FF', '#FF8700', '#F596C8', '#FFF500', '#C80000','#004C6C', '#9B0000', '#787878', '#0082FA']

def get_AlphaTauriPoints(team):
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    points = {}
    for i in range(len(df)):
        if df.Constructor[i] == team or df.Constructor[i] == "toro_rosso":
            Season = df.Season[i]
            if df.ConstructorPoints[i]!= "":
                Points = df.ConstructorPoints[i]
            points[Season] = Points
    df = {'Points': points.values(), 'Season': points.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Points")
    return fig

def get_AlphaTauriPosition(team):
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Constructor[i] == team or df.Constructor[i] == "toro_rosso":
            Season = df.Season[i]
            Position = df.ConstructorStandings[i]
            position[Season] = Position
    df = {'Position': position.values(), 'Season': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Position")
    fig.update_layout(yaxis_range=[10,0])
    return fig

def get_TeamCareerPoints(team):
    colour = teamlist.index(team)
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    points = {}
    for i in range(len(df)):
        if df.Constructor[i] == team:
            Season = df.Season[i]
            if df.ConstructorPoints[i]!= "":
                Points = df.ConstructorPoints[i]
            points[Season] = Points
    df = {'Points': points.values(), 'Season': points.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Points", color_discrete_sequence=[teamcolour[colour]], title='Teams Points Throughout History')
    return fig

def get_ConstructorChampionship(team):
    colour = teamlist.index(team)
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Constructor[i] == team:
            Season = df.Season[i]
            Position = df.ConstructorStandings[i]
            position[Season] = Position
    df = {'Position': position.values(), 'Season': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Position", color_discrete_sequence=[teamcolour[colour]], title='Constructor Standings Throughout Teams History')
    fig.update_layout(yaxis_range=[10,0])
    return fig

def get_SeasonChampionship(team):
    colour = teamlist.index(team)
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Constructor[i] == team and df.Season[i] == 2020:
            Round = df.Round[i]
            Position = df.ConstructorStandings[i]
            position[Round] = Position
    df = {'Position': position.values(), 'Round': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Round", y="Position", color_discrete_sequence=[teamcolour[colour]], title='Constructors Standings Throughout Previous Season')
    fig.update_layout(yaxis_range=[10,0])
    return fig

def get_TeamLineup(lineup):
    df = pd.read_csv("static/Data/TeamLineups/{}.csv".format(lineup))
    Lineup = {}
    for i in range(len(df)):
        driver = df.Driver[i]
        races = df.Races[i]
        Lineup[driver] = races
    df = {'Races': Lineup.values(), 'Driver': Lineup.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.pie(df, values='Races', names='Driver', title='Share of each drivers Time in Teams History')
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=6, uniformtext_mode='hide')
    return fig

def get_FullSeasonChampionship(teamlist):
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    standings = {}
    for team in teamlist:
        position = {}
        for i in range(len(df)):
            if df.Constructor[i] == team and df.Season[i] == 2020:
                Round = df.Round[i]
                Position = df.ConstructorStandings[i]
                position[Round] = Position
        if "Round" not in standings:
            standings["Round"] = position.keys()
        if team not in standings:
            standings[team] = position.values()
        standings = pd.DataFrame.from_dict(standings)
    fig = px.line(standings, x="Round", y=["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"], title='2020 Constructor Standings After Each Round')
    fig.update_layout(yaxis_range=[11,0])
    for i in range(len(teamlist)):
        fig['data'][i]['line']['color']=teamcolour[i]
    return fig


def get_TeamFinishesScatter(team):
    colour = teamlist.index(team)
    df = pd.read_csv("static/Data/TeamRaceFinishes/{}.csv".format(team))
    fig = px.scatter(df, x="Race_Num", y="RaceResult", color_discrete_sequence=[teamcolour[colour]], title='Positions of Every Recorded Race Finish In The Teams History')
    fig.update_layout(yaxis_range=[25,0])
    return fig