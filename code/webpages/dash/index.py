from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import dash
import time
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from formulaml_dash import app
from template import verstappen, albon, ricciardo, ocon, stroll, perez, russell, latifi, magnussen, grosjean, norris, sainz, leclerc, vettel, bottas, hamilton, raikkonen, giovinazzi, gasly, kvyat



app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

@app.callback(Output('page-content','children', ),
              Input('url', 'pathname', ))
def display_page(pathname):
    time.sleep(1)
    if pathname == '/driver/verstappen':
        return verstappen.layout
    elif pathname == '/driver/albon':
        return albon.layout
    elif pathname == '/driver/ricciardo':
        return ricciardo.layout
    elif pathname == '/driver/ocon':
        return ocon.layout
    elif pathname == '/driver/stroll':
        return stroll.layout
    elif pathname == '/driver/perez':
        return perez.layout
    elif pathname == '/driver/russell':
        return russell.layout
    elif pathname == '/driver/latifi':
        return latifi.layout
    elif pathname == '/driver/magnussen':
        return magnussen.layout
    elif pathname == '/driver/grosjean':
        return grosjean.layout
    elif pathname == '/driver/norris':
        return norris.layout
    elif pathname == '/driver/sainz':
        return sainz.layout
    elif pathname == '/driver/leclerc':
        return leclerc.layout
    elif pathname == '/driver/vettel':
        return vettel.layout
    elif pathname == '/driver/bottas':
        return bottas.layout
    elif pathname == '/driver/hamilton':
        return hamilton.layout
    elif pathname == '/driver/raikkonen':
        return raikkonen.layout
    elif pathname == '/driver/giovinazzi':
        return giovinazzi.layout
    elif pathname == '/driver/gasly':
        return gasly.layout
    elif pathname == '/driver/kvyat':
        return kvyat.layout
    else:
        return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)