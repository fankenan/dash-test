import  dash_table
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Output,Input
import pandas as pd 
# import gx
from app import app 


cj = pd.read_excel('../data/wk.xlsx')
# cj = cj['id'].astype('object')
def gx_table():
    # cj = pd.read_excel('./data/testdata.xlsx')
    return html.Div([],id='table',className='shadow')

@app.callback(Output('table','children'),Input('my-input', 'value'))
def updata(value):
    if value:
        df = cj[cj['身份证号']==int(value)]
        df = df[['考试名称','姓名','语文分数','数学分数','英语分数','政治分数','历史分数','地理分数','总分分数','总分市名']]
        return html.Div(
                dash_table.DataTable(
                        data=df.to_dict('records'),
                        page_size=10,
                        columns=[{"name": i, "id": i} for i in df.columns],
                        style_cell = {'textAlign': 'center'}, 
                        style_cell_conditional=[
                            {
                                'if': {'column_id': 'Region'},
                                'textAlign': 'center'
                            }
                        ]
                    )
        )
    else:
        return html.H3('请输入学生身份证号！')