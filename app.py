import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

with open('data.txt') as f:
    lines = f.read().splitlines()

########### Define your variables ######
myheading = "CIS Benchmarks for AWS"
mytitle = "Non-Compliance by Rule"
mylabels = lines[::2]
myvalues_init = lines[1::2]
myvalues [x[:-5] for x in myvalues_init]
color1 = 'e11383'
color2 = 'f5821f'
color3 = '683817'
color4 = 'DAF7A6'
color5 = '581845'
color6 = 'C70039'
color7 = 'FFC300'
color8 = '04DD1B'
color9 = 'DD040B'
color10 = '9DA8C6'
color11 = '580DBE'
color12 = 'B047EC'
color13 = 'DD770A'
color14 = '0BF8D0'
tabtitle = 'SecurityHub'
sourceurl = 'https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html'
githublink = 'https://github.com/calijason76/security-hub'

########### Set up the chart
mydata = go.Pie(
    hole=0.7,
    sort=False,
    values=myvalues,
    labels=mylabels,
    marker={'colors': [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14],
            'line': {'color': 'white', 'width': 3}}
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
