from src.person import Person

class Collector:
    def __init__(self):
        self.max_woman = 0
        self.max_man = 0
        self.avg_age_death = 0
        self.avg_age_death = 0
        self.g_avg_age_death = 0
        self.g_avg_age_death = 0
        self.dead_by_age = {}
        self.g_dead_by_age = {}
        self.broken_partners = 0
        self.g_broken_partners = 0
        self.broken_partners_by_dead = 0
        self.g_broken_partners_by_dead = 0
        self.time_out_by_age = {}
        self.g_time_out_by_age = {}

    def analize(self, person: Person):
        pass

