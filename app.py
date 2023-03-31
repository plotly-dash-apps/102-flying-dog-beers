import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import pandas as pd
#import numpy as np
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_daq as daq

df = pd.read_csv('assets/week_keyword_table_s01_2021.csv',index_col=0)
#fig = px.scatter(df, x='lasercut', y='lasercut',
                #color='lasercut', hover_name='lasercut',
                 #log_x=True, size_max=60)

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("TLTL Lab Link💡", href="https://tltlab.org/")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu📚",
            children=[
                dbc.DropdownMenuItem("mainpage"),
                #dbc.DropdownMenuItem("analysis"),
                #dbc.DropdownMenuItem(divider=True),
                #dbc.DropdownMenuItem("conclusion"),
            ],
        ),
    ],
    brand="Keyword Matrix📝",
    brand_href="#",
    sticky="top",
className="navbar navbar-expand-sm bg-dark .text-white navbar-dark sticky-top" ,
)
# Individual Weekly Graph
div1 = html.Div([html.Iframe(src=app.get_asset_url("assets/s1_weekly_network1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div2 = html.Div([html.Iframe(src=app.get_asset_url("assets/s2_weekly_network1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div3 = html.Div([html.Iframe(src=app.get_asset_url("assets/s3_weekly_network1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
# Individual Weekly Graph
div1 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_weekly_1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div2 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s2_weekly_1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div3 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s3_weekly_1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div11 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s4_weekly_1.html"), id="graph4")] )
div12 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s5_weekly_1.html"), id="graph5")] )
div13 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s6_weekly_1.html"), id="graph6")] )
div14 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s7_weekly_1.html"), id="graph7")] )
div15 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s1_weekly_1.html"), id="2022_graph1")] )
div16 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s2_weekly_1.html"), id="2022_graph2")] )
div17 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s3_weekly_1.html"), id="2022_graph3")] )
div18 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s4_weekly_1.html"), id="2022_graph4")] )
div19 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s5_weekly_1.html"), id="2022_graph5")] )
div20 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s6_weekly_1.html"), id="2022_graph6")] )
div21 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s7_weekly_1.html"), id="2022_graph7")] )
div22 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s8_weekly_1.html"), id="2022_graph8")] )
div23 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s9_weekly_1.html"), id="2022_graph9")] )
div24 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s10_weekly_1.html"), id="2022_graph10")] )
div25 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s11_weekly_1.html"), id="2022_graph11")] )
div26 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s12_weekly_1.html"), id="2022_graph12")] )
div27 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s1_weekly_1.html"), id="2023_graph1")] )
div28 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s2_weekly_1.html"), id="2023_graph2")] )
div29 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s3_weekly_1.html"), id="2023_graph3")] )
div30 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s4_weekly_1.html"), id="2023_graph4")] )
div31 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s5_weekly_1.html"), id="2023_graph5")] )
div32 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s6_weekly_1.html"), id="2023_graph6")] )
div33 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s7_weekly_1.html"), id="2023_graph7")] )
div34 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s8_weekly_1.html"), id="2023_graph8")] )
div35 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s9_weekly_1.html"), id="2023_graph9")] )
div36 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s10_weekly_1.html"), id="2023_graph10")] )
div37 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s11_weekly_1.html"), id="2023_graph11")] )
div38 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s12_weekly_1.html"), id="2023_graph12")] )

###############################
div39 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div40 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s2_aggregate_1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div41 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s3_aggregate_1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div42 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s4_aggregate_1.html"), id="graph4")] )
div43 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s5_aggregate_1.html"), id="graph5")] )
div44 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s6_aggregate_1.html"), id="graph6")] )
div45 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s7_aggregate_1.html"), id="graph7")] )
div46 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s1_aggregate_1.html"), id="2022_graph1")] )
div47 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s2_aggregate_1.html"), id="2022_graph2")] )
div48 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s3_aggregate_1.html"), id="2022_graph3")] )
div49 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s4_aggregate_1.html"), id="2022_graph4")] )
div50 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s5_aggregate_1.html"), id="2022_graph5")] )
div51 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s6_aggregate_1.html"), id="2022_graph6")] )
div52 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s7_aggregate_1.html"), id="2022_graph7")] )
div53 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s8_aggregate_1.html"), id="2022_graph8")] )
div54 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s9_aggregate_1.html"), id="2022_graph9")] )
div55 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s10_aggregate_1.html"), id="2022_graph10")] )
div56 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s11_aggregate_1.html"), id="2022_graph11")] )
div57 = html.Div([html.Iframe(src=app.get_asset_url("assets/2022_s12_aggregate_1.html"), id="2022_graph12")] )
div58 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s1_aggregate_1.html"), id="2023_graph1")] )
div59 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s2_aggregate_1.html"), id="2023_graph2")] )
div60 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s3_aggregate_1.html"), id="2023_graph3")] )
div61 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s4_aggregate_1.html"), id="2023_graph4")] )
div62 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s5_aggregate_1.html"), id="2023_graph5")] )
div63 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s6_aggregate_1.html"), id="2023_graph6")] )
div64 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s7_aggregate_1.html"), id="2023_graph7")] )
div65 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s8_aggregate_1.html"), id="2023_graph8")] )
div66 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s9_aggregate_1.html"), id="2023_graph9")] )
div67 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s10_aggregate_1.html"), id="2023_graph10")] )
div68 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s11_aggregate_1.html"), id="2023_graph11")] )
div69 = html.Div([html.Iframe(src=app.get_asset_url("assets/2023_s12_aggregate_1.html"), id="2023_graph12")] )
content = html.Div(id="page-content")
initial_html = open("assets/2021_s1_weekly_1.html", 'r').read()
with open('assets/2021_s2_weekly_1.html', 'r') as f:
    second_html = f.read()

with open('assets/2021_s2_weekly_1.html', 'r') as f:
    third_html = f.read()
# Individual Aggregate Graph
div4 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div5 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div6 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
content = html.Div(id="page-content")
# Define the initial HTML content to display in the Iframe component
initial_html_aggregate = open('assets/2021_s1_aggregate_1.html', 'r').read()

with open('assets/2021_s2_aggregate_1.html', 'r') as f:
    second_html_aggregate = f.read()

with open('assets/2021_s3_aggregate_1.html', 'r') as f:
    third_html_aggregate = f.read()

# Class Collective Graph
div7 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_class_1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div8 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_class_1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div9 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_class_1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
content = html.Div(id="page-content")
# Define the initial HTML content to display in the Iframe component
initial_html_class = open('assets/2021_class_1.html', 'r').read()

with open('assets/2022_class_1.html', 'r') as f:
    second_html_class = f.read()

with open('assets/2023_class_1.html', 'r') as f:
    third_html_class = f.read()

# Define the Sidebar
sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Individual knowledge map',
                        style={'margin-top': '12px', 'margin-left': '24px'})
            ],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),

        dbc.Row(
            [
                html.Div([html.Hr(),
                          html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='yeardropdown', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),

                          html.P('Find your name to see your individual weekly keywords',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='mydropdown',  # options=[{'label': 'student 1', 'value': 'optionA'},
                                       #  {'label': 'student 2', 'value': 'optionB'},
                                       # {'label': 'student 3', 'value': 'optionC'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),

                          html.P('Find your name to see your individual aggregated keywords',
                                 style={'margin-top': '16px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='mydropdown2',  # options=[{'label': 'student 1', 'value': 'optionA'},
                                       #      {'label': 'student 2', 'value': 'optionB'},
                                       #     {'label': 'student 3', 'value': 'optionC'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),




                          #html.P('See class collectives map',
                                 #style={'margin-top': '16px', 'margin-bottom': '4px'},
                                 #className='bg-dark text-white'),
                          #dcc.Dropdown(id='mydropdown3', options=[{'label': '2021', 'value': '2021'},
                                                                  #{'label': '2022', 'value': '2022'},
                                                                  #{'label': '2023', 'value': '2023'}
                                                                  #],
                                       #multi=False,
                                       #style={'width': '220px', 'color': '#000000'}
                                       #),
                          # html.Button(id='my-button', n_clicks=0, children='apply',
                           #style={'margin-top': '16px'},
                          #className='bg-dark text-white'),
                          #html.Hr()
                          ])

            ],



            style={'height': '40vh', 'margin': '10px', 'display': 'flex'}),

                          html.Hr(),
                          html.Hr(),
                          html.Hr(),
                          html.Hr(),
                          html.Hr(),
                          html.Hr(),


        dbc.Row(
            [
                html.H5('Collective knowledge map',
                        style={'margin-top': '12px', 'margin-left': '24px'})
            ],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
dbc.Row(
            [
                html.Div([html.Hr(),
                          html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='bg-dark text-white'),
                          dcc.Dropdown(id='yeardropdown1', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),

                          ])
            ],



            style={'height': '40vh', 'margin': '10px', 'display': 'flex'})
        # html.Hr(),

        # dbc.Row(
        # [
        # html.P('Brief instruction: xxxxxx', className='bg-dark text-white')
        # ],
        # style={"height": "45vh", 'margin': '8px', 'display': 'flex'}
        # ),
        # html.Div(id='my-output')
    ],
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
                         html.P('Individual weekly keywords', className='text-center font-weight-bold',style={'fontWeight': 'bold'}),
                         html.Iframe(id='html-iframe', srcDoc=initial_html, width='95%', height='600',
                                     style={'height': '45vh'}),

                         dbc.Row([dbc.Col([html.Div([
                            #html.Label('Select a week:', style={'fontSize': '20px'}),
                             dcc.Slider(
                                 id='myslider',
                                 min=1,
                                 max=10,
                                 value=1,
                                 step=1,
                                 updatemode='drag',
                                 marks={1: {'label': '1'}, 2: {'label': '2' }, 3: '3',4: '4', 5: '5', 6: '6',7: '7', 8: '8', 9: '9',10: '10'},
tooltip={"placement": "bottom", "always_visible": True},included=False
                             ),
                             dbc.Label("Week", className="text-center w-100 mb-0",width='10%'),
                         ], style={'width': '85%', 'margin': '20px', 'margin-top': '20px',
                                   #'color': '#000000',
                                   'fontSize': '15px',
                                   'padding': '5px'})
                         ])]),

                     ],width={"size": 4}),

                 dbc.Col(
                     [
                         html.P('Individual aggregated weekly keywords', className='text-center font-weight-bold',style={'fontWeight': 'bold'}),
                         html.Iframe(id='html-iframe-2', srcDoc=initial_html_aggregate, width='95%', height='600',
                                     style={'height': '45vh'}),

                         dbc.Row([dbc.Col([html.Div([
                             # html.Label('Select a week:', style={'fontSize': '20px'}),
                             dcc.Slider(
                                 id='myslider2',
                                 min=1,
                                 max=10,
                                 value=1,
                                 step=1,
                                 updatemode='drag',
                                 marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                        8: '8', 9: '9', 10: '10'},
                                 tooltip={"placement": "bottom", "always_visible": True}, included=False
                             ),
                             dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),
                         ], style={'width': '85%', 'margin': '20px', 'margin-top': '20px',
                                   # 'color': '#000000',
                                   'fontSize': '15px',
                                   'padding': '5px'})
                         ])]),

                     ],width={"size": 4}),


dbc.Col(
                     [
                         html.P(' Weekly class collective keywords ', className='text-center font-weight-bold',style={'fontWeight': 'bold'}),
                         html.Iframe(id='html-iframe-4', srcDoc=initial_html_aggregate, width='85%', height='1000',
                                     style={'height': '65vh'}),

                         dbc.Row([dbc.Col([html.Div([
                             # html.Label('Select a week:', style={'fontSize': '20px'}),
                             dcc.Slider(
                                 id='myslider3',
                                 min=1,
                                 max=10,
                                 value=1,
                                 step=1,
                                 updatemode='drag',
                                 marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                        8: '8', 9: '9', 10: '10'},
                                 tooltip={"placement": "bottom", "always_visible": True}, included=False
                             ),
                             dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),
                         ], style={'width': '85%', 'margin': '20px', 'margin-top': '20px',
                                   # 'color': '#000000',
                                   'fontSize': '15px',
                                   'padding': '5px'})
                         ])]),

                     ],width={"size": 6}),
                 #dbc.Col(
                     #[
                         #html.P('Total class collective keywords', className='font-weight-bold'),
                         #html.Iframe(id='html-iframe-3', srcDoc=initial_html_class, width='95%', height='600',
                                     #style={'height': '45vh'})

                     #])

             ], style={"height": "100vh"}
         )

         #        dbc.Row(
         #             [
         #                dbc.Col(
         #                    [ html.Hr(),
         #                     html.P('keywords of the whole class'),
         #                                      html.Div([
         #                                           dcc.Graph(id='keywords', figure=fig)
         #                                      ]), #md=10,

         #                 ])
         #         ],
         #        style={"height": "50vh", 'margin': '8px'}
         #    )
         ],
        fluid=True
    )
    ])


# Define the callbacks of year dropdown and weekly dropdown
@app.callback(
    Output('mydropdown', 'options'),
    Input('yeardropdown', 'value'))
def update_students(year):
    if year == '2021':
        options = [
            {'label': 'Student 1', 'value': 'student 1'},
            {'label': 'Student 2', 'value': 'student 2'},
            {'label': 'Student 3', 'value': 'student 3'},
            {'label': 'Student 4', 'value': 'student 4'},
            {'label': 'Student 5', 'value': 'student 5'},
            {'label': 'Student 6', 'value': 'student 6'},
            {'label': 'Student 7', 'value': 'student 7'}
        ]
    elif year == '2022':
        options = [
            {'label': 'Student 1', 'value': 'Student 1'},
            {'label': 'Student 2', 'value': 'Student 2'},
            {'label': 'Student 3', 'value': 'Student 3'},
            {'label': 'Student 4', 'value': 'Student 4'},
            {'label': 'Student 5', 'value': 'Student 5'},
            {'label': 'Student 6', 'value': 'Student 6'},
            {'label': 'Student 7', 'value': 'Student 7'},
            {'label': 'Student 8', 'value': 'Student 8'},
            {'label': 'Student 9', 'value': 'Student 9'},
            {'label': 'Student 10', 'value': 'Student 10'},
            {'label': 'Student 11', 'value': 'Student 11'},
            {'label': 'Student 12', 'value': 'Student 12'}
        ]
    elif year == '2023':
        options = [
            {'label': 'Student 1', 'value': 'student_1'},
            {'label': 'Student 2', 'value': 'student_2'},
            {'label': 'Student 3', 'value': 'student_3'},
            {'label': 'Student 4', 'value': 'student_4'},
            {'label': 'Student 5', 'value': 'student_5'},
            {'label': 'Student 6', 'value': 'student_6'},
            {'label': 'Student 7', 'value': 'student_7'},
            {'label': 'Student 8', 'value': 'student_8'},
            {'label': 'Student 9', 'value': 'student_9'},
            {'label': 'Student 10', 'value': 'student_10'},
            {'label': 'Student 11', 'value': 'student_11'},
            {'label': 'Student 12', 'value': 'student_12'}
        ]
    else:
        options = []
    return options





