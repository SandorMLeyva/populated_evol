
class Person:
	def __init__(self, age, gender, max_children, birthday):
		self.age = age
		self.gender = gender
		self.civil_status = 0
		self.time_out = 0
		self.max_children = max_children
		self.children = 0
		self.birthday = birthday
		self.partner = None

	# TODO
	@property
	def looking_couple(self):
		return True

	# TODO
	def death(self):
		return True

	def get_partner(self, person: Person):
		if not (self.civil_status or person.civil_status) and self.looking_couple and person.looking_couple:
			# TODO generar a ver si se hacen novios o que
			# poner self.partner = person y person.partner = self en caso de que si

	def breaking_off(self):
		# TODO generar a ver si se rompe la relacion
		# en caso de que se rompa
