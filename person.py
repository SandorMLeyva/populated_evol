import numpy as np
from tables import *


def get_key_by_age(age, table):
	ages = list(table.keys()).sort()
	for i in ages:
		if i > age:
			return i


class Person:
	def __init__(self, age, gender, birthday_month):
		self.age = age
		self.gender = gender
		self.civil_status = 0
		self.time_out = 0
		self.max_children = 0  # TODO se genera
		self.children = 0
		self.birthday_month = birthday_month
		self.partner = None

	@property
	def looking_couple(self):
		'''
		Propiedad que dice si la persona esta buscando pareja
		:return: boolean
		'''
		prob = AVAILABLE[get_key_by_age(self.age, AVAILABLE)]
		return prob >= self.generate_uniform_var

	def death(self):
		'''
		Comprueba si la persona muere y retorna un bool
		:return: boolean
		'''
		if self.age > 126:
			return True
		prob = DEATH[get_key_by_age(self.age, DEATH)]
		val_prob = prob[0 if self.gender else 1]
		is_death = val_prob >= self.generate_uniform_var

		# En caso de que muera y tenia pareja, actualizar a su pareja
		if is_death and self.partner is not None:
			self.partner.partner = None
			self.partner.civil_status = 0
			# TODO arreglar self.partner.time_out  pq hay que generar la variable exponencial
			self.partner.time_out = 5

		return is_death

	def get_partner(self, person: Person):
		'''
		Establece o no la relacion con la persona que recibe como parametro, y retorna un bool con la respuesta
		:param person:
		:return:
		'''
		if not (self.civil_status or person.civil_status) and self.looking_couple and person.looking_couple:
			prob = MATCH[get_key_by_age(abs(self.age - person.age), MATCH)]
			relationship = prob >= self.generate_uniform_var
			if relationship:
				self.partner = person
				self.civil_status = 1
				person.partner = self
				person.civil_status = 1
			return relationship
		return False

	def breaking_off(self):
		'''
		Comprueba si la pareja se va a romper
		:return: boolena
		'''
		prob = 0.2
		breaking = prob >= self.generate_uniform_var
		if breaking:
			self.partner.partner = None
			self.partner.civil_status = 0
			# TODO arreglar self.partner.time_out  pq hay que generar la variable exponencial
			self.partner.time_out = TIME_OFF[get_key_by_age(self.partner.age, TIME_OFF)]
			self.partner = None
			self.civil_status = 0
			# TODO arreglar esta variable tambien
			self.time_out = TIME_OFF[get_key_by_age(self.age, TIME_OFF)]
		return breaking

	def birthday(self, month):
		'''
		Dice si es el cumpleannos
		:param month:
		:return:boolen
		'''
		if (month - self.birthday_month) % 12:
			return False
		self.age = self.age + 1
		return True

	@property
	def generate_uniform_var(self):
		return np.random.uniform()

	@staticmethod
	def generate_exp_var(lambd):
		return -(1 / lambd) * np.log(np.random.uniform())


class Woman(Person):
	def __init__(self, birthday_month: int, age: int = 0)-> Person:
		super().__init__(age, False, birthday_month)
		self.giving_birth = 0

	def pregnancy(self):
		preg = PREGNANCY[get_key_by_age(self.age, PREGNANCY)] >= self.generate_uniform_var
		if preg and self.partner is not None and self.children != self.max_children \
				and self.partner.children != self.partner.max_children:
			self.giving_birth = 9

	def childbirth(self, month) -> list[Person]:
		if self.giving_birth == 0:
			number_child = NUMBER_BABY[get_key_by_age(self.generate_uniform_var, NUMBER_BABY)]
			return [Woman(month) if 0.5 < np.random.uniform() else Man(month) for _ in range(number_child)]
		return []


class Man(Person):
	def __init__(self, birthday_month: int, age: int = 0) -> Person:
		super().__init__(age, True, birthday_month)
