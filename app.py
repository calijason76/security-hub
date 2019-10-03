import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

with open('data.txt') as f:
    lines = f.read().splitlines()

########### Define your variables ######
myheading = "What's your favorite Dunkin' Donut?"
mytitle = "Top 3 Flavors"
mylabels = lines[::2]
myvalues = lines[1::2]
color1 = 'e11383'
color2 = 'f5821f'
color3 = '683817'
color4 = 'e11383'
color5 = 'f5821f'
color6 = '683817'
color7 = 'e11383'
color8 = 'f5821f'
color9 = '683817'
color10 = 'e11383'
color11 = 'f5821f'
color12 = '683817'
color13 = 'e11383'
color14 = 'f5821f'
tabtitle = 'dunkin'
sourceurl = 'https://brandpalettes.com/dunkin-donuts-color-codes/'
githublink = 'https://github.com/austinlasseter/dash-piechart-example'

########### Set up the chart
mydata = go.Pie(
    hole=0.5,
    sort=False,
    values=myvalues,
    labels=mylabels,
    marker={'colors': [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14],
            'line': {'color': 'white', 'width': 5}}
)
mylayout = go.Layout(
    title = mytitle
)
fig = go.Figure(data=[mydata], layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
