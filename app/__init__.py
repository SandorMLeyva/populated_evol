from flask import Flask, render_template, make_response
from flask.json import jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return make_response(render_template('index.html'))


@app.route('/man')
def man():
	return jsonify({})
