import numpy as np
from tables import *


def get_key_by_age(age, table):
    ages = list(table.keys())
    ages.sort()
    for i in ages:
        if i >= age:
            return i
    return ages[-1]

def max_number_childs():
    while True:
        for max_number in MAX_NUMBER_CHILDS.keys():
            if MAX_NUMBER_CHILDS[max_number] >= np.random.uniform():
                return max_number if max_number <= 5 else max_number + int(np.random.uniform(0, 8))

class Person:

    def __init__(self, age, gender, birthday_month):
        self.age = age
        self.gender = gender
        self.time_out = 0
        self.max_children = max_number_childs()
        self.children = 0
        self.birthday_month = birthday_month
        self.partner = None
        self.dead = False

    @property
    def looking_couple(self):
        '''
		Propiedad que dice si la persona esta buscando pareja
		:return: boolean
		'''
        if self.time_out > 0:
            return False
        prob = AVAILABLE[get_key_by_age(self.age, AVAILABLE)]
        return prob >= self.generate_uniform_var

    def die(self):
        '''
		Comprueba si la persona muere y retorna un bool
		:return: boolean
		'''
        self.dead = False
        if self.age > 125 + int(np.random.uniform(0, 15)):
            self.dead = True

        if not self.dead:
            prob = DEATH[get_key_by_age(self.age, DEATH)]
            val_prob = prob[0 if self.gender else 1]
            self.dead = val_prob > self.generate_uniform_var

        # En caso de que muera y tenia pareja, actualizar a su pareja
        if self.dead and self.partner is not None:
            self.partner.partner = None
            # TODO fixed arreglar self.partner.time_out  pq hay que generar la variable exponencial
            self.partner.time_out = int(self.generate_exp_var(TIME_OFF[get_key_by_age(self.age, TIME_OFF)]))

        return self.dead

    def get_partner(self, person):
        '''
		Establece o no la relacion con la persona que recibe como parametro, y retorna un bool con la respuesta
		:param person:
		:return:
		'''
        if self.partner is None and person.partner is None and self.looking_couple and person.looking_couple and self.gender != person.gender:
            prob = MATCH[get_key_by_age(abs(self.age - person.age), MATCH)]
            relationship = prob >= self.generate_uniform_var
            if relationship:
                self.partner = person
                person.partner = self
            return relationship
        return False

    def breaking_off(self):
        '''
		Comprueba si la pareja se va a romper
		:return: boolena
		'''
        if self.partner is None:
            return False, None
        prob = 0.2
        breaking = prob >= self.generate_uniform_var
        p = self.partner
        if breaking:
            self.partner.partner = None
            # TODO fixed arreglar self.partner.time_out  pq hay que generar la variable exponencial
            self.partner.time_out = int(self.generate_exp_var(TIME_OFF[get_key_by_age(self.partner.age, TIME_OFF)]))
            self.partner = None
            # TODO fixed arreglar esta variable tambien
            self.time_out = int(self.generate_exp_var(TIME_OFF[get_key_by_age(self.age, TIME_OFF)]))
        return breaking, p

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

    def end_time_out(self):
        self.time_out = 0

    @property
    def generate_uniform_var(self):
        return np.random.uniform()

    @staticmethod
    def generate_exp_var(lambd):
        return -(1 / lambd) * np.log(np.random.uniform())


class Woman(Person):
    def __init__(self, birthday_month: int, age: int = 0) -> Person:
        super().__init__(age, False, birthday_month)
        self.giving_birth = 0

    def pregnancy(self):
        preg = PREGNANCY[get_key_by_age(self.age, PREGNANCY)] >= self.generate_uniform_var
        if preg and self.partner is not None and self.children < self.max_children \
                and self.partner.children < self.partner.max_children:
            self.giving_birth = 9
            return True
        return False

    def childbirth(self, month) -> list:
        while True:
            for number_child in NUMBER_BABY.keys():
                if self.generate_uniform_var <= NUMBER_BABY[number_child]:
                    self.children += number_child
                    # Esta condicion pq puede ser que el esposo halla muerto
                    if self.partner is not None:
                        self.partner.children += number_child
                    return [Woman(month) if 0.5 < self.generate_uniform_var else Man(month) for _ in range(number_child)]


class Man(Person):
    def __init__(self, birthday_month: int, age: int = 0) -> Person:
        super().__init__(age, True, birthday_month)


class Event:
    def __init__(self, person: Person, type_event: int, time: int):
        '''
		type_event = {
			0 -> Birthday
			1 -> Childbirth
			2 ->  End time out
		}
		:type time: object
		:param person:
		:param type_event:
		'''
        self.person = person
        self.type_event = type_event
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time

