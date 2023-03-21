import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import pandas as pd
import numpy as np
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_daq as daq

df = pd.read_excel('week_keyword_table_s01_2021.xlsx',index_col=0)
fig = px.scatter(df, x='lasercut', y='lasercut',
                color='lasercut', hover_name='lasercut',
                 log_x=True, size_max=60)

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("TLTL Lab Link💡", href="https://tltlab.org/")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu📚",
            children=[
                dbc.DropdownMenuItem("homepage"),
                dbc.DropdownMenuItem("analysis"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("conclusion"),
            ],
        ),
    ],
    brand="Keyword Matrix📝",
    brand_href="#",
    sticky="top",
className="navbar navbar-expand-sm bg-dark .text-white navbar-dark sticky-top" ,
)
# Individual Weekly Graph
div1 = html.Div([html.Iframe(src=app.get_asset_url("s1_aggregate_network1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div2 = html.Div([html.Iframe(src=app.get_asset_url("s2_weekly_network1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div3 = html.Div([html.Iframe(src=app.get_asset_url("s3_weekly_network1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})

content = html.Div(id="page-content")
initial_html = open("/Users/chenyimin/PycharmProjects/knowledge_map/index.html", 'r').read()
with open('s2_weekly_network1.html', 'r') as f:
    second_html = f.read()

with open('s3_weekly_network1.html', 'r') as f:
    third_html = f.read()
# Individual Aggregate Graph
div4 = html.Div([html.Iframe(src=app.get_asset_url("s1_aggregate_network1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div5 = html.Div([html.Iframe(src=app.get_asset_url("s2_aggregate_network1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div6 = html.Div([html.Iframe(src=app.get_asset_url("s3_aggregate_network1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
content = html.Div(id="page-content")
# Define the initial HTML content to display in the Iframe component
initial_html_aggregate = open('s1_aggregate_network1.html', 'r').read()

with open('s2_aggregate_network1.html', 'r') as f:
    second_html_aggregate = f.read()

with open('s3_aggregate_network1.html', 'r') as f:
    third_html_aggregate = f.read()

# Define the Sidebar
sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Find yourself here!',
                        style={'margin-top': '12px', 'margin-left': '24px'})
            ],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [
                html.Div([html.Hr(),
                          html.P('Find your name to see individual weekly keywords',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='mydropdown', options=[{'label': 'student 1', 'value': 'optionA'},
                                                                    {'label': 'student 2', 'value': 'optionB'},
                                                                    {'label': 'student 3', 'value': 'optionC'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),

                          html.P('Find your name to see your individual aggregated keywords in 4 weeks',
                                 style={'margin-top': '16px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='mydropdown2', options=[{'label': 'student 1', 'value': 'optionA'},
                                                                    {'label': 'student 2', 'value': 'optionB'},
                                                                    {'label': 'student 3', 'value': 'optionC'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),

                          html.P('See keywords of the whole class in 4 weeks',
                                 style={'margin-top': '16px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='my-dropdown-3', options=[{'label': 'week 1', 'value': 'option a'},
                                                                    {'label': 'week 2', 'value': 'option b'},
                                                                    {'label': 'week 3', 'value': 'option c'},
                                                                    {'label': 'week 4', 'value': 'option d'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),
                          #html.Button(id='my-button', n_clicks=0, children='apply',
                                      #style={'margin-top': '16px'},
                                      #className='bg-dark text-white'),
                          html.Hr()
                          ])
            ],
            style={'height': '10vh', 'margin': '8px', 'display': 'flex'}), #html.Hr(),

        #dbc.Row(
            #[
                #html.P('Brief instruction: xxxxxx', className='bg-dark text-white')
           # ],
           # style={"height": "45vh", 'margin': '8px', 'display': 'flex'}
       # ),
        #html.Div(id='my-output')
    ]
)

# Define the App Layout
app.layout = html.Div(
    [dbc.Container(
        [dbc.Row(dbc.Col(navbar, width=30)),
         html.Hr(),
         dbc.Row(
             [
                 dbc.Col(sidebar, width=3, className='bg-dark'),
                 # dbc.Col(content, width=9)
                 dbc.Col(
                     [
                         html.P('individual weekly keywords', className='font-weight-bold'),
                         html.Iframe(id='html-iframe', srcDoc=initial_html, width='95%', height='600',
                                     style={'height': '45vh'}),

                         dbc.Row([dbc.Col([html.Div([
                             # html.Label('Select a week:', style={'fontSize': '20px'}),
                             dcc.Slider(
                                 id='myslider',
                                 min=0,
                                 max=2,
                                 value=1,
                                 step=1,
                                 updatemode='drag',
                                 marks={0: 'Week1', 1: 'Week2', 2: 'Week3'}
                             ),
                         ], style={'width': '85%', 'margin': '30px', 'margin-top': '20px',
                                   'color': '#000000',
                                   'fontSize': '10px',
                                   'padding': '5px'})
                         ])]),

                     ]),

                 dbc.Col(
                     [
                         html.P('individual aggregated keywords', className='font-weight-bold'),
                         html.Iframe(id='html-iframe-2', srcDoc=initial_html_aggregate, width='95%', height='600',
                                     style={'height': '45vh'}),

                         dbc.Row([dbc.Col([html.Div([
                             # html.Label('Select a week:', style={'fontSize': '20px'}),
                             dcc.Slider(
                                 id='myslider2',
                                 min=0,
                                 max=2,
                                 value=1,
                                 step=1,
                                 updatemode='drag',
                                 marks={0: 'Week1', 1: 'Week2', 2: 'Week3'}
                             )
                         ], style={'width': '85%', 'margin': '30px', 'margin-top': '20px',
                                   'color': '#000000',
                                   'fontSize': '10px',
                                   'padding': '5px'})
                         ])])

                     ])
             ], style={"height": "50vh"}
         ),

         dbc.Row(
             [
                 dbc.Col(
                     [ html.Hr(),
                         html.P('keywords of the whole class'),
                                         html.Div([
                                             dcc.Graph(id='keywords', figure=fig)
                                         ]), #md=10,

                     ])
             ],
             style={"height": "50vh", 'margin': '8px'}
         )
         ],
        fluid=True
    )
    ])

# dbc.Row(
#         [
#            dbc.Col(
#               [
#                  html.P('keywords of the whole class'),
#             html.Div([
#                dcc.Graph(id='keywords', figure=fig)
#           ]), #md=10,
#
#                   ])
#          ],
#         style={"height": "50vh", 'margin': '8px'}
#  )
# Define the callback function for Individual Weekly Graph
@app.callback(
    Output('html-iframe', 'srcDoc'),
    [Input('mydropdown', 'value'),
     Input('myslider', 'value') ]
    #[Input('my-dropdown', 'value'),Input('my-slider', 'value')]
)
def update_output(mydropdown,myslider):
    # Define the HTML content to display based on the dropdown menu
    if mydropdown== 'optionA' and myslider == 0 :
        return open('s1_weekly_network1.html', 'r').read()
    elif mydropdown== 'optionA' and myslider == 1 :
        return open('s1_weekly_network2.html', 'r').read()
    elif mydropdown== 'optionA' and myslider == 2 :
        return open('s1_weekly_network2.html', 'r').read()
    elif mydropdown == 'optionB' and myslider == 0:
        return open('s2_weekly_network1.html', 'r').read()
    elif mydropdown== 'optionB' and myslider == 1 :
        return open('s2_weekly_network2.html', 'r').read()
    elif mydropdown== 'optionB' and myslider == 2 :
        return open('s2_weekly_network3.html', 'r').read()
    elif mydropdown == 'optionC' and myslider == 0:
        return open('s3_weekly_network1.html', 'r').read()
    elif mydropdown == 'optionC' and myslider == 1:
        return open('s3_weekly_network2.html', 'r').read()
    elif mydropdown == 'optionC' and myslider == 2:
        return open('s3_weekly_network3.html', 'r').read()






#def update_output(value):
    # Define the HTML content to display based on the dropdown menu
    #if value == 'option1':
        #return open('s1_aggregate_network1.html', 'r').read()
    #elif value == 'option2':
        #return open('s2_weekly_network1.html', 'r').read()
    #elif value == 'option3':
        #return open('s3_weekly_network1.html', 'r').read()




# Define the callback function for Individual Aggregate Graph
@app.callback(
    Output('html-iframe-2', 'srcDoc'),
    [Input('mydropdown2', 'value'),
     Input('myslider2', 'value')]
)
def update_output(mydropdown2,myslider2):
    # Define the HTML content to display based on the dropdown menu
    if mydropdown2== 'optionA' and myslider2 == 0 :
        return open('s1_aggregate_network1.html', 'r').read()
    elif mydropdown2== 'optionA' and myslider2 == 1 :
        return open('s1_aggregate_network2.html', 'r').read()
    elif mydropdown2 == 'optionA' and myslider2 == 2:
        return open('s1_aggregate_network3.html', 'r').read()
    elif mydropdown2 == 'optionB' and myslider2 == 0:
        return open('s2_aggregate_network1.html', 'r').read()
    elif mydropdown2 == 'optionB' and myslider2 == 1:
        return open('s2_aggregate_network2.html', 'r').read()
    elif mydropdown2 == 'optionB' and myslider2 == 2:
        return open('s2_aggregate_network3.html', 'r').read()
    elif mydropdown2 == 'optionC' and myslider2 == 0:
        return open('s3_aggregate_network1.html', 'r').read()
    elif mydropdown2 == 'optionC' and myslider2 == 1:
        return open('s3_aggregate_network2.html', 'r').read()
    elif mydropdown2 == 'optionC' and myslider2 == 2:
        return open('s3_aggregate_network3.html', 'r').read()
if __name__ == "__main__":
    app.run_server(debug=True, port=8078)