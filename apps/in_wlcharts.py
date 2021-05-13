from app import app
# import dash_html_components as html 
from dash.dependencies import Input, Output
import dash_core_components as dcc
# import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
# from apps import in_sildebar


st_data = pd.read_excel('./st_data.xlsx')

def in_wlcharts_qs():
    return dcc.Graph(id = 'qs_wlcharts')

@app.callback(
    Output('qs_wlcharts', 'figure'), 
    Input('ksmc','value' ))
def updata_qs(ksmc):
    files_path = st_data[st_data['考试名称'].isin([ksmc])]
    # print(st_data,files_path, files_path.iloc[0, 2])
    sx_qs_yb = pd.read_excel(files_path.iloc[0, 2] + '.xlsx')
    sx_qs_eb = pd.read_excel(files_path.iloc[0, 3] + '.xlsx')
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Bar(x=sx_qs_yb['学校'], y=sx_qs_yb['上线人数'] , name='一本上线人数'), row=1, col=1)
    fig.add_trace(go.Scatter(x=sx_qs_yb['学校'], y=sx_qs_yb['上线率'], name='一本上线率'), row=1, col=1)
    fig.add_trace(go.Bar(x=sx_qs_eb['学校'], y=sx_qs_eb['上线人数'], name='二本上线人数'), row=1, col=2)
    fig.add_trace(go.Scatter(x=sx_qs_eb['学校'], y=sx_qs_eb['上线率'], name='一本上线率'), row=1, col=2)
    fig.update_layout(title_text='全市上线情况')
    return fig


def in_wlcharts_yb():
    return dcc.Graph(id = 'yb_wlcharts')

@app.callback(
    Output('yb_wlcharts', 'figure'), 
    Input('ksmc','value' ))
def updata_yb(ksmc):
    files_path = st_data[st_data['考试名称'].isin([ksmc])]
    yb_xx_sx_l = pd.read_excel(files_path.iloc[0, 4] + '.xlsx')
    yb_xx_sx_w = pd.read_excel(files_path.iloc[0, 6] + '.xlsx')
    fig = make_subplots(rows=1, cols=2, )
    fig.add_trace(go.Bar(x=yb_xx_sx_l['学校'], y=yb_xx_sx_l['总分上线'], name='理科一本上线数'), row=1, col=1,)
    fig.add_trace(go.Scatter(x=yb_xx_sx_l['学校'], y=yb_xx_sx_l['上线率'], name='理科一本上线率'), row=1, col=1,)
    fig.add_trace(go.Bar(x=yb_xx_sx_w['学校'], y=yb_xx_sx_w['总分上线'], name='文科一本上线数'), row=1, col=2,)
    fig.add_trace(go.Scatter(x=yb_xx_sx_w['学校'], y=yb_xx_sx_w['上线率'], name='文科一本上线率'), row=1, col=2,)
    fig.update_layout(title_text='各学校一本上线情况')
    return fig



def in_wlcharts_eb():
    return dcc.Graph(id = 'eb_wlcharts')

@app.callback(
    Output('eb_wlcharts','figure'), 
    Input('ksmc','value'))
def updata_eb(ksmc):
    files_path = st_data[st_data['考试名称'].isin([ksmc])]
    eb_xx_sx_l = pd.read_excel(files_path.iloc[0, 5] + '.xlsx')
    eb_xx_sx_w = pd.read_excel(files_path.iloc[0, 7] + '.xlsx')
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Bar(x=eb_xx_sx_l['学校'], y=eb_xx_sx_l['总分上线'], name='理科二本上线数'), row=1, col=1,)
    fig.add_trace(go.Scatter(x=eb_xx_sx_l['学校'], y=eb_xx_sx_l['上线率'], name='理科二本上线率'), row=1, col=1,)
    fig.add_trace(go.Bar(x=eb_xx_sx_w['学校'], y=eb_xx_sx_w['总分上线'], name='文科二本上线数'), row=1, col=2,)
    fig.add_trace(go.Scatter(x=eb_xx_sx_w['学校'], y=eb_xx_sx_w['上线率'], name='文科一本上线率'), row=1, col=2,)
    fig.update_layout(title_text='各学校二本上线情况')
    return fig
