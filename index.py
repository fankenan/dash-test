import dash_core_components as dcc
import dash_html_components as html
# import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output

from app import app 
from apps import index_in
from gx import index_gx

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return index_in.layout
    elif pathname == '/gx':
        return index_gx.layout
    else:
        return '404'


app.run_server(debug=True)