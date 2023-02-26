import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import json

url = 'http://127.0.0.1:5000/votes_geojson'
response = requests.get(url)
data = response.json()

df = pd.json_normalize(data['features'])

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='map'),
    dcc.Dropdown(id='dropdown', options=[{'label': 'AKP', 'value': 'AKP_per'},
                                          {'label': 'CHP', 'value': 'CHP_per'},
                                          {'label': 'MHP', 'value': 'MHP_per'},
                                          {'label': 'HDP', 'value': 'HDP_per'},
                                          {'label': 'IYI', 'value': 'IYIP_per'}])
])

@app.callback(Output('map', 'figure'),
              Input('dropdown', 'value'))
def update_figure(value):
    filtered_df = df[df['properties.parti_kisa_adi'] == value]
    fig = px.choropleth_mapbox(filtered_df, geojson=data, 
        locations='Plaka', color='value', 
        featureidkey='Plaka', zoom=5, center={'lat': 39.95, 'lon': 32.85}, 
        mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

