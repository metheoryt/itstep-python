"""
Абстрактные классы
PEP 3119
"""
from abc import ABCMeta, ABC, abstractmethod


class BasePet(metaclass=ABCMeta):  # аналогично - class BasePet(ABC):

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def kind(self) -> str:
        pass

    @abstractmethod
    def voice(self) -> str:
        pass

    def represent(self):
        return f'{self.kind} {self.name.title()} говорит "{self.voice()}"'


class Dog(BasePet):
    @property
    def kind(self) -> str:
        return 'пёс'

    def voice(self) -> str:
        return 'гав'


class Cat(BasePet):
    @property
    def kind(self) -> str:
        return 'кот'

    def voice(self) -> str:
        return 'мяу'


for pet in Cat('мурзик'), Dog('пушок'):
    print(f'{pet.kind} {pet.name.title()} говорит "{pet.voice()}"')
    print(pet.represent())
