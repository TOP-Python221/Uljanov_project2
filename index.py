from datetime import datetime as dt
import dataclasses as dataclasses



class Body:
    helth: int
    stamina: int
    hunger: int
    thirst: int

    def tick_changes(self):
        pass



class Creature:
    """ класс существа """
    def __int__(self, name: str,
                birthday: dt,
                helts: int,
                stamina: int,
                hunger: int,
                thirst: int,
                ):
        self.name = name
        self.helts = helts
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst

    def feed(self):
        pass

    def play(self):
        pass

    def talk(self):
        pass

class Ming:
    pass

class StatesCalculator:

    def new_body(self) -> Body:
        pass

    def new_mind(self):
        pass

    def new_creature(self) -> Creature:
        pass

class PersistenceManager:

    def read_file(self):
        pass

    def write_file(self):
        pass


class StatesManager:
    pass

class BodyState:
    pass

class Mind:
   pass

class MindState:
    pass

