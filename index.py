from datetime import datetime as dt


class Creature:
    """ класс существа """
    def __int__(self, name: str,
                birthday: dt,
                body: 'Body'):
        self.name = name
        self.body = body



class Body:
    def __int__(self,
                helth: int,
                stamina: int,
                hunger: int,
                thirst: int):
        self.helts = helth
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst