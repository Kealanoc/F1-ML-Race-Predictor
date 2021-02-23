from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from formulaml_dash import app
from template import driver


app.layout = html.Div([

    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'max_verstappen',),
              Input('url', 'pathname',))
def display_page(pathname):
    if pathname == '/max_verstappen':
        return driver.layout
    elif pathname == '/ricciardo':
        return driver.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)