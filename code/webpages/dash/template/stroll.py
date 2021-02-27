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
from .GraphScripts import PlotlyGraphScripts as gs

data=dj()
name = 'stroll'

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

awards = data[name]["awards_won"]
teams = data[name]["driven_for"]
code = data[name]["code"]
team = data[name]["graph_team"]
lineup = data[name]["team_lineup"]

layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(
    [
        dbc.Navbar(
            [
                dbc.Nav([dbc.NavLink(dbc.NavLink("Home", href="/home", active="exact")), dbc.NavLink(dbc.NavLink("Season", href="#", active="exact")), dbc.NavLink(dbc.NavLink("Predictor", href="#", active="exact")), dbc.NavLink(dbc.NavLink("Teams", href="#", active="exact")), dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Max Verstappen", href="/driver/verstappen"),
                dbc.DropdownMenuItem("Daniel Ricciardo", href="/driver/ricciardo"),
                dbc.DropdownMenuItem("Lewis Hamilton", href="/driver/hamilton"),
                dbc.DropdownMenuItem("Kimi Raikkonen", href="/driver/raikkonen"),
                dbc.DropdownMenuItem("Sebastian Vettel", href="/driver/vettel"),
                dbc.DropdownMenuItem("Lando Norris", href="/driver/norris"),
                dbc.DropdownMenuItem("George Russell", href="/driver/russell"),
                dbc.DropdownMenuItem("Alex Albon", href="/driver/albon"),
                dbc.DropdownMenuItem("Sergio Perez", href="/driver/perez"),
                dbc.DropdownMenuItem("Esteban Ocon", href="/driver/ocon"),
                dbc.DropdownMenuItem("Lance Stroll", href="/driver/stroll"),
                dbc.DropdownMenuItem("Nicolas Latifi", href="/driver/latifi"),
                dbc.DropdownMenuItem("Kevin Magnussen", href="/driver/magnussen"),
                dbc.DropdownMenuItem("Romain Grosjean", href="/driver/grosjean"),
                dbc.DropdownMenuItem("Carlos Sainz Jr.", href="/driver/sainz"),
                dbc.DropdownMenuItem("Charles Leclerc", href="/driver/leclerc"),
                dbc.DropdownMenuItem("Valtteri Bottas", href="/driver/bottas"),
                dbc.DropdownMenuItem("Antonio Giovinazzi", href="/driver/giovinazzi"),
                dbc.DropdownMenuItem("Pierre Gasly", href="/driver/gasly"),
                dbc.DropdownMenuItem("Daniil Kvyat", href="/driver/kvyat"),
            ],
            nav=True,
            in_navbar=True,
            label="Drivers",
            style={
                "padding-top":"7px",
            }
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
        html.P('First Podium: ' + data[name]["first_win"]),
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
    #dcc.Graph(
        #id='example-graph', figure=gs.get_TeamCareerPoints(team), style={'height':'300px', 'width':'500px'}),
    #dcc.Graph(
       # id='example-graph', figure=gs.get_ConstructorChampionship(team), style={'height':'300px', 'width':'500px'}),
    #dcc.Graph(
        #id='example-graph', figure=gs.get_SeasonChampionship(team), style={'height':'300px', 'width':'500px'}),
    #dcc.Graph(
        #id='example-graph', figure=gs.get_TeamLineup(lineup), style={'height':'300px', 'width':'500px'}),
    dcc.Graph(
        id='example-graph', figure=gs.get_DriverCareerPoints(name), style={'height':'20%', 'width':'40%', 'display':'inline-block', 'margin-left':'3%'}),
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
    ],id='teamHistory', style={'padding-left':'6%',
                            'padding-top':'4%',
                            'width':'40%',
                            'float':'left',
                            'clear':'both'}),
    dcc.Graph(
        id='example-graph', figure=gs.get_DriverChampionship(name), style={'height':'10%', 'width':'40%', 'margin-right':'3%', 'margin-left':'15%', 'display':'inline-block'}),
    
    dcc.Graph(
        id='example-graph', figure=gs.get_DriverSeasonPoints(name), style={'height':'20%', 'width':'40%', 'margin-left':'3%', 'display':'inline-block'}),
    
    html.Div([
        html.H3('2020 Season'),
        html.P('The 2020 season was strong for Max despite some unfortunate circumstances at Monza, Tuscany and Sakhir among others. However in a season where you only finish outside the podium once is an incredible achivement, and really shows the elite skill of Max.'),
    ],id='points', style={'float':'right',
                            'padding-right':'6%',
                            'padding-top':'4%',
                            'width':'40%',
                            'clear':'both'}),
    
    html.Div([
        html.H3('2020 Qualifying'),
        html.P("Along with a year with strong finishes, Max had a year where he was untouchable in qualifying. Albon his teammate of course doesn't have the same amount of experience or the same F1 pedigree Max has but was expected to put up more of a fight than he ended up giving."),
    ],id='qualifying', style={'float':'left',
                            'padding-left':'6%',
                            'padding-top':'4%',
                            'width':'40%',
                            'clear':'both'}),
    
    dcc.Graph(
        id='example-graph', figure=gs.get_QualiDiff(code), style={'height':'10%', 'width':'40%', 'margin-right':'3%', 'margin-left':'15%', 'display':'inline-block'}),

    ], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%', 'font-size':'25px'}),

if __name__ == '__main__':
    app.run_server(debug=True)