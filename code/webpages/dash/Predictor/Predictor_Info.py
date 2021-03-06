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
import dash_table
from .GraphScripts import PlotlyGraphScripts as gs

data=dj()
name = 'bottas'

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
racedata = pd.read_csv("static/Data/RaceData.csv")
raceresults = pd.read_csv("static/Data/RaceResults.csv")
awards = data[name]["awards_won"]
teams = data[name]["driven_for"]
code = data[name]["code"]
team = data[name]["graph_team"]
lineup = data[name]["team_lineup"]

teams_dd = dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Red Bull Racing", href="/team/red_bull/"),
                dbc.DropdownMenuItem("Mercedes AMG", href="/team/mercedes/"),
                dbc.DropdownMenuItem("Scuderia Ferrari", href="/team/ferrari/"),
                dbc.DropdownMenuItem("Renault Sport", href="/team/renault/"),
                dbc.DropdownMenuItem("McLaren F1 Team", href="/team/mclaren/"),
                dbc.DropdownMenuItem("Racing Point F1 Team", href="/team/racingpoint/"),
                dbc.DropdownMenuItem("AlphaTauri", href="/team/alphatauri/"),
                dbc.DropdownMenuItem("Alfa Romeo Racing", href="/team/alfaromeo/"),
                dbc.DropdownMenuItem("Haas F1 Team", href="/team/haas/"),
                dbc.DropdownMenuItem("Williams Racing", href="/team/williams/"),
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
                dbc.DropdownMenuItem("Predictor", href="/predictor/"),
                dbc.DropdownMenuItem("Predictor Information", href="/predictor_info/"),
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
                dbc.Nav([dbc.NavLink(dbc.NavLink("Home", href="/", active="exact")), predictor_dd, teams_dd, dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Max Verstappen", href="/driver/verstappen/"),
                dbc.DropdownMenuItem("Daniel Ricciardo", href="/driver/ricciardo/"),
                dbc.DropdownMenuItem("Lewis Hamilton", href="/driver/hamilton/"),
                dbc.DropdownMenuItem("Kimi Raikkonen", href="/driver/raikkonen/"),
                dbc.DropdownMenuItem("Sebastian Vettel", href="/driver/vettel/"),
                dbc.DropdownMenuItem("Lando Norris", href="/driver/norris/"),
                dbc.DropdownMenuItem("George Russell", href="/driver/russell/"),
                dbc.DropdownMenuItem("Alex Albon", href="/driver/albon/"),
                dbc.DropdownMenuItem("Sergio Perez", href="/driver/perez/"),
                dbc.DropdownMenuItem("Esteban Ocon", href="/driver/ocon/"),
                dbc.DropdownMenuItem("Lance Stroll", href="/driver/stroll/"),
                dbc.DropdownMenuItem("Nicolas Latifi", href="/driver/latifi/"),
                dbc.DropdownMenuItem("Kevin Magnussen", href="/driver/magnussen/"),
                dbc.DropdownMenuItem("Romain Grosjean", href="/driver/grosjean/"),
                dbc.DropdownMenuItem("Carlos Sainz Jr.", href="/driver/sainz/"),
                dbc.DropdownMenuItem("Charles Leclerc", href="/driver/leclerc/"),
                dbc.DropdownMenuItem("Valtteri Bottas", href="/driver/bottas/"),
                dbc.DropdownMenuItem("Antonio Giovinazzi", href="/driver/giovinazzi/"),
                dbc.DropdownMenuItem("Pierre Gasly", href="/driver/gasly/"),
                dbc.DropdownMenuItem("Daniil Kvyat", href="/driver/kvyat/"),
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
    
    html.H1("Machine Learning Model", style={'text-indent':'100px', 
                                        'line-height':'100%', 
                                        'clear':'both',
                                        'display':'inline-block',
                                        'padding-top':'1%'}),
    html.H2("Random Forest Regressor", style={'text-indent':'100px', 
                                        'line-height':'100%', 
                                        'clear':'both'}),
                                        
    #left
    html.Div([
        html.P("Regression Based Algorithm"),
        html.P("Real Data From FIA Archives"),
        html.P("1.7 million Data Points"),
    ],id='left', style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'margin-top': '20px',
                            'display':'inline-block',
                            'font-size':'25px',}),

    ],id='header', style={'background-color':data[name]["background-color"],
                            'height':'300px', 
                            'padding-top':'10px', 
                            'padding-bottom':'70px', 
                            'font-size':'35px',
                            'color':'black',
                            'margin-bottom': '50px'}),
    
    html.Div([
        html.Div([
            html.H3('Algorithm Summary'),
            html.P('This Web Application has featured many dashboards displaying analysis and statistics on every driver and team currency competing in Formula 1. This data can give you a great insight into not only the performance of a driver or team, but also an insight into their strengths and weaknesses’. All of our data is gathered from real world data sourced from the FIAs own public archives; The oldest data dates back as far as 1950 and the inception of Formula 1. However our purpose of this Application was not just to show basic analysis and data on drivers and teams but also to use the data we have gathered to create a machine learning model in order to demonstrate how powerful even simple publicly available data can allow you to predict the outcome of a race. In this Dashboard we will outline how we created our algorithm and will show you the results of our predictions.'),
        ],id='Intro', style={'padding-left':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'float':'left',
                                'clear':'both'}),
        html.Div([                        
            dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} 
                    for i in racedata.columns],
            page_size=20,
            data=racedata.to_dict('records'),
            css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
            style_cell={
            'width': '1%',
            'textOverflow': 'ellipsis',
            'overflow': 'hidden',
            'textAlign':'left'},
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender"),),
        ],  style={ 
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
        html.Div([
            html.H3('Gathering Data'),
            html.P('The first step in creating our algorithm was to gather all of the data. We achieved this by using an open source API called Ergast, that allows us to access the FIA archives through HTTP requests. The data is then returned via JSON data and stored in DataFrames. To the left and above you can see two examples of these DataFrames. In Total we Have six DataFrames, including RaceData (above), RaceResults (left), DriversStandings, ConstructorsStandings, Weather, and Qualifying data. The archives are not perfect so work had to be done to fill in as much missing data as we could by using web scrapers to get information and data from other sources. Once all of our data was assembled it was time to merge the data into one large DataFrame that could be analyzed and used for our Model. The final DataFrame contains 14,606 rows and 116 columns of data.'),
        ],id='Intro', style={'padding-right':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'float':'right',
                                'clear':'both'}),
        html.Div([                        
            dash_table.DataTable(
            id='table',
            columns=[{"name": raceresults.columns[i], "id": raceresults.columns[i]} 
                    for i in range(3,len(raceresults.columns)-2)],
            page_size=20,
            data=raceresults.to_dict('records'),
            css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
            style_cell={
            'width': '1%',
            'textOverflow': 'ellipsis',
            'overflow': 'hidden',
            'textAlign':'left'},
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender"),),
        ],  style={ 
                                'width':'40%', 
                                'margin-left':'3%', 
                                'margin-right':'15%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-left':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),

    html.Div([
        html.Div([
            html.H3('How the Algorithm Works'),
            html.P('The Algorithm itself is based on Regression.  Regression  is a statistical process for estimating the relationships between a dependent variable. In more simple terms, the algorithm takes in a variable which will be the goal, For example who will win  the Race. The algorithm will then look through all of the previous occurrences of Drivers, winning a grand prix and examine the parameters that were at play at the time. For example how experienced the driver was at that point, how well the team was performing, the weather at the time and much more. After this is done the algorithm will then weight parameters according to what it believes will give the greatest accuracy. The weight of the parameters affects how much or how little they influence the outcome. We are able to train the algorithm to do this by feeding it all the data from each year up until 2019 and having it predict the 2020 season. This is exactly what we did to demonstrate the effectiveness of the algorithm as we can easily verify based on the real results how accurate it was.'),
            html.P('The first Regression technique we tested was called Linear Regression, this is a very simple algorithm that attempts to find any linear correlation between parameters and the goal. From our Testing of this Algorithm we saw it predict the winner of each race in 2020 around 46% of the time. We decided to use this as our baseline to help us test other algorithms in order to improve our results. The Algorithm we settled on was a Random Forest Regressor. This algorithm works in a similar way to Linear Regression but on a much larger scale. The Random Forest assesses parameters based on MSE or Median Standard Error. It will then try different parameters and weights and will construct this into a tree. The algorithm will then do this many times and branch off up to 30 times to assess different variations of the parent tree. This will Construct what is called a forest of decision trees which is where the algorithm gets its name. At the end, it will then get the MSE of each of the trees and use that to output a final prediction. This Algorithm was suited to our varied data set much more than Linear Regression. In our testing, our prediction results for the winner of each grand prix went improved from our baseline of 46% to 70%. Below you will see a graph showing the Feature Importance that the Algorithm decided on.'),
            ],id='Intro', style={ 
                                'margin-top':'3%',
                                'margin-bottom':'1%',
                                'margin-left':'3%', 
                                'margin-right':'3%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),

    html.Div([
        html.Div([
        dcc.Graph(
            id='example-graph', figure=gs.get_FeatureImportance(), 
                    style={'height':'1000px', 'width':'100%', 
                                'display':'inline-block',
                                'margin-top':'3%',
                                'margin-bottom':'3%',
                                'float':'centre',
                                'border-radius': '10px',
                                'border-top':'solid 10px' + data[name]["background-color"],
                                'border-left':'solid 10px' + data[name]["background-color"],
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ],style={
                                'margin-top':'1%',
                                'margin-left':'1%',
                                'margin-right':'1%',
                                'margin-bottom':'0%',
                                }),],
    ),

    html.Div([
        html.Div([
            html.H3('What This Tells Us'),
            html.P('As you can see on the graph some parameters carry much more weight than others with the biggest ones being Pos (Starting Position), Driver Points and the Driver themselves. This all makes sense and it produces decent results as is. Future focus for us to improve the model would be to modify the algorithm, engineer the data or find a new algorithm that may factor in other parameters with more weight. For now anyway you can go to the next page in order to see the models results for each race of the previous season.'),
            ],id='Intro', style={ 
                                'margin-top':'10px',
                                'margin-bottom':'1%',
                                'margin-left':'3%', 
                                'margin-right':'3%', 
                                'display':'inline-block',
                                'border-radius': '10px',
                                'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),

], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%', 'font-size':'25px','background-color': '#cccccc'}),

if __name__ == '__main__':
    app.run_server(debug=True)