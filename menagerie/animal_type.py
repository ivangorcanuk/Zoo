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
    def __init__(self, number, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal):
        self._number = number
        self._nickname = nickname
        self._typeAnimal = typeAnimal
        self._predator = predator
        self._weight = weight  # вес
        self._dwells = dwells  # среда обитания
        self._climate = climate
        self._clasAnimal = clasAnimal

    def __gt__(self, other):
        return self._weight < other

    def inf(self):
        print('вызвали класс')

###############################################################################################################################
class Predator:  # хищные
    food = Instrumen()
    def __init__(self, food):
        self._food = food

class Herbivorous:  # травоядный
    food = Instrumen()
    def __init__(self, food):
        self._food = food

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
    migratory = Instrumen()
    def __init__(self, number, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory):
        super().__init__(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal)
        self._migratory = migratory

    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + str(self._weight)\
               + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + self._migratory + '#'

###########################################################################################################################################

class Parrot(Winged, Herbivorous):  # попугай
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, number, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)

    def inf(self):
        print('вызвали класс попугай')

class Otter(Underwater, Predator):  # выдра
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)
    def inf(self):
        print('вызвали класс выдра')

class Wolf(Ground, Predator):  # волк
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)
    def inf(self):
        print('вызвали класс волк')

class Hare(Ground, Herbivorous):  # заец
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс заец')

class Roe(Ground, Herbivorous):  # косуля
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс косуля')

class Buffalo(Ground, Herbivorous):  # бизон
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс бизон')

class Ostrich(Winged, Herbivorous):  # страус
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, number, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс страус')

class Dolphin(Underwater, Predator):  # дельфин
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)
    def inf(self):
        print('вызвали класс дельфин')

class Tiger(Ground, Predator):  # тигр
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)
    def inf(self):
        print('вызвали класс тигр')

class Octopus(Underwater, Predator):  # осьминог
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)
    def inf(self):
        print('вызвали класс осьминог')

class Crane(Winged, Herbivorous):  # журавль
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, number, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс журавль')

class Pike(Underwater, Predator):  # щука
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)
    def inf(self):
        print('вызвали класс щука')

class Zebra(Ground, Herbivorous):  # зебра
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, number, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс зебра')

class Pigeon(Winged, Herbivorous):  # голубь
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, number, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)
    def inf(self):
        print('вызвали класс голубь')