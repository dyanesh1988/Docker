from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'Total Visitors are 55+5'
