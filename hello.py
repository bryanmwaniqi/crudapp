from flask import Flask

app = Flask(__name__)

app.config.from_object('config.Development')

@app.route('/')
def index():
	return "<h1>Hello World</h1>"