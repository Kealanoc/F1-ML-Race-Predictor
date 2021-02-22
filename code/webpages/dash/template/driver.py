import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from formulaml_dash import app
import plotly.express as px
import pandas as pd

name = "max_verstappen"
code = "VER"
team = "red_bull"
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

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

awards = ['2014, 15, 16, 19 FIA Action of the Year', '2015, 16, 17 FIA Personality of the Year', '2015 FIA Rookie of the Year', '2016 Lorenzo Bandini Trophy', '2014 FIA European Formula 3 Championship Third Place']
teams = ['2014-2016: Scuderia Toro Rosso', '2016-Present: Red Bull Racing']

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    #header
    html.Div([
    html.H1('Max Verstappen', style={'text-indent':'100px', 
                                        'line-height':'100%', 
                                        'clear':'both',
                                        'display':'inline-block',
                                        'padding-top':'1%'}),
    html.Img(src="../../static/assets/flags/netherlands_flag.png", style={'width':'75px',
                                                                        'height':'45px',
                                                                        'display':'inline-block',
                                                                        'clear':'both'}),
    html.Img(src="../../static/assets/logos/redbull_logo.png", style={'height':'80%',
                                                                    'float':'right',
                                                                    'padding-top':'6%',
                                                                    'padding-right':'2.5%',
                                                                    'padding-left':'2%',
                                                                    'display':'inline-block'}),
    html.Img(src="../../static/assets/portraits/verstappen_photo.png", style={'height':'120%',
                                                                            'padding-left':'2.5%',
                                                                            'padding-top' :'1%',
                                                                            'float':'right',
                                                                            'vertical-align':'top',}),
    html.H2('Red Bull Racing', style={'text-indent':'100px',
                                        'vertical-align':'text-top',
                                        'line-height':'100%'}),
    #left
    html.Div([
        html.P('Age: 23'),
        html.P('Entries: 119'),
        html.P('Titles: 0'),
        html.P('Poles: 3'),
    ],id='left', style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'display':'inline-block'}),
    #right
    html.Div([
        html.P('Wins: 10'),
        html.P('Podiums: 42'),
        html.P('First Start: 2015 Australian Grand Prix'),
        html.P('First Win: 2016 Spanish Grand Prix'),
    ],id='right',style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'display':'inline-block'}),
    ],id='header', style={'background-color':'#223971',
                            'height':'300px', 
                            'padding-top':'10px', 
                            'padding-bottom':'70px', 
                            'font-size':'35px',
                            'color':'black'}),
    dcc.Graph(
        id='example-graph', figure=get_DriverCareerPoints(name)),
    dcc.Graph(
        id='example-graph', figure=get_QualiDiff(code)),
    dcc.Graph(
        id='example-graph', figure=get_DriverSeasonPoints(name)),
    dcc.Graph(
        id='example-graph', figure=get_DriverChampionship(name)),
    dcc.Graph(
        id='example-graph', figure=get_TeamCareerPoints(team)),
    dcc.Graph(
        id='example-graph', figure=get_ConstructorChampionship(team)),
    dcc.Graph(
        id='example-graph', figure=get_SeasonChampionship(team)),
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
