import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.offline as offline
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# read in data from csv file
df = pd.read_csv('lineas_metro.csv',index_col=0)

df = df.T.iloc[::-1] 		# transform and reverse rows (to get caps in right order for heat map)
df = df.T 							# and then transform it back again.

app = dash.Dash(__name__)
server = app.server

# Change the title of the page from the default "Dash"
app.title = "Heatmap Metro"

# Using external css from chriddyp from plotly for ease
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

left_margin = 200
right_margin = 100

app.layout = html.Div([

	html.H1('Heatmap metro'),
	html.H2('Prueba'),
    dcc.Dropdown(
        placeholder="Selecciona el mes",
        options=[{'label': i, 'value': i} for i in df.index],
        multi=True,
        id='isv_select'
    ),
    dcc.Graph(id='heatmap_output')
])

@app.callback(
	Output('heatmap_output', 'figure'),
	[Input('isv_select', 'value')])
def update_figure(value):
    if value is None:
        return {'data': []}
    else:
        dff = df.loc[value,:]
        scaled_size = left_margin + right_margin + 150*len(value)
        return {
            'data': [{
                'z': dff.values.T.tolist(),
                'y': dff.columns.tolist(),
                'x': dff.index.tolist(),
                'ygap': 2,
                'reversescale': 'true',
                'colorscale': [[0, 'white'], [1, 'blue']],
                'type': 'heatmap',
            }],
            'layout': {
                'height': 750,
                'width': scaled_size,
                'xaxis': {'side':'top'},
                'margin': {
                	'l': left_margin,
                	'r': right_margin,
                	'b': 150,
                	't': 100
                }
            }
        }


if __name__ == '__main__':
    app.run_server(debug=True)