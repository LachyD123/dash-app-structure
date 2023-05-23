# notes
'''
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
'''

# package imports
import dash
from dash import html
from flask import Flask


server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server
)


app.layout =  html.Div([
    html.Div(children='Hello World')
])   # set the layout to the serve_layout function
server = app.server         # the server is needed to deploy the application

if __name__ == "__main__":
    app.run_server(
      
    )