# Define the callbacks of year dropdown and aggregate  dropdown
@app.callback(
    Output('mydropdown2', 'options'),
    Input('yeardropdown', 'value'))
def update_students(year):
    if year == '2021':
        options = [
            {'label': 'Student 1', 'value': 'option_a'},
            {'label': 'Student 2', 'value': 'option_b'},
            {'label': 'Student 3', 'value': 'option_c'},
            {'label': 'Student 4', 'value': 'option_d'},
            {'label': 'Student 5', 'value': 'option_e'},
            {'label': 'Student 6', 'value': 'option_f'},
            {'label': 'Student 7', 'value': 'option_g'}
        ]
    elif year == '2022':
        options = [
            {'label': 'Student 1', 'value': 'option_A'},
            {'label': 'Student 2', 'value': 'option_B'},
            {'label': 'Student 3', 'value': 'option_C'},
            {'label': 'Student 4', 'value': 'option_D'},
            {'label': 'Student 5', 'value': 'option_E'},
            {'label': 'Student 6', 'value': 'option_F'},
            {'label': 'Student 7', 'value': 'option_G'},
            {'label': 'Student 8', 'value': 'option_H'},
            {'label': 'Student 9', 'value': 'option_I'},
            {'label': 'Student 10', 'value': 'option_J'},
            {'label': 'Student 11', 'value': 'option_K'},
            {'label': 'Student 12', 'value': 'option_L'}
        ]
    elif year == '2023':
        options = [
            {'label': 'Student 1', 'value': 'option A'},
            {'label': 'Student 2', 'value': 'option B'},
            {'label': 'Student 3', 'value': 'option C'},
            {'label': 'Student 4', 'value': 'option D'},
            {'label': 'Student 5', 'value': 'option E'},
            {'label': 'Student 6', 'value': 'option F'},
            {'label': 'Student 7', 'value': 'option G'},
            {'label': 'Student 8', 'value': 'option H'},
            {'label': 'Student 9', 'value': 'option I'},
            {'label': 'Student 10', 'value': 'option J'},
            {'label': 'Student 11', 'value': 'option K'},
            {'label': 'Student 12', 'value': 'option L'}
        ]
    else:
        options = []
    return options

