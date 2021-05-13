from app import app 
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
import plotly.express as px 
import plotly.graph_objects as go



cj = pd.read_excel('../data/wk.xlsx')
# cj = cj['id'].astype('object')

def gx_sildbar():
    return  html.Div([
                html.H6("请输入学生识别号"),
                html.Div([dcc.Input(id='my-input', value = '20',type='number',className='shadow')]),
                html.Br(),
                html.Div(id='my-output'),

            ],className='text-white d-flex flex-column align-items-center pt-4')


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    # return input_value
    # return print(input_value,type(input_value))
    stu_name = cj[cj['身份证号'].isin([int(input_value)])]['姓名'].drop_duplicates()
    # return print(stu_name)

    name = list(stu_name)
    name = str(name)[2:-2]
    
    if name:
        # return name
        return '您查找的学生姓名为： {}'.format(name)
    else: return '请输入正确的身份证号！'

# def gx_table_sum():
#     return html.Div(
#         dash_table.DataTable(
#             id='sum_table',
            
#         )
#     )

def gx_scatter_sum():
    fig = px.scatter()
    return dcc.Graph(figure=fig, id = 'chart_sum', config= {'displaylogo': False})

@app.callback(
    Output('chart_sum', 'figure'),
    Input('my-input', 'value')
)
def update_gx_scatter_sum(input_value):
    if input_value:
        df = cj[cj['身份证号']==int(input_value)]
        df = df[['考试名称', '总分市名']]
        fig = px.line(df, x='考试名称', y='总分市名',orientation='v', title='名次走势')
        # fig.update_yaxes()
        fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1, autorange="reversed")
        return fig
    else:
        html.Div(html.H3(children='请输入学生身份证号码'))



def gx_radar():
    fig = go.Figure(data=go.Scatterpolar())
    return dcc.Graph(figure = fig, id = 'radar', config = dict({'staticPlot': True, 'displaylogo': False}))

@app.callback(
    Output('radar', 'figure'),
    Input('my-input', 'value'))
def update_radar(input_value):
    if input_value:
        df = cj[cj['身份证号']==int(input_value)]
        # print(df)
        df = df[['语文分数', '数学分数', '英语分数', '政治分数', '历史分数', '地理分数']]
        zf_150 = df.shape[0]  * 15
        zf_100 = df.shape[0] * 10
        # print(zf_100,zf_150)
        yw_sum,sx_sum,yy_sum,zz_sum,ls_sum,dl_sum = int(df['语文分数'].sum()), int(df['数学分数'].sum()), int(df['英语分数'].sum()),int(df['政治分数'].sum()),int(df['历史分数'].sum()),int(df['地理分数'].sum())
        # print(yw_sum/zf_150, sx_sum/zf_150, yy_sum/zf_150, zz_sum/zf_100, ls_sum/zf_100, dl_sum/zf_100)
        if zf_150 == 0:
            r = [yw_sum/1, sx_sum/1, yy_sum/1,zz_sum/1, ls_sum/1, dl_sum/1]
        else: r = [yw_sum/zf_150, sx_sum/zf_150, yy_sum/zf_150,zz_sum/zf_100, ls_sum/zf_100, dl_sum/zf_100]
        fig = go.Figure(data=go.Scatterpolar(
            r = r, 
            theta = ['语文', '数学', '英语', '政治', '历史', '地理'],
            fill='toself', 
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                visible=True
                ),
            ),
            showlegend=False,
            title='学科优势'
        )
        return fig

def gx_pie():
    fig = px.pie()
    return dcc.Graph(figure = fig,id = 'pie', config=dict({'staticPlot': True, 'displaylogo': False}))

@app.callback(
    Output('pie', 'figure'),
    Input('my-input', 'value'))
def update_radar(input_value):
    df = cj[cj['身份证号']==int(input_value)]
    # print(input_value)
    df = df[['语文分数', '数学分数', '英语分数', '政治分数', '历史分数', '地理分数']]
    zf_150 = df.shape[0] * 150
    zf_100 = df.shape[0] * 100
    yw_sum,sx_sum,yy_sum,zz_sum,ls_sum,dl_sum = int(df['语文分数'].sum()), int(df['数学分数'].sum()), int(df['英语分数'].sum()),int(df['政治分数'].sum()),int(df['历史分数'].sum()),int(df['地理分数'].sum())
    s_1= pd.Series(['语文', '数学', '英语', '政治', '历史', '地理'])
    if zf_100 == 0:
        s_2 = pd.Series([1,1,1,1,1,1])
    else: s_2 = pd.Series([yw_sum,sx_sum,yy_sum,zz_sum,ls_sum,dl_sum])
    df_xkzb_s = {'学科':s_1,'分数':s_2}
    df_xkzb = pd.DataFrame(df_xkzb_s)
    fig = px.pie(df_xkzb, values='分数', names='学科', title='学科占比')
    # fig.show(config={'staticPlot': True, 'displaylogo': False})
    return fig