from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))
app.run(host= 'http://coronaupdate.herokuapp.com/', port=environ.get('PORT'))
