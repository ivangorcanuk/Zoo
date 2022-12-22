class Instrumen:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class MainInf:
    number = Instrumen()
    nickname = Instrumen()
    typeAnimal = Instrumen()
    predator = Instrumen()
    weight = Instrumen()
    dwells = Instrumen()
    climate = Instrumen()
    clasAnimal = Instrumen()
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(), weight=float(), dwells=str(), climate=str(), clasAnimal=str(), migratory=str()):
        self._number = number
        self._nickname = nickname
        self._typeAnimal = typeAnimal
        self._predator = predator
        self._weight = weight  # вес
        self._dwells = dwells  # среда обитания
        self._climate = climate
        self._clasAnimal = clasAnimal
        self._migratory = migratory

    def __gt__(self, other):
        return self._weight < other

    @property
    def migratory(self):
        return self._migratory

    def inf(self):
        print('вызвали класс')

###############################################################################################################################
class Predator:  # хищные
    pass

class Herbivorous:  # травоядный
    pass

###############################################################################################################################
class Ground(MainInf):  # наземные
    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' +\
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

class Underwater(MainInf):  # подводные
    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + \
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

class Winged(MainInf):  # крылатые
    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + str(self._weight)\
               + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + self._migratory + '#'

    @property
    def migratory(self):
        return self._migratory

    @migratory.setter
    def migratory(self, migratory):
        self._migratory = migratory

###########################################################################################################################################

class Parrot(Winged, Herbivorous):  # попугай
    def inf(self):
        print('вызвали класс попугай')

class Otter(Underwater, Predator):  # выдра
    def inf(self):
        print('вызвали класс выдра')

class Wolf(Ground, Predator):  # волк
    def inf(self):
        print('вызвали класс волк')

class Hare(Ground, Herbivorous):  # заец
    def inf(self):
        print('вызвали класс заец')

class Roe(Ground, Herbivorous):  # косуля
    def inf(self):
        print('вызвали класс косуля')

class Buffalo(Ground, Herbivorous):  # бизон
    def inf(self):
        print('вызвали класс бизон')

class Ostrich(Winged, Herbivorous):  # страус
    def inf(self):
        print('вызвали класс страус')

class Dolphin(Underwater, Herbivorous):  # дельфин
    def inf(self):
        print('вызвали класс дельфин')

class Tiger(Ground, Predator):  # тигр
    def inf(self):
        print('вызвали класс тигр')

class Octopus(Underwater, Herbivorous):  # осьминог
    def inf(self):
        print('вызвали класс осьминог')

class Crane(Winged, Herbivorous):  # журавль
    def inf(self):
        print('вызвали класс журавль')

class Pike(Underwater, Predator):  # щука
    def inf(self):
        print('вызвали класс щука')

class Zebra(Ground, Herbivorous):  # зебра
    def inf(self):
        print('вызвали класс зебра')

class Pigeon(Winged, Herbivorous):  # голубь
    def inf(self):
        print('вызвали класс голубь')