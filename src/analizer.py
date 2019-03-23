from src.person import Person


class Collector:

	def __init__(self):
		self.woman_death = 0
		self.g_woman_death = []
		self.man_death = 0
		self.g_man_death = []
		self.woman = 0
		self.man = 0
		self.woman_count = 0
		self.man_count = 0
		self.g_woman = []
		self.g_man = []
		self.dead_by_age = {}
		self.g_y_dead_by_age = []
		self.g_dead_by_age = {}
		self.broken_partners = 0
		self.g_broken_partners = []
		self.broken_partners_by_dead = 0
		self.g_broken_partners_by_dead = []
		self.time_out_by_age = {}
		self.g_y_time_out_by_age = []
		self.g_time_out_by_age = {}
		self.lovers = 0
		self.g_lovers = []
		self.g_t = 1
		self.current_t = 0
		self.important_years = []
		self.max_y_live_persons = []
		self.max_y_death_persons = []

	def analize(self, person: Person, type_, t):
		'''
        type_ = 1 : dead
                2 : born
                3 : borke
                4 : new love
        :param person:
        :param type_:
        :return:
        '''

		# TODO falta poner los tiempos de luto

		if  int(t / 12) != self.current_t:
			self.current_t = int(t/12)
			# TODO guarda en bd con el anno de los datos recogidos
			self.close_year(t)
			self.important_years.append(self.current_t)

		if type_ == 1:
			if person.age in self.dead_by_age:
				self.dead_by_age[person.age] += 1
			else:
				self.dead_by_age[person.age] = 1

			if person.partner is not None:
				self.broken_partners_by_dead += 1

			self.man_death += 1 if person.gender else 0
			self.woman_death += 1 if not person.gender else 0

		elif type_ == 2:
			self.man += 1 if person.gender else 0
			self.woman += 1 if not person.gender else 0

		elif type_ == 3:
			self.broken_partners += 1
			if person.age in self.time_out_by_age:
				# Lo guardo asi para poder calcular el promedio al final
				# [0] va la cantidad
				# [1] va la suma de todos los tiempos esperados
				self.time_out_by_age[person.age][0] += 1
				self.time_out_by_age[person.age][1] += person.time_out
			else:
				self.time_out_by_age[person.age] = [1, person.time_out]

		else:
			self.lovers += 1

	def close_year(self, t):

		print('Anno', self.current_t)
		print('meses', t)
		print('Nacieron %s mujeres y %s hombres' % (self.woman, self.man))
		print('Murieron %s mujeres y %s hombres' % (self.woman_death, self.man_death))
		print('Numero de muertes por edad', self.dead_by_age)
		print('Numero de personas viudas', self.broken_partners_by_dead)
		print('Numero de parejas formadas', self.lovers)
		print('Numero de rupturas', self.broken_partners)
		print('Tiempo de espera de las parejas', self.time_out_by_age)

		self.max_y_death_persons.append(self.woman_death+ self.man_death)
		self.max_y_live_persons.append(self.woman+ self.man)

		self.g_woman_death.append(self.woman_death)
		self.g_man_death.append(self.man_death)

		self.g_y_dead_by_age.append(self.dead_by_age)

		self.g_y_time_out_by_age.append(self.time_out_by_age)
		self.time_out_by_age = {}
		self.g_woman.append(self.woman)
		self.g_man.append(self.man)

		self.man_count += self.man
		self.woman_count += self.woman

		self.g_broken_partners.append(self.broken_partners)
		self.g_lovers.append(self.lovers)
		self.g_broken_partners_by_dead.append(self.broken_partners_by_dead)



		for key in self.dead_by_age.keys():
			if key in self.g_dead_by_age:
				self.g_dead_by_age[key] += self.dead_by_age[key]
			else:
				self.g_dead_by_age[key] = self.dead_by_age[key]

		# clean
		self.woman = self.man = self.woman_death = self.man_death = self.lovers = self.broken_partners = self.broken_partners_by_dead = 0
		self.dead_by_age = {}

