from person import *
from random import sample

class Heap:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
        self.data.sort(key= lambda x: x.time)

    def ext_min(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

class Simulator:
    def __init__(self):
        self.population = []
        self.t = 0
        self.Tf = 0
        self.events = Heap() # esto tiene que ser un heap

    def build(self, woman: int, man: int, time):
        self.t = 0
        self.Tf = time
        for _ in range(woman):
            birthday = int(np.random.uniform(1, 12))
            new_person = Woman(birthday, int(np.random.uniform(0, 100)))
            self.population.append(new_person)
            self.events.insert(Event(new_person,0, birthday))
        for _ in range(man):
            birthday = int(np.random.uniform(1, 12))
            new_person = Man(birthday, int(np.random.uniform(0, 100)))
            self.population.append(new_person)
            self.events.insert(Event(new_person,0, birthday))

        self.population = sample(self.population, woman+man)




    def sim(self):

        while self.t <= self.Tf and len(self.population) > 0:

            event = self.events.ext_min()
            person = event.person
            self.t = event.time

            # TODO activar a cada persona ver cual es el mejor lugar que no coincida con nada mas
            # TODO comprobar que el evento no es de una persona muerta,
            if not person.dead:
                # Birthday
                if event.type_event == 0:
                    person.birthday(self.t)
                    self.events.insert(Event(person, 0, self.t+12))
                # Childbirth
                elif event.type_event == 1:
                    childs = person.childbirth(self.t)
                    for child in childs:
                        self.events.insert(Event(child, 0, self.t+12))
                        self.population.append(child)
                    print('nacieron', len(childs))
                else:
                    person.end_time_out()

                # activate
                if person.die():
                    if person.partner is not None:
                        self.events.insert(Event(person.partner, 2, person.partner.time_out + self.t))
                    self.population.remove(person)
                    print('Muerte con edad', person.age, person.gender)
                else:
                    self.population = sample(self.population, len(self.population))
                    for p in self.population:
                        person.get_partner(p)

                    breaking, ex = person.breaking_off()
                    if breaking:
                        self.events.insert(Event(person, 2, self.t + person.time_out))
                        self.events.insert(Event(ex, 2, self.t + ex.time_out))

                    if not person.gender and person.partner is not None and person.pregnancy():
                        self.events.insert(Event(person, 1, 9+self.t))
            # print('poblacion', len(self.population))
        print('termino con poblacion',len(self.population))




s = Simulator()
s.build(5,5,12)
s.sim()
