from flask import Flask, render_template, make_response
from flask.json import jsonify

app = Flask(__name__)
app.__setattr__('data', '')

@app.route('/')
def index():
	return make_response(render_template('index.html'))


@app.route('/man')
def man():
	return jsonify({'hola': app.data.g_dead_by_age })

@app.route('/death/<gender>')
def death(gender):
	if gender == 'female':
		return jsonify({
			'number_d': app.data.g_woman_death,
			'len': list(range(len(app.data.g_woman_death)))
		})

	return jsonify({
		'number_d': app.data.g_man_death,
		'len': list(range(len(app.data.g_man_death)))
	})

@app.route('/deathbyage/<year>')
def death_bay_age(year):
	if int(year) >= len(app.data.g_y_dead_by_age):
		return jsonify({
			'data': [],
			'x': []
		})
	x = list(app.data.g_y_dead_by_age[int(year)].keys())
	x.sort()
	y = app.data.g_y_dead_by_age[int(year)]
	return jsonify({
		'data' : [ y[item] for item in x],
		'x': x
	})

@app.route('/born/<gender>')
def borns(gender):
	if gender == 'female':
		return jsonify({
			'number_d': app.data.g_woman,
			'len': list(range(len(app.data.g_woman)))
		})

	return jsonify({
		'number_d': app.data.g_man,
		'len': list(range(len(app.data.g_man)))
	})
