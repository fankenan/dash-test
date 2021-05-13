# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
# from dash.dependencies import Input, Output

# from app import app 
from apps import in_sildebar
from apps import in_sumchart
from apps import in_wlcharts

layout = html.Div([
                dbc.Row([
                    # dbc.Col(width=1),
                    dbc.Col([in_sildebar.in_sildebar()],width=2,className='bg-dark vh-100'),
                    dbc.Col([in_sumchart.sumchart_yb(), in_sumchart.sumchart_eb(),in_wlcharts.in_wlcharts_qs(), in_wlcharts.in_wlcharts_yb(), in_wlcharts.in_wlcharts_eb()],width=9,className='vh-100'),
                    # dbc.Col(width=1)
                    ]
                )
            ],className ='vh-100 w-100 p-3')






# app.run_server(debug=True)