from flask import Flask

app = Flask(__name__)

app.config.from_object('config.TestingConfig')

def add(num1, num2):
	return num1 + num2

@app.route('/')
def index():
	return "<h1>Hello World</h1>"