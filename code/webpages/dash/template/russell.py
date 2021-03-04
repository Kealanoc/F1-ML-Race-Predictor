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
name = 'russell'

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

awards = data[name]["awards_won"]
teams = data[name]["driven_for"]
code = data[name]["code"]
team = data[name]["graph_team"]
lineup = data[name]["team_lineup"]

teams_dd = dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Red Bull Racing", href="/team/red_bull"),
                dbc.DropdownMenuItem("Mercedes AMG", href="/team/mercedes"),
                dbc.DropdownMenuItem("Scuderia Ferrari", href="/team/ferrari"),
                dbc.DropdownMenuItem("Renault Sport", href="/team/renault"),
                dbc.DropdownMenuItem("McLaren F1 Team", href="/team/mclaren"),
                dbc.DropdownMenuItem("Racing Point F1 Team", href="/team/racingpoint"),
                dbc.DropdownMenuItem("AlphaTauri", href="/team/alphatauri"),
                dbc.DropdownMenuItem("Alfa Romeo Racing", href="/team/alfaromeo"),
                dbc.DropdownMenuItem("Haas F1 Team", href="/team/haas"),
                dbc.DropdownMenuItem("Williams Racing", href="/team/williams"),
            ],
            nav=True,
            in_navbar=True,
            label="Teams",
            style={
                "padding-top":"7px",
            }
                )

predictor_dd = dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Predictor", href="/predictor"),
                dbc.DropdownMenuItem("Predictor Information", href="/predictor_info"),
            ],
            nav=True,
            in_navbar=True,
            label="Predictor",
            style={
                "padding-top":"7px",
            }
                )
            
layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(
    [
        dbc.Navbar(
            [
                dbc.Nav([dbc.NavLink(dbc.NavLink("Home", href="/home", active="exact")), predictor_dd, teams_dd, dbc.DropdownMenu(
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
                            'color':'black',
                            'margin-bottom': '50px'}),
   html.Div([
        html.Div([
            html.H3('Driver Summary'),
            html.P("One of the finest young talents to enter F1 in a very long time. Russell has an earned pedigree not many other drivers could even think of. An F2 Championship victory over Lando Norris and Alex Albon along with a dominant GP3 vicotry over drivers like Jack Aitken and Anthoine Hubert. Despite this massive pedigree and the seemingly universally found opinion that he is a future champion, he has had very little chance to show his ability or growth. The coming years will be pivotal to Russell's career."),
        ],id='points', style={'margin-left':'3%',
                                'margin-top':'1%',
                                'width':'40%',
                                'float':'left',
                                'clear':'both'}),
        dcc.Graph(
            id='example-graph', figure=gs.get_DriverFinishesScatter(name, team), 
                        style={'height':'10%', 
                                'width':'40%', 
                                'margin-right':'3%', 
                                'margin-left':'12%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-right':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),

    html.Div([
        dcc.Graph(
            id='example-graph', figure=gs.get_DriverCareerPoints(name, team), 
                    style={'height':'20%', 'width':'40%', 
                                'display':'inline-block',
                                'margin-right': '15%', 
                                'margin-left':'3%',
                                'margin-top':'3%',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-left':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
        html.Div([
            html.H3('Awards Won:'),
            html.Ul(children=[html.Li(i) for i in awards]),
        ],id='awards', style={'padding-right':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'float':'right',
                                'clear':'both'}),
    ],style={}),
    #teamHistory
    html.Div([
        html.Div([
            html.H3('Team(s) Driven For:'),
            html.Ul(children=[html.Li(i) for i in teams]),
        ],id='teamHistory', style={'padding-left':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'float':'left',
                                'clear':'both'}),
        dcc.Graph(
            id='example-graph', figure=gs.get_DriverChampionship(name, team), 
                            style={'height':'10%', 
                                'width':'40%', 
                                'margin-right':'3%', 
                                'margin-left':'15%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-right':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),
    
    html.Div([
        dcc.Graph(
            id='example-graph', figure=gs.get_DriverSeasonPoints(name, team), 
                        style={'height':'20%', 
                                'width':'40%', 
                                'margin-left':'3%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-left':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
        html.Div([
            html.H3('2020 Season'),
            html.P("2020 was a rollercoaster season for Russell, coming into the season the Williams car was better than it had been in years. Due to him still being unable to find points and with fan pressure mounting from Latifi appearing equally close to points if not closer than him, he got an opportunity of a lifetime thanks to Hamilton's COVID diagnosis. A dominant performance over Bottas with a lot of heartbreak saw George pick up his first career points."),
        ],id='points', style={'float':'right',
                                'padding-right':'6%',
                                'padding-top':'2%',
                                'width':'40%',
                                'clear':'both'}),
    ]),
    html.Div([
        html.Div([
            html.H3('2020 Qualifying'),
            html.P("Russell came into the season unbeaten in qualifying against teammates after dominating Robert Kubica the previous year. He held that record right up until he was paired with Bottas and he lost by only a few milliseconds. When it comes to the Williams battle however, he dominated once again and remains unbeaten in qualifying a Williams. "),
        ],id='qualifying', style={'float':'left',
                                'padding-left':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'clear':'both'}),
        dcc.Graph(
            id='example-graph', figure=gs.get_QualiDiff(code, team), 
                            style={'height':'10%', 
                                'width':'40%', 
                                'margin-right':'3%', 
                                'margin-left':'15%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-right':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),
    

    ], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%', 'font-size':'25px','background-color': '#cccccc'}),

if __name__ == '__main__':
    app.run_server(debug=True)