from datetime import datetime as dt
import dataclasses as dataclasses


class Body:
    # для хранения текущих (мгновенных) значений
    def __init__(self,
                 helth: int,
                 stamina: int,
                 hunger: int,
                 thirst: int):
        self.helth = helth
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst

    def tick_changes(self):
        pass

class CreatureState:
        """ класс хранитель """
        helth: int
        stamina: int
        hunger: int
        thirst: int

class Creature:
    """ класс существа """
    def __int__(self, name: str,
                age: int,
                birthday: dt,
                body: Body,
                ):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.body = body

        # метод для сохранения состояния существа
        def state() -> 'CharacterState':
            pass

    def feed(self):
        """"""
        pass

    def play(self):
        pass

    def talk(self):
        pass

class Mind:
    pass

class StatesCalculator:

    def new_body(self) -> Body:
        # для вычисления настроения, хранения последних значений
        def __init__(self, joy: int,
                     anger: int,
                     ):
            self.joy = joy
            self.anger = anger

    def new_mind(self):
        pass

    def new_creature(self) -> Creature:
        pass


class PersistenceManager:
    pass

class StatesManager:
    """ класс опекун """
    def read_file(self) -> 'CharacterState':
        pass

    def write_file(last_state: 'CharacterState') -> None:
        pass


class BodyState:
    pass


class MindState:
    pass

