
class Person:
	def __init__(self, age, gender, birthday_month):
		self.age = age
		self.gender = gender
		self.civil_status = 0
		self.time_out = 0
		self.max_children = 0 # TODO se genera
		self.children = 0
		self.birthday_month = birthday_month
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
		# en caso de que se rompa quitar las referencias

	def birthday(self, month):
		self.age = self.age+1 if not (month-self.birthday_month)%12 else self.age


class Woman(Person):
	def __init__(self, age,birthday_month):
		super().__init__(age,False, birthday_month)
		self.giving_birth = 0

	def pregnancy(self):
		# TODO calcular a ver sin se embaraza
		preg = True
		if preg and self.partner is not None and self.children != self.max_children \
				and self.partner.children != self.partner.max_children:
			self.giving_birth = 9

class Man(Person):
	def __init__(self, age,birthday_month):
		super().__init__(age,True, birthday_month)

