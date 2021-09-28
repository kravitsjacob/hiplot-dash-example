# Example of embedding hiplot into dash

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import hiplot as hip

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Label(
            [
                'Select Columns',
                dcc.Dropdown(
                    id='columns_select',
                    options=[{"label": i, "value": i} for i in df.columns.astype(str).tolist()],
                    multi=True
                )
            ]
        ),
        html.Button(id='update_button', n_clicks=0, children='Update Plot'),
        html.Iframe(id='parallel') # style={'width': '100%', 'height': '1080px'}
    ]
)


@app.callback(
    Output('parallel', 'srcDoc'),
    Input('update_button', 'n_clicks'),
    State('columns_select', 'value'),
)
def update_parallel(n_clicks, columns_selected):

    srcDoc = 1
    return srcDoc


if __name__ == '__main__':
    app.run_server(debug=True)

