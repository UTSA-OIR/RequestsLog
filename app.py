from flask import Flask, render_template, url_for, request       # Library Imports
import pandas as pd
import sqlalchemy
import pandas as pd
import sqlalchemy

app = Flask(__name__)                                # define our application
   


@app.route('/')                                  # url mapping
def homepage():
 
 
    return render_template("index.html")

