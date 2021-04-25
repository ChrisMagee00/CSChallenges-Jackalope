#import the Flask code
from flask import Flask
#declare our app
app = Flask(__name__)
#import our own routes file
from API import routes