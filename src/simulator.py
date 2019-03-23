from src.person import *
from random import sample
from src.heap import *


class Simulator:
    def __init__(self):
        self.population = []
        self.t = 0
        self.Tf = 0
        self.events = Heap()
        self.man = 0
        self.woman = 0
        self.man_t = 0
        self.woman_t = 0

    def build(self, woman: int, man: int, time):
        self.t = 0
        self.Tf = time
        self.woman = self.woman_t = woman
        self.man = self.man_t = man

        for _ in range(woman):
            birthday = int(np.random.uniform(1, 12))
            new_person = Woman(birthday, int(np.random.uniform(0, 100)))
            self.population.append(new_person)
            self.events.insert(Event(new_person, 0, birthday))
        for _ in range(man):
            birthday = int(np.random.uniform(1, 12))
            new_person = Man(birthday, int(np.random.uniform(0, 100)))
            self.population.append(new_person)
            self.events.insert(Event(new_person, 0, birthday))

        self.population = sample(self.population, woman + man)

    def sim(self):

        while self.t <= self.Tf and len(self.population) > 0:

            event = self.events.ext_min()
            person = event.person
            self.t = event.time
            print('Mes', self.t)
            if not person.dead:
                # Birthday
                if event.type_event == 0:
                    person.birthday(self.t)
                    self.events.insert(Event(person, 0, self.t + 12))
                # Childbirth
                elif event.type_event == 1:
                    childs = person.childbirth(self.t)
                    for child in childs:
                        self.events.insert(Event(child, 0, self.t + 12))
                        self.population.append(child)
                        if child.gender:
                            self.man += 1
                            self.man_t += 1
                        else:
                            self.woman += 1
                            self.woman_t += 1

                    print('[Nace %s ninnos]' % len(childs))
                else:
                    person.end_time_out()

                # activate
                if person.die():
                    if person.gender:
                        self.man -= 1
                    else:
                        self.woman -= 1

                    if person.partner is not None:
                        self.events.insert(Event(person.partner, 2, person.partner.time_out + self.t))
                    self.population.remove(person)
                    print('Muere %s con %s annos y %s hijos' % (
                    'Hombre' if person.gender else 'Mujer', person.age, person.children))
                else:

                    breaking, ex = person.breaking_off()
                    if breaking:
                        print('Se rompio una pareja y tienen %s y %s de luto' % (person.time_out, ex.time_out))
                        self.events.insert(Event(person, 2, self.t + person.time_out))
                        self.events.insert(Event(ex, 2, self.t + ex.time_out))

                    self.population = sample(self.population, len(self.population))
                    for p in self.population:
                        new_match = person.get_partner(p)
                        if new_match:
                            print('Hay una nueva pareja')

                    if not person.gender and person.partner is not None and person.pregnancy():
                        print('Una mujer quedo embarazada')
                        self.events.insert(Event(person, 1, 9 + self.t))

        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('termino con poblacion %s, %s mujeres y %s hombres' % (len(self.population), self.woman, self.man))
        print('hubo un maximo de %s personas en el poblado, %s mujeres y %s hombres' % (
        str(self.man_t + self.woman_t), self.woman_t, self.man_t))
        print('La simulacion termino en %s meses' % self.t)



