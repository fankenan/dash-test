import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc  
# from app import app
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


def sumchart_yb():
    qsyb_sum = pd.read_excel('../data/qsyb_sum.xlsx')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(qsyb_sum['考试名称']), y=list(qsyb_sum['登封一中']), mode='lines+markers', name='登封一中')),
    fig.add_trace(go.Scatter(x=list(qsyb_sum['考试名称']), y=list(qsyb_sum['实验高中']), mode='lines+markers', name='实验高中')),
    fig.add_trace(go.Scatter(x=list(qsyb_sum['考试名称']), y=list(qsyb_sum['嵩阳高中']), mode='lines+markers', name='嵩阳高中')),
    fig.add_trace(go.Scatter(x=list(qsyb_sum['考试名称']), y=list(qsyb_sum['外国语高中']), mode='lines+markers', name='外国语高中')),
    # fig.add_trace(go.Scatter(x=list(qsyb_sum['考试名称']), y=list(qsyb_sum['少林中学']), mode='lines+markers', name='少林中学')),
    fig.update_layout(title='历次考试一本上线情况')
    return html.Div(dcc.Graph(figure=fig))

def sumchart_eb():
    qseb_sum = pd.read_excel('../data/qseb_sum.xlsx')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(qseb_sum['考试名称']), y=list(qseb_sum['登封一中']), mode='lines+markers', name='登封一中')),
    fig.add_trace(go.Scatter(x=list(qseb_sum['考试名称']), y=list(qseb_sum['实验高中']), mode='lines+markers', name='实验高中')),
    fig.add_trace(go.Scatter(x=list(qseb_sum['考试名称']), y=list(qseb_sum['嵩阳高中']), mode='lines+markers', name='嵩阳高中')),
    fig.add_trace(go.Scatter(x=list(qseb_sum['考试名称']), y=list(qseb_sum['外国语高中']), mode='lines+markers', name='外国语高中')),
    # fig.add_trace(go.Scatter(x=list(qseb_sum['考试名称']), y=list(qseb_sum['少林中学']), mode='lines+markers', name='少林中学')),
    fig.update_layout(title='历次考试二本上线情况')
    return html.Div(dcc.Graph(figure=fig))