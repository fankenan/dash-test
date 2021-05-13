# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
# from dash.dependencies import Input, Output

# from app import app 
from gx import gx
from gx import table

layout = html.Div(
    dbc.Row([
        # dbc.Col(width=1),
        dbc.Col([gx.gx_sildbar(),],width=2,className='bg-dark vh-100'),
        dbc.Col([gx.gx_scatter_sum(),
                dbc.Row([
                    dbc.Col(gx.gx_radar()), 
                    dbc.Col(gx.gx_pie())]
                ),
                table.gx_table()],
                width=9,className=''),
        ]
    ),className='vh-100 w-100 p-3'
)
    


# app.run_server(debug=True)