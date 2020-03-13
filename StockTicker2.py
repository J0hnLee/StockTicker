# perform the basic imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# launch the application
app = dash.Dash()
# Create a Div to contain basic headers, an input box, and our graph
app.layout= html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a Stock Ticker:'),
    dcc.Input(id='puda',value='TSMC'),
    dcc.Graph(id='pudaGraph',
              figure={
                  'data':[
                      {'x':[1,2],'y':[3,4]}
        ]})
])

@app.callback(Output('pudaGraph','figure'),
              [Input('puda','value')])
def update_graph(stockTicker):
    fig={'data':
             [{'x': [7, 8], 'y': [3, 4]}],
         'layout':{'title':stockTicker}

    }
    return fig



if __name__ == '__main__':
    app.run_server()