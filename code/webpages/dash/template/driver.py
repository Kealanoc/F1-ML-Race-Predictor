import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from formulaml_dash import app
import plotly.express as px
import pandas as pd

name = "max_verstappen"
df = pd.read_csv("static/Data/DriverStandings.csv")
df = df.drop(["Driver Wins", "Driver Standings"], axis=1)
season = []
points = {}
for i in range(len(df)):
    j = i+1
    if df.Driver[i] == name:
        Season = df.Season[i]
        Points = df.DriverPoints[i]
        points[Season] = Points
df = {'Points': points.values()}
df = pd.DataFrame.from_dict(df, orient='index', columns=points.keys())
fig = px.line(df, x="Season", y="Points")

external_scripts = [
    {'src': 'https://code.jquery.com/jquery-3.2.1.min.js'},
    {'src': 'https://cdn.jsdelivr.net/npm/chart.js@2.8.0'},
    {'src': 'static/GraphScripts/careerPoints.js'},
    {'src': 'static/GraphScripts/DriverPointsThroughoutSeasonLineChart.js'},
    {'src': 'static/GraphScripts/QualiGapTeammateBarChart.js'},
]
app = dash.Dash(external_scripts=external_scripts,external_stylesheets=[dbc.themes.BOOTSTRAP])

awards = ['2014, 15, 16, 19 FIA Action of the Year', '2015, 16, 17 FIA Personality of the Year', '2015 FIA Rookie of the Year', '2016 Lorenzo Bandini Trophy', '2014 FIA European Formula 3 Championship Third Place']
teams = ['2014-2016: Scuderia Toro Rosso', '2016-Present: Red Bull Racing']

layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
), html.Div([
    dcc.Location(id='url', refresh=False),
    #header
    html.Div([
    html.H1('Max Verstappen', 
            style={'text-indent':'100px', 
                    'line-height':'20%', 
                    'clear':'both',
                    'display':'inline-block',
                    'padding-top':'1%'}),
    
    html.Img(src="../../static/assets/flags/netherlands_flag.png", 
            style={'width':'75px',
                    'height':'45px',
                    'display':'inline-block',
                    'clear':'both'}),
    
    html.Img(src="../../static/assets/logos/redbull_logo.png", 
            style={'height':'40%',
                    'float':'right',
                    'padding-top':'6%',
                    'padding-right':'2.5%',
                    'padding-left':'2%'}),
    
    html.Img(src="../../static/assets/portraits/verstappen_photo.png", 
            style={'height':'110%',
                    'padding-left':'2.5%',
                    'padding-top' :'1%',
                    'float':'right',
                    'vertical-align':'top',}),

    html.H2('Red Bull Racing', 
            style={'text-indent':'100px',
                    'vertical-align':'text-top',
                    'line-height':'0%'}),
    #left
    html.Div([
        html.P('Age: 23'),
        html.P('Entries: 119'),
        html.P('Titles: 0'),
        html.P('Poles: 3'),
    ],id='left', style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'10%',
                            'display':'inline-block'}),
    #right
    html.Div([
        html.P('Wins: 10'),
        html.P('Podiums: 42'),
        html.P('First Start: 2015 Australian Grand Prix'),
        html.P('First Win: 2016 Spanish Grand Prix'),
    ],id='right',style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'10%',
                            'display':'inline-block'}),
    ],id='header', style={'background-color':'#223971',
                            'height':'300px', 
                            'padding-top':'10px', 
                            'padding-bottom':'80px', 
                            'position':'relative',
                            'font-size':'30px'}),
    #dcc.Graph(
     # id='example-graph', figure=fig),
    #awards
    html.Div([
        html.H3('Awards Won:'),
        html.Ul(children=[html.Li(i) for i in awards]),
    ],id='awards'),
    #teamHistory
    html.Div([
        html.H3('Team(s) Driven For:'),
        html.Ul(children=[html.Li(i) for i in teams]),
    ],id='teamHistory',),
    ], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%'})

if __name__ == '__main__':
    app.run_server(debug=True)