from src.person import Person

class Collector:

    def __init__(self):
        self.woman_death = 0
        self.man_death = 0
        self.woman = 0
        self.man = 0
        self.dead_by_age = {}
        self.g_dead_by_age = {}
        self.broken_partners = 0
        self.g_broken_partners = 0
        self.broken_partners_by_dead = 0
        self.g_broken_partners_by_dead = 0
        self.time_out_by_age = {}
        self.g_time_out_by_age = {}
        self.lovers = 0
        self.g_lovers = 0
        self.g_t = 0

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

        if not t % 12:
            # TODO guarda en bd con el anno de los datos recogidos
            self.g_t += 1
            print('Anno', self.g_t)
            print('Nacieron %s mujeres y %s hombres' %(self.woman, self.man))
            print('Murieron %s mujeres y %s hombres' %(self.woman_death, self.man_death))
            print('Numero de muertes por edad', self.dead_by_age)
            print('Numero de personas viudas', self.broken_partners_by_dead)
            print('Numero de parejas formadas', self.lovers)
            print('Numero de rupturas', self.broken_partners)

            self.g_broken_partners += self.broken_partners
            self.g_lovers += self.lovers
            self.g_broken_partners_by_dead += self.broken_partners_by_dead
            # self.g_dead_by_age. += self.broken_partners_by_dead

            #clean
            self.woman = self.man = self.woman_death = self.man_death = self.lovers = self.broken_partners = self.broken_partners_by_dead = 0
            self.dead_by_age = {}


        if type_ == 1:
            if person.age in self.dead_by_age:
                self.dead_by_age[person.age] += 1
            else:
                self.dead_by_age[person.age] = 1

            if person.age in self.g_dead_by_age:
                self.g_dead_by_age[person.age] += 1
            else:
                self.g_dead_by_age[person.age] = 1
            if person.partner is not None:
                self.broken_partners_by_dead += 1
                self.g_broken_partners_by_dead += 1

            self.man_death += 1 if person.gender else 0
            self.woman_death += 1 if not person.gender else 0

        elif type_ == 2:
            self.man += 1 if person.gender else 0
            self.woman += 1 if not person.gender else 0

        elif type_ == 3:
            self.broken_partners += 1
            self.g_broken_partners += 1
            if person.age in self.time_out_by_age:
                self.time_out_by_age[person.age][0] += 1
                self.time_out_by_age[person.age][1] += person.time_out
            else:
                self.time_out_by_age[person.age] = [1, person.time_out]

        else:
            self.lovers += 1