# Define the callback function for Individual Weekly Graph
@app.callback(
    Output('html-iframe', 'srcDoc'),
   #[Input('mydropdown', 'value')]
    [Input('yeardropdown', 'value'),Input('mydropdown', 'value'),Input('myslider', 'value')]
)
def update_output(yeardropdown,mydropdown,myslider):
    # Define the HTML content to display based on the dropdown menu
    if yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 1:
        return open('assets/2021_s1_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 1:
        return open('assets/2021_s2_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 1:
        return open('assets/2021_s3_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 1:
        return open('assets/2021_s4_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 1:
        return open('assets/2021_s5_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 1:
        return open('assets/2021_s6_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 1:
        return open('assets/2021_s7_weekly_1.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 2:
        return open('assets/2021_s1_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 2:
        return open('assets/2021_s2_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 2:
        return open('assets/2021_s3_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 2:
        return open('assets/2021_s4_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 2:
        return open('assets/2021_s5_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 2:
        return open('assets/2021_s6_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 2:
        return open('assets/2021_s7_weekly_2.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 3:
        return open('assets/2021_s1_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 3:
        return open('assets/2021_s2_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 3:
        return open('assets/2021_s3_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 3:
        return open('assets/2021_s4_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 3:
        return open('assets/2021_s5_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 3:
        return open('assets/2021_s6_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 3:
        return open('assets/2021_s7_weekly_3.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 4:
        return open('assets/2021_s1_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 4:
        return open('assets/2021_s2_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 4:
        return open('assets/2021_s3_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 4:
        return open('assets/2021_s4_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 4:
        return open('assets/2021_s5_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 4:
        return open('assets/2021_s6_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 4:
        return open('assets/2021_s7_weekly_4.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 5:
        return open('assets/2021_s1_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 5:
        return open('assets/2021_s2_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 5:
        return open('assets/2021_s3_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 5:
        return open('assets/2021_s4_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 5:
        return open('assets/2021_s5_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 5:
        return open('assets/2021_s6_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 5:
        return open('assets/2021_s7_weekly_5.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 6:
        return open('assets/2021_s1_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider ==6:
        return open('assets/2021_s2_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 6:
        return open('assets/2021_s3_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 6:
        return open('assets/2021_s4_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 6:
        return open('assets/2021_s5_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 6:
        return open('assets/2021_s6_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 6:
        return open('assets/2021_s7_weekly_6.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 7:
        return open('assets/2021_s1_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 7:
        return open('assets/2021_s2_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 7:
        return open('assets/2021_s3_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 7:
        return open('assets/2021_s4_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 7:
        return open('assets/2021_s5_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 7:
        return open('assets/2021_s6_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 7:
        return open('assets/2021_s7_weekly_7.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 8:
        return open('assets/2021_s1_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider ==8:
        return open('assets/2021_s2_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 8:
        return open('assets/2021_s3_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 8:
        return open('assets/2021_s4_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 8:
        return open('assets/2021_s5_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 8:
        return open('assets/2021_s6_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 8:
        return open('assets/2021_s7_weekly_8.html', 'r').read()

    if yeardropdown=='2022' and mydropdown== 'Student 1'and myslider == 1:
        return open('assets/2022_s1_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 2'and myslider == 1:
        return open('assets/2022_s2_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 3'and myslider == 1:
        return open('assets/2022_s3_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 4'and myslider == 1:
        return open('assets/2022_s4_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 5'and myslider == 1:
        return open('assets/2022_s5_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 6'and myslider == 1:
        return open('assets/2022_s6_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 7'and myslider == 1:
        return open('assets/2022_s7_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 8'and myslider == 1:
        return open('assets/2022_s8_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 9'and myslider == 1:
        return open('assets/2022_s9_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 10'and myslider == 1:
        return open('assets/2022_s10_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 11'and myslider == 1:
        return open('assets/2022_s11_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 12'and myslider == 1:
        return open('assets/2022_s12_weekly_1.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 2:
        return open('assets/2022_s1_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 2:
        return open('assets/2022_s2_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 2:
        return open('assets/2022_s3_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 2:
        return open('assets/2022_s4_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 2:
        return open('assets/2022_s5_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 2:
        return open('assets/2022_s6_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 2:
        return open('assets/2022_s7_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 2:
        return open('assets/2022_s8_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 2:
        return open('assets/2022_s9_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 2:
        return open('assets/2022_s10_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 2:
        return open('assets/2022_s11_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 2:
        return open('assets/2022_s12_weekly_2.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 3:
        return open('assets/2022_s1_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 3:
        return open('assets/2022_s2_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 3:
        return open('assets/2022_s3_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 3:
        return open('assets/2022_s4_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 3:
        return open('assets/2022_s5_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 3:
        return open('assets/2022_s6_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 3:
        return open('assets/2022_s7_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 3:
        return open('assets/2022_s8_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 3:
        return open('assets/2022_s9_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 3:
        return open('assets/2022_s10_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 3:
        return open('assets/2022_s11_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 3:
        return open('assets/2022_s12_weekly_3.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 4:
        return open('assets/2022_s1_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 4:
        return open('assets/2022_s2_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 4:
        return open('assets/2022_s3_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 4:
        return open('assets/2022_s4_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 4:
        return open('assets/2022_s5_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 4:
        return open('assets/2022_s6_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 4:
        return open('assets/2022_s7_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 4:
        return open('assets/2022_s8_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 4:
        return open('assets/2022_s9_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 4:
        return open('assets/2022_s10_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 4:
        return open('assets/2022_s11_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 4:
        return open('assets/2022_s12_weekly_4.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 5:
        return open('assets/2022_s1_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 5:
        return open('assets/2022_s2_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 5:
        return open('assets/2022_s3_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 5:
        return open('assets/2022_s4_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 5:
        return open('assets/2022_s5_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 5:
        return open('assets/2022_s6_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 5:
        return open('assets/2022_s7_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 5:
        return open('assets/2022_s8_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 5:
        return open('assets/2022_s9_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 5:
        return open('assets/2022_s10_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 5:
        return open('assets/2022_s11_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 5:
        return open('assets/2022_s12_weekly_5.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 6:
        return open('assets/2022_s1_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 6:
        return open('assets/2022_s2_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 6:
        return open('assets/2022_s3_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 6:
        return open('assets/2022_s4_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 6:
        return open('assets/2022_s5_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 6:
        return open('assets/2022_s6_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 6:
        return open('assets/2022_s7_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 6:
        return open('assets/2022_s8_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 6:
        return open('assets/2022_s9_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 6:
        return open('assets/2022_s10_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 6:
        return open('assets/2022_s11_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 6:
        return open('assets/2022_s12_weekly_6.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 7:
        return open('assets/2022_s1_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 7:
        return open('assets/2022_s2_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 7:
        return open('assets/2022_s3_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 7:
        return open('assets/2022_s4_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 7:
        return open('assets/2022_s5_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 7:
        return open('assets/2022_s6_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 7:
        return open('assets/2022_s7_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 7:
        return open('assets/2022_s8_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 7:
        return open('assets/2022_s9_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 7:
        return open('assets/2022_s10_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 7:
        return open('assets/2022_s11_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 7:
        return open('assets/2022_s12_weekly_7.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 8:
        return open('assets/2022_s1_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 8:
        return open('assets/2022_s2_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 8:
        return open('assets/2022_s3_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 8:
        return open('assets/2022_s4_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 8:
        return open('assets/2022_s5_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 8:
        return open('assets/2022_s6_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 8:
        return open('assets/2022_s7_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 8:
        return open('assets/2022_s8_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 8:
        return open('assets/2022_s9_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 8:
        return open('assets/2022_s10_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 8:
        return open('assets/2022_s11_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 8:
        return open('assets/2022_s12_weekly_8.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 9:
        return open('assets/2022_s1_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 9:
        return open('assets/2022_s2_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 9:
        return open('assets/2022_s3_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 9:
        return open('assets/2022_s4_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 9:
        return open('assets/2022_s5_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 9:
        return open('assets/2022_s6_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 9:
        return open('assets/2022_s7_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 9:
        return open('assets/2022_s8_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 9:
        return open('assets/2022_s9_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 9:
        return open('assets/2022_s10_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 9:
        return open('assets/2022_s11_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 9:
        return open('assets/2022_s12_weekly_9.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 10:
        return open('assets/2022_s1_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 10:
        return open('assets/2022_s2_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 10:
        return open('assets/2022_s3_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 10:
        return open('assets/2022_s4_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 10:
        return open('assets/2022_s5_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 10:
        return open('assets/2022_s6_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 10:
        return open('assets/2022_s7_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 10:
        return open('assets/2022_s8_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 10:
        return open('assets/2022_s9_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 10:
        return open('assets/2022_s10_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 10:
        return open('assets/2022_s11_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 10:
        return open('assets/2022_s12_weekly_10.html', 'r').read()


    if yeardropdown=='2023' and mydropdown== 'student_1'and myslider == 1:
        return open('assets/2023_s1_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_2'and myslider == 1:
        return open('assets/2023_s2_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_3'and myslider == 1:
        return open('assets/2023_s3_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_4'and myslider == 1:
        return open('assets/2023_s4_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_5'and myslider == 1:
        return open('assets/2023_s5_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_6'and myslider == 1:
        return open('assets/2023_s6_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_7'and myslider == 1:
        return open('assets/2023_s7_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_8'and myslider == 1:
        return open('assets/2023_s8_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_9'and myslider == 1:
        return open('assets/2023_s9_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_10'and myslider == 1:
        return open('assets/2023_s10_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_11'and myslider == 1:
        return open('assets/2023_s11_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_12'and myslider == 1:
        return open('assets/2023_s12_weekly_1.html', 'r').read()

    elif yeardropdown=='2023' and mydropdown== 'student_1'and myslider == 2:
        return open('assets/2023_s1_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_2'and myslider == 2:
        return open('assets/2023_s2_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_3'and myslider == 2:
        return open('assets/2023_s3_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_4'and myslider == 2:
        return open('assets/2023_s4_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_5'and myslider == 2:
        return open('assets/2023_s5_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_6'and myslider == 2:
        return open('assets/2023_s6_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_7'and myslider == 2:
        return open('assets/2023_s7_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_8'and myslider == 2:
        return open('assets/2023_s8_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_9'and myslider == 2:
        return open('assets/2023_s9_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_10'and myslider == 2:
        return open('assets/2023_s10_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_11'and myslider == 2:
        return open('assets/2023_s11_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_12'and myslider == 2:
        return open('assets/2023_s12_weekly_2.html', 'r').read()

    elif yeardropdown=='2023' and mydropdown== 'student_1'and myslider == 3:
        return open('assets/2023_s1_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_2'and myslider == 3:
        return open('assets/2023_s2_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_3'and myslider == 3:
        return open('assets/2023_s3_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_4'and myslider == 3:
        return open('assets/2023_s4_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_5'and myslider == 3:
        return open('assets/2023_s5_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_6'and myslider == 3:
        return open('assets/2023_s6_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_7'and myslider == 3:
        return open('assets/2023_s7_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_8'and myslider == 3:
        return open('assets/2023_s8_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_9'and myslider == 3:
        return open('assets/2023_s9_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_10'and myslider == 3:
        return open('assets/2023_s10_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_11'and myslider == 3:
        return open('assets/2023_s11_weekly_3.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_12'and myslider == 3:
        return open('assets/2023_s12_weekly_3.html', 'r').read()

    elif yeardropdown=='2023' and mydropdown== 'student_1'and myslider == 4:
        return open('assets/2023_s1_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_2'and myslider == 4:
        return open('assets/2023_s2_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_3'and myslider == 4:
        return open('assets/2023_s3_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_4'and myslider == 4:
        return open('assets/2023_s4_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_5'and myslider == 4:
        return open('assets/2023_s5_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_6'and myslider == 4:
        return open('assets/2023_s6_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_7'and myslider == 4:
        return open('assets/2023_s7_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_8'and myslider == 4:
        return open('assets/2023_s8_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_9'and myslider == 4:
        return open('assets/2023_s9_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_10'and myslider == 4:
        return open('assets/2023_s10_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_11'and myslider == 4:
        return open('assets/2023_s11_weekly_4.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_12'and myslider == 4:
        return open('assets/2023_s12_weekly_4.html', 'r').read()

    elif yeardropdown=='2023' and mydropdown== 'student_1'and myslider == 5:
        return open('assets/2023_s1_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_2'and myslider == 5:
        return open('assets/2023_s2_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_3'and myslider == 5:
        return open('assets/2023_s3_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_4'and myslider == 5:
        return open('assets/2023_s4_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_5'and myslider == 5:
        return open('assets/2023_s5_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_6'and myslider == 5:
        return open('assets/2023_s6_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_7'and myslider == 5:
        return open('assets/2023_s7_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_8'and myslider == 5:
        return open('assets/2023_s8_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_9'and myslider == 5:
        return open('assets/2023_s9_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_10'and myslider == 5:
        return open('assets/2023_s10_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_11'and myslider == 5:
        return open('assets/2023_s11_weekly_5.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'student_12'and myslider == 5:
        return open('assets/2023_s12_weekly_5.html', 'r').read()

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
[Input('yeardropdown', 'value'), Input('mydropdown2', 'value'), Input('myslider2', 'value')]
    #[Input('mydropdown2', 'value')]
)
def update_output(yeardropdown,mydropdown2,myslider2):
    # Define the HTML content to display based on the dropdown menu
    if yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_1.html', 'r').read()

    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_1.html', 'r').read()

    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option A':
        return open('assets/2023_s1_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option B':
        return open('assets/2023_s2_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option C':
        return open('assets/2023_s3_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option D':
        return open('assets/2023_s4_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option E':
        return open('assets/2023_s5_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option F':
        return open('assets/2023_s6_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option G':
        return open('assets/2023_s7_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option H':
        return open('assets/2023_s8_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option I':
        return open('assets/2023_s9_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option J':
        return open('assets/2023_s10_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option K':
        return open('assets/2023_s11_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown2 == 'option L':
        return open('assets/2023_s12_aggregate_1.html', 'r').read()

    if yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_2.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_2.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option A':
        return open('assets/2023_s1_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option B':
        return open('assets/2023_s2_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option C':
        return open('assets/2023_s3_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option D':
        return open('assets/2023_s4_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option E':
        return open('assets/2023_s5_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option F':
        return open('assets/2023_s6_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option G':
        return open('assets/2023_s7_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option H':
        return open('assets/2023_s8_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option I':
        return open('assets/2023_s9_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option J':
        return open('assets/2023_s10_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option K':
        return open('assets/2023_s11_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown2 == 'option L':
        return open('assets/2023_s12_aggregate_2.html', 'r').read()
    #start here 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
    #week 3
    if yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_3.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_3.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option A':
        return open('assets/2023_s1_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option B':
        return open('assets/2023_s2_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option C':
        return open('assets/2023_s3_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option D':
        return open('assets/2023_s4_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option E':
        return open('assets/2023_s5_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option F':
        return open('assets/2023_s6_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option G':
        return open('assets/2023_s7_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option H':
        return open('assets/2023_s8_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option I':
        return open('assets/2023_s9_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option J':
        return open('assets/2023_s10_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option K':
        return open('assets/2023_s11_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown2 == 'option L':
        return open('assets/2023_s12_aggregate_3.html', 'r').read()
# Week 4

    if yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_4.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_4.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option A':
        return open('assets/2023_s1_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option B':
        return open('assets/2023_s2_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option C':
        return open('assets/2023_s3_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option D':
        return open('assets/2023_s4_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option E':
        return open('assets/2023_s5_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option F':
        return open('assets/2023_s6_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option G':
        return open('assets/2023_s7_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option H':
        return open('assets/2023_s8_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option I':
        return open('assets/2023_s9_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option J':
        return open('assets/2023_s10_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option K':
        return open('assets/2023_s11_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown2 == 'option L':
        return open('assets/2023_s12_aggregate_4.html', 'r').read()
# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 5
    if yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_5.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_5.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option A':
        return open('assets/2023_s1_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option B':
        return open('assets/2023_s2_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option C':
        return open('assets/2023_s3_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option D':
        return open('assets/2023_s4_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option E':
        return open('assets/2023_s5_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option F':
        return open('assets/2023_s6_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option G':
        return open('assets/2023_s7_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option H':
        return open('assets/2023_s8_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option I':
        return open('assets/2023_s9_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option J':
        return open('assets/2023_s10_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option K':
        return open('assets/2023_s11_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown2 == 'option L':
        return open('assets/2023_s12_aggregate_5.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 6
    if yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_6.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_6.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 7
    if yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_7.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_7.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 8
    if yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_a':
        return open('assets/2021_s1_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_b':
        return open('assets/2021_s2_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_c':
        return open('assets/2021_s3_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_d':
        return open('assets/2021_s4_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_e':
        return open('assets/2021_s5_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_f':
        return open('assets/2021_s6_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown2 == 'option_g':
        return open('assets/2021_s7_aggregate_8.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_8.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 9
    if yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_9.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 10
    if yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_A':
        return open('assets/2022_s1_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_B':
        return open('assets/2022_s2_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_C':
        return open('assets/2022_s3_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_D':
        return open('assets/2022_s4_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_E':
        return open('assets/2022_s5_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_F':
        return open('assets/2022_s6_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_G':
        return open('assets/2022_s7_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_H':
        return open('assets/2022_s8_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_I':
        return open('assets/2022_s9_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_J':
        return open('assets/2022_s10_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_K':
        return open('assets/2022_s11_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown2 == 'option_L':
        return open('assets/2022_s12_aggregate_10.html', 'r').read()



# Define the callback function for year Graph in total
#@app.callback(
    #Output('html-iframe-3', 'srcDoc'),
    #Input('mydropdown3', 'value')
    #Input('yeardropdown', 'value')
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
#)

#def update_output(value):
    # Define the HTML content to display based on the dropdown menu
    #if value == '2021':
        #return open('assets/2021_class_1.html', 'r').read()
    #elif value == '2022':
        #return open('assets/2022_class_1.html', 'r').read()
    #elif value == '2023':
        #return open('assets/2023_class_1.html', 'r').read()

# Define the callback function for Individual Weekly Graph
@app.callback(
    Output('html-iframe-4', 'srcDoc'),
    [Input('yeardropdown1', 'value'),Input('myslider3', 'value')]
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
)

def update_output(yeardropdown1,myslider3):
    # Define the HTML content to display based on the dropdown menu
    #2021
    if yeardropdown1 == '2021' and myslider3 ==1:
        return open('assets/2021_class_1.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 ==2:
        return open('assets/2021_class_2.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 3:
        return open('assets/2021_class_3.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 4:
        return open('assets/2021_class_4.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 5:
        return open('assets/2021_class_5.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 6:
        return open('assets/2021_class_6.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 7:
        return open('assets/2021_class_7.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 8:
        return open('assets/2021_class_8.html', 'r').read()
    #2022
    if yeardropdown1 == '2022'and myslider3 ==1:
        return open('assets/2022_class_1.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 ==2:
        return open('assets/2022_class_2.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 3:
        return open('assets/2022_class_3.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 4:
        return open('assets/2022_class_4.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 5:
        return open('assets/2022_class_5.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 6:
        return open('assets/2022_class_6.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 7:
        return open('assets/2022_class_7.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 8:
        return open('assets/2022_class_8.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 9:
        return open('assets/2022_class_9.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 10:
        return open('assets/2022_class_10.html', 'r').read()

        # 2023
    if yeardropdown1 == '2023'and myslider3 ==1:
        return open('assets/2023_class_1.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 ==2:
        return open('assets/2023_class_2.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 3:
        return open('assets/2023_class_3.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 4:
        return open('assets/2023_class_4.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 5:
        return open('assets/2023_class_5.html', 'r').read()



if __name__ == "__main__":
    app.run_server(port=8073)