# from app import app 
import dash_core_components as dcc 
import dash_html_components as html 
# import dash_bootstrap_components as dbc
import pandas as pd

ksmc_list = pd.read_excel('../data/qsyb_sum.xlsx')
ksmc_list = list(ksmc_list['考试名称'])

def in_sildebar():
    return html.Div([
        html.H6('请选择考试名称：',className='pt-5 text-light'),
        dcc.Dropdown(
            id = 'ksmc',
            options=[{'label': item, 'value': item} for item in ksmc_list],
            value = '2021届高三天一一联',
            className = 'font-monospace'
        ),]
    )

