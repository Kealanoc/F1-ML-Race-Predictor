import dash, dash_table
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
from collections import OrderedDict

data=dj()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

teamlist = ["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"]

championship = pd.DataFrame(OrderedDict([
    ("pos", ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]),
    ("driver", ["Lewis Hamilton","Valtteri Bottas","Max Verstappen","Sergio Perez","Daniel Ricciardo","Carlos Sainz Jr.","Alexander Albon","Charles Leclerc","Lando Norris","Pierre Gasly","Lance Stroll","Esteban Ocon","Sebastian Vettel","Daniil Kvyat","Nico Hulkenberg","Kimi Raikkonen","Antonio Giovinazzi","George Russell","Romain Grosjean","Kevin Magnussen","Nicolas Latifi","Jack Aitken","Pietro Fittipaldi"]),
    ("team", ["Mercedes AMG-Petronas","Mercedes AMG-Petronas","Red Bull Racing","BWT Racing Point","Renault Sport F1","McLaren F1","Red Bull Racing","Scuderia Ferrari","McLaren F1","AlphaTauri-Honda","BWT Racing Point","Renault Sport F1","Scuderia Ferrari","AlphaTauri-Honda","BWT Racing Point","Alfa Romeo Racing","Alfa Romeo Racing","Williams Racing","Haas F1","Haas F1","Williams Racing","Williams Racing","Haas F1"]),
    ("wins", ["11", "2", "2", "1", "0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0"]),
    ("poles", ["10", "5", "1", "0","0","0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0"]),
    ("podiums", ["14", "11", "11", "2", "2", "1", "2", "2","1","1","2","1","1","0","0","0","0","0","0","0","0","0","0",]),
    ("points", ["347", "223", "214", "125", "119", "105", "105", "98", "97", "75", "75", "62", "33", "32","10", "4", "4", "3", "2", "1", "0","0","0"]),
]))

constructors = pd.DataFrame(OrderedDict([
    ("pos", ["1","2","3","4","5","6","7","8","9","10"]),
    ("team", ["Mercedes AMG-Petronas", "Red Bull Racing", "McLaren F1 Team", "BWT Racing Point", "Renault Sport F1", "Scuderia Ferrari", "AlphaTauri Honda", "Alfa Romeo Racing", "Haas F1 Team", "Williams Racing"]),
    ("wins", ["13", "2", "0", "1", "0", "0", "1", "0", "0", "0"]),
    ("poles", ["15", "1", "0", "1", "0", "0", "0", "0", "0", "0"]),
    ("podiums", ["23", "13", "2", "4", "3", "2", "1", "0", "0", "0"]),
    ("points", ["573", "319", "202", "195", "181", "131", "107", "8", "3", "0"]),
]))

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
    html.Div([
        html.Img(src="../static/assets/season/hamiltonTurkey.jpg", alt="Lewis Hamilton Celebrates his 7th world title", style={"height":"110%",
                                                                                                                                "float":"right",
                                                                                                                                "position": "relative",
                                                                                                                                "margin-right":"2%",
                                                                                                                                "margin-bottom":"1%"}),
        html.Img(src="../static/assets/season/gasly_win.jpg", alt="Lewis Hamilton Celebrates his 7th world title", style={"height":"110%",
                                                                                                                                "float":"left",
                                                                                                                                "position": "relative",
                                                                                                                                "margin-left":"2%",
                                                                                                                                "margin-bottom":"1%"}),                                                                                                                        
        html.H1("2020 Formula 1 Championship"),
        html.H2("Drivers Champion: Lewis Hamilton[7]"),
        html.H2("Constructors Champion: Mercedes AMG-Petronas[7]"),
    ],id="header", style={"text-align":"center",
                            "padding-top":"3%",
                            "padding-bottom":"3%",
                            "height":"300px",
                            "font-size":"30px",
                            "background-color":"#E10600"}),
    html.Div([
        html.Div([
            html.H3("Story of the season"),
            html.P("The 2020 season was simultaneously one of the most entertaining but predictable seasons in Formula 1 history. The season was originally organised to have 22 races, the most in a single F1 season and was due to begin in Melbourne, the annual season opener. However, due to the COVID-19 pandemic that gripped the world, the season wouldn't get underway until July. Despite being a shortened season and some tracks being forced to host multiple races, there was no loss of drama or of spectacular entertainment."),
            html.P("The season eventually kicked off in Austria to empty stands, with back to back races around the Red Bull Ring. The first race of the year was a race of attrition and saw 9 cars fail to finish along with the drama of a crash between Hamilton and Albon, allowing young Lando Norris to swoop in and take his first F1 podium. The Styrian Grand Prix didnt have the same kind of enthralling action with cars dropping out left and right however it did resume the controversy between Leclerc and Vettel after they had a lap 1 turn 3 collision."),
            html.P("The next races were in Hungary and then another back to back, at Silverstone in the UK. Hungary started with a wet track that saw Verstappen hit the wall before the race had even started, the Red Bull mechanics sorted out all the issues in time for him to start the race. During the week prior to the British Grand Prix it was revealed Sergio Perez had contracted COVID-19, Nico Hulkenberg who had been unable to find a seat for the season filled in for his old teammate. The race will be remembered however for the ending. Hamilton finished the race on 3 wheels after suffering a puncture on the final lap, after the same having happened to Bottas and Sainz just in the minutes before. Verstappen had made a precautionary pitstop and when the puncture happened was 30 seconds behind, he finished the race in second, 5 seconds behind Hamilton"),
            html.P("Next was the '70th Anniversary Grand Prix', the second race at Britain. This race saw Verstappen win and take the first non-Mercedes win of the season. After the previous week's disappointment of Hulkenberg being unable to start his substitute driver appearence for Racing Point, this week he filled in again and got to race, finishing in P7 after qualifying 3rd but starting from the back of the grid. Following this was the Spanish Grand Prix, Hamilton took pole position and the race win to continue his domination of the season thus far."),
            html.P("Hamilton made it back to back wins at an emotional Belgian Grand Prix, the anniversary of the death of young Anthoine Hubert created an emotional atmosphere but didn't stop any of the drivers from producing their best. At the following Italian Grand Prix we saw some very surprising developments. With the race seeming like it would be another Mercedes domination the weekend took some very surprising turns. After Magnussen suffered an engine failure on the start finish straight he retired next to the pit lane entry, causing the pitlane to be closed. Hamilton entered the pitlane during this period and received a 10 second time penalty. Leclerc hit the wall hard after the restard leading to a red flag and with Verstappen out due to a faulty power unit, and Bottas lacking pace, the fight for the win was between Stroll, Sainz and Gasly. Stroll fell away from the top two quickly after having issues, and after a multiple lap long battle Pierre Gasly beat Carlos Sainz and took his first F1 race win."),
            html.P("Next up was the inaugural Tuscan Grand Prix at Mugello, this race saw a typical Mercedes-Hamilton domination, however it also saw a shocking incident. After a first lap collision saw multiple drivers retire, the restart saw an issue with the concertina effect. Not all drivers were on the same page and when some thought they were going, the pack ahead slowed and caused a major multi-car crash in which everyone was lucky to be okay. After Tuscany was the Russian Grand Prix, Hamilton took pole but after two separate 5 second penalties for doing practise starts outside the designated area for doing them. Bottas won with Verstappen finishing 3rd. At the following inaugural Eifel Grand Prix Hamilton took the win after a stiff first corner challenge from Bottas, Daniel Ricciardo also manged to get his first podium with Renault. Kimi broke the record for most races at the Eifel Grand Prix and at the following Portuguese Grand Prix Hamilton took the record for most F1 wins at 92."),
            html.P("As we got to the last five races of the season Mercedes were in position to take their 7th consecutive Constructors World Championship and thats what they did at the Emilia Romagna Grand Prix at Imola. This race was also notable due to Ricciardo getting a second Renault podium and George Russel crashing out under safety car to blow his best opportunity of getting points in F1 thus far. The next race in Turkey was very memorable. Hamilton won the race and won his 7th Driver's World Championship, Sergio Perez also found himself on the podium after a strong drive, and Sebastian Vettel overtook teammate Leclerc at the last corner to take his first podium of the season and his last at Ferrari."),
            html.P("The next race at Bahrain will infamously live in the memory of all F1 fans. At the beginning of the race Romain Grosjean made contact with Daniil Kvyat, which sent him heading straight towards the barriers, his car broke through and was broken in half immediately bursting into flames. Thanks to the many safety measures in place Grosjean survived the crash with burns to his hands and ankles. On the restart Lance Stroll was flipped after making contact with Kvyat. For the next race, also at Bahrain, Hamilton was ruled out due to contracting COVID-19, allowing George Russell to fill in. Russell was not far away from pole position and looked on for a dominant race win until his substitute Jack Aitken crashed at the last corner. Mercedes made a huge mistake in the pit stop he took, giving him the wrong tires, after having to immediately stop again he seemed to make up for the team's mistake but was once again stopped from winning due to a puncture, he finished in 9th with the fastest lap still achieving his first F1 points. The race also saw Sergio Perez take his first F1 race victory."),
            html.P("The last race of the season saw Hamilton return from his illness, Verstappen and Red Bull were on top form however taking pole position, and the race win. This race marked the end of 6 years at Ferrari for Vettel, and 7 for Sergio Perez at Racing Point/Force India. Kevin Magnussen also had what seemes to be his last ever F1 race after 7 years in the sport."),
        ], id="content", style={"margin-top":"1%",
                                "text-align":"center",
                                "float":"right",
                                "margin-right":"3%",
                                "width":"45%",
                                "font-size":"20px"}),
        
        html.Div([
            dash_table.DataTable(
                id="table",
                data=championship.to_dict('records'),
                columns=[{
                    'id':'pos',
                    'name':'Pos',
                    'type':'numeric'
                },{
                    'id':'driver',
                    'name':'Driver',
                    'type':'text'
                },{
                    'id':'team',
                    'name':'Team',
                    'type':'text'
                },{
                    'id':'wins',
                    'name':'Wins',
                    'type':'numeric'
                },{
                    'id':'poles',
                    'name':'Poles',
                    'type':'numeric'
                },{
                    'id':'podiums',
                    'name':'Podiums',
                    'type':'numeric'
                },{
                    'id':'points',
                    'name':'Pts',
                    'type':'numeric'
                }],
                style_table={'height': 'auto'},
                style_cell={'height': 'auto',
                            'fontSize':'20px',
                            'text-align':'left',
                            'font-family':'Yu Gothic UI'},
                style_cell_conditional=[
                                    {'if': {'column_id': 'podiums'},
                                        'width': '7%'}],
                style_header={'backgroundColor': 'rgb(230, 230, 230)',
                                'fontWeight': 'bold'}
            )
        ], style={"width":"45%",
                    "float":"left",
                    'margin-left':'3%',
                    'margin-top':'1%',
                    'padding-top':'0.5%'}),
    ], style = {}),
    html.Div([
        html.Div([
            dcc.Graph(
                id='example-graph', figure=gs.get_FullSeasonChampionship(teamlist), style={'height':'20%', 'width':'45%', 
                                        'display':'inline-block',
                                        'margin-left': '3%', 
                                        'margin-right':'2%',
                                        'margin-top':'3%',
                                        'border-radius': '10px',
                                        'border-top':'solid 10px' + "#E10600",
                                        'border-left':'solid 10px' + "#E10600",
                                        'border-bottom':'solid 10px' + "#E10600"}),
        ])
    ]),
    html.Div([
        html.Img(src="../static/assets/season/crash.jpg", alt="Lewis Hamilton Celebrates his 7th world title", style={"width":"45%",
                                                                                                                                "float":"left",
                                                                                                                                "margin-left":"3%",
                                                                                                                                "margin-top":"3%",
                                                                                                                                "margin-bottom":"1%"}),
    ]),
        html.Div([
            dash_table.DataTable(
                id="table2",
                data=constructors.to_dict('records'),
                columns=[{
                    'id':'pos',
                    'name':'Pos',
                    'type':'numeric'
                },{
                    'id':'team',
                    'name':'Team',
                    'type':'text'
                },{
                    'id':'wins',
                    'name':'Wins',
                    'type':'numeric'
                },{
                    'id':'poles',
                    'name':'Poles',
                    'type':'numeric'
                },{
                    'id':'podiums',
                    'name':'Podiums',
                    'type':'numeric'
                },{
                    'id':'points',
                    'name':'Pts',
                    'type':'numeric'
                }],
                style_table={'height': 'auto'},
                style_cell={'height': 'auto',
                            'fontSize':'20px',
                            'text-align':'left',
                            'font-family':'Yu Gothic UI'},
                style_cell_conditional=[
                                    {'if': {'column_id': 'podiums'},
                                        'width': '7%'}],
                style_header={'backgroundColor': 'rgb(230, 230, 230)',
                                'fontWeight': 'bold'}
            )
        ], style={"width":"45%",
                    "float":"left",
                    'margin-left':'3%',
                    'margin-top':'3%'}),
    ], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%', 'font-size':'25px','background-color': 'white',}),

if __name__ == '__main__':
    app.run_server(debug=True)
