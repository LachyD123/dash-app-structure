from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.run_server(
            host=APP_HOST,
            port=APP_PORT,
            debug=APP_DEBUG,
            dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
        )
