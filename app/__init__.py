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
	'''
	Muertes por genero
	:param gender:
	:return:
	'''
	if gender == 'female':
		return jsonify({
			'number_d': app.data.g_woman_death,
			'len': app.data.important_years #list(range(len(app.data.g_woman_death)))
		})

	return jsonify({
		'number_d': app.data.g_man_death,
		'len': app.data.important_years
	})

@app.route('/deathbyage/<year>')
def death_bay_age(year):
	''''
	Muerte por edad de cada anno
	'''
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

@app.route('/deathbyage/all')
def death_bay_age_all():
	''''
	Muerte por edad de toda la simulacion
	'''
	# TODO revisar que aqui ha algo mal
	x = list(app.data.g_dead_by_age.keys())
	x.sort()
	y = app.data.g_dead_by_age
	return jsonify({
		'data' : [ y[item] for item in x],
		'x': x
	})

@app.route('/manvswoman')
def man_vs_woman():
	return jsonify({
		'man': app.data.man_count,
		'woman': app.data.woman_count
	})

@app.route('/born/<gender>')
def borns(gender):
	'''
	Nacidos por genero
	:param gender:
	:return:
	'''
	if gender == 'female':
		return jsonify({
			'number_d': app.data.g_woman,
			'len': app.data.important_years#list(range(len(app.data.g_woman)))
		})

	return jsonify({
		'number_d': app.data.g_man,
		'len': app.data.important_years#list(range(len(app.data.g_man)))
	})

@app.route('/widow')
def widow():
	return jsonify({
		'x': app.data.important_years, #list(range(len(app.data.g_broken_partners_by_dead))),
		'data': app.data.g_broken_partners_by_dead
	})

@app.route('/lovers')
def lovers():
	return jsonify({
		'x': app.data.important_years,#list(range(len(app.data.g_lovers))),
		'data': app.data.g_lovers
	})

@app.route('/brokenpartners')
def broken():
	return jsonify({
		'x': app.data.important_years,#list(range(len(app.data.g_broken_partners))),
		'data': app.data.g_broken_partners
	})


@app.route('/timeout/<year>')
def timeout(year):
	''''
	Tiempo de espera despues de una ruptura
	'''
	if int(year) >= len(app.data.g_y_time_out_by_age):
		return jsonify({
			'data': [],
			'x': []
		})
	x = list(app.data.g_y_time_out_by_age[int(year)].keys())
	x.sort()
	y = app.data.g_y_time_out_by_age[int(year)]
	return jsonify({
		'data' : [ y[item][1]/y[item][0] for item in x],
		'x': x
	})

@app.route('/maxborn')
def max_born():
	return jsonify({
		'x': app.data.important_years,#list(range(len(app.data.max_y_live_persons))),
		'data': app.data.max_y_live_persons
	})

@app.route('/maxdeath')
def max_death():
	return jsonify({
		'x': app.data.important_years,  #list(range(len(app.data.max_y_death_persons))),
		'data': app.data.max_y_death_persons
	})

