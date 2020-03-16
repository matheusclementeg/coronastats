from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))
port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)