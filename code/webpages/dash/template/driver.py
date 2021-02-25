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


driverList = ['max_verstappen', 'ricciardo']
data=dj()
name = 'max_verstappen'
code = "NOR"
team = "red_bull"
lineup = "Red_Bull"

def get_DriverCareerPoints(name):
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
    fig = px.line(df, x="Season", y="Points")
    return fig


def get_QualiDiff(code):
    df = pd.read_csv("static/Data/QualiComparison/{}.csv".format(code))
    fig = px.bar(df, x="Round", y="Quali Time Difference")
    return fig

def get_TeamCareerPoints(team):
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
    fig = px.line(df, x="Season", y="Points")
    return fig

def get_ConstructorChampionship(team):
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Constructor[i] == team:
            Season = df.Season[i]
            Position = df.ConstructorStandings[i]
            position[Season] = Position
    df = {'Position': position.values(), 'Season': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Position")
    fig.update_layout(yaxis_range=[10,0])
    return fig

def get_DriverChampionship(name):
    df = pd.read_csv("static/Data/DriverStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Driver[i] == name:
            Season = df.Season[i]
            Position = df.DriverStandings[i]
            position[Season] = Position
    df = {'Position': position.values(), 'Season': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Season", y="Position")
    fig.update_layout(yaxis_range=[10,0])
    return fig

def get_DriverSeasonPoints(name):
    df = pd.read_csv("static/Data/DriverStandings.csv")
    points = {}
    for i in range(len(df)):
        if df.Driver[i] == name and df.Season[i] == 2020:
            Round = df.Round[i]
            Points = df.DriverPoints[i]
            points[Round] = Points
    df = {'Points': points.values(), 'Round': points.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.bar(df, x="Round", y="Points")
    return fig

def get_SeasonChampionship(team):
    df = pd.read_csv("static/Data/ConstructorStandings.csv")
    position = {}
    for i in range(len(df)):
        if df.Constructor[i] == team and df.Season[i] == 2020:
            Round = df.Round[i]
            Position = df.ConstructorStandings[i]
            position[Round] = Position
    df = {'Position': position.values(), 'Round': position.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.line(df, x="Round", y="Position")
    fig.update_layout(yaxis_range=[10,0])
    return fig

def get_TeamLineup(lineup):
    df = pd.read_csv("static/Data/TeamLineups/Red_Bull.csv")
    Lineup = {}
    for i in range(len(df)):
        driver = df.Driver[i]
        races = df.Races[i]
        Lineup[driver] = races
    df = {'Races': Lineup.values(), 'Driver': Lineup.keys()}
    df = pd.DataFrame.from_dict(df)
    fig = px.pie(df, values='Races', names='Driver', title='Share of each drivers time in a teams history')
    return fig

teamlist = ["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"]
teamcolour = ['#00D2BE', '#1E41FF', '#FF8700', '#F596C8', '#FFF500', '#C80000','#FFFFFF', '#9B0000', '#787878', '#0082FA']
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
    fig = px.line(standings, x="Round", y=["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"])
    fig.update_layout(yaxis_range=[11,0])
    for i in range(len(teamlist)):
        fig['data'][i]['line']['color']=teamcolour[i]
    return fig

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

awards = data[name]["awards_won"]
teams = data[name]["driver_for"]

layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(
    [
        dbc.Navbar(
            [
                dbc.Nav([dbc.NavLink(dbc.NavLink("Home", href="/ricciardo", active="exact")), dbc.NavLink(dbc.NavLink("Season", href="#", active="exact")), dbc.NavLink(dbc.NavLink("Predictor", href="#", active="exact")), dbc.NavLink(dbc.NavLink("Driver", href="#", active="exact")), dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Max Verstappen", href="/driver/max_verstappen"),
                dbc.DropdownMenuItem("Daniel Ricciardo", href="/driver/ricciardo"),
            ],
            nav=True,
            in_navbar=True,
            label="Drivers",
                )]),
            ],
            sticky="top",
            style={"font-size":"25px",
                    "height":"65px",
                    "background-color":"#F8EAE8",}
        ),
    ]
),
        #header
    html.Div(id='driver_dropdown'),
    html.Div([
    html.H1(data[name]["name"], style={'text-indent':'100px', 
                                        'line-height':'100%', 
                                        'clear':'both',
                                        'display':'inline-block',
                                        'padding-top':'1%'}),

    html.Img(src=data[name]["flag"], style={'width':'75px',
                                            'height':'45px',
                                            'display':'inline-block',
                                            'clear':'both'}),
    
    html.Img(src=data[name]["team_logo"], style={'height':'80%',
                                            'float':'right',
                                            'padding-top':'6%',
                                            'padding-right':'2.5%',
                                            'padding-left':'2%',
                                            'display':'inline-block'}),

    html.Img(src=data[name]["driver_photo"], style={'height':'120%',
                                            'padding-left':'2.5%',
                                            'padding-top' :'1%',
                                            'float':'right',
                                            'vertical-align':'top',}),

    html.H2(data[name]["team"], style={'text-indent':'100px',
                                        'vertical-align':'text-top',
                                        'line-height':'100%'}),
    #left
    html.Div([
        html.P("Age: " + data[name]["age"]),
        html.P("Entries: " + data[name]["entries"]),
        html.P("Titles: " + data[name]["titles"]),
        html.P('Poles: ' + data[name]["poles"]),
    ],id='left', style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'display':'inline-block'}),
    #right
    html.Div([
        html.P('Wins: ' + data[name]["wins"]),
        html.P('Podiums: ' + data[name]["podiums"]),
        html.P('First Start: ' + data[name]["first_start"]),
        html.P('First Win: ' + data[name]["first_win"]),
    ],id='right',style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'display':'inline-block'}),
    ],id='header', style={'background-color':data[name]["background-color"],
                            'height':'300px', 
                            'padding-top':'10px', 
                            'padding-bottom':'70px', 
                            'font-size':'35px',
                            'color':'black'}),
    dcc.Graph(
        id='example-graph', figure=get_DriverCareerPoints(name), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_QualiDiff(code), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_DriverSeasonPoints(name), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_DriverChampionship(name), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_TeamCareerPoints(team), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_ConstructorChampionship(team), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_SeasonChampionship(team), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_TeamLineup(lineup), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=get_FullSeasonChampionship(teamlist)),
    html.Div([
        html.H3('Awards Won:'),
        html.Ul(children=[html.Li(i) for i in awards]),
    ],id='awards', style={'float':'right',
                            'clear':'both',
                            'padding-right':'6%',
                            'padding-top':'4%'}),
    #teamHistory
    html.Div([
        html.H3('Team(s) Driven For:'),
        html.Ul(children=[html.Li(i) for i in teams]),
    ],id='teamHistory', style={'clear':'both',
                            'padding-left':'6%',
                            'padding-top':'4%'}),
    ], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%', 'font-size':'25px'})


if __name__ == '__main__':
    app.run_server(debug=True)
