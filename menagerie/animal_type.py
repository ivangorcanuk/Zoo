class Instrumen:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        setattr(instance, self.name, value)

"""Базовый класс с общей информацией о всех животных"""

class MainInf:
    nickname = Instrumen()  # кличка
    typeAnimal = Instrumen()  # тип животного наземный/подводный/крылатый
    predator = Instrumen()  # хищник True/False
    weight = Instrumen()  # вес
    dwells = Instrumen()  # место обитания
    climate = Instrumen()  # климат
    clasAnimal = Instrumen()  # какому классу животного пренадлежит

    def __init__(self, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal):
        self._nickname = nickname
        self._typeAnimal = typeAnimal
        self._predator = predator
        self._weight = weight  # вес
        self._dwells = dwells  # среда обитания
        self._climate = climate
        self._clasAnimal = clasAnimal

    def __gt__(self, other):
        return self._weight < other

"""Классы делящие животных на хищников/травоядных"""

class Predator:  # хищные
    food = Instrumen()  # еда
    def __init__(self, food):
        self._food = food

class Herbivorous:  # травоядный
    food = Instrumen()  # еда
    def __init__(self, food):
        self._food = food

"""Классы делящие животных на наземных/подводныех/крылатых"""

class Ground(MainInf):  # наземные
    def __str__(self):
        return self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' +\
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

class Underwater(MainInf):  # подводные
    def __str__(self):
        return self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + \
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

class Winged(MainInf):  # крылатые
    migratory = Instrumen()
    def __init__(self, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory):
        super().__init__(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal)
        self._migratory = migratory

    def __str__(self):
        return self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + str(self._weight)\
               + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + self._migratory + '#'

"""Классы делящие животных по их типу"""

class Parrot(Winged, Herbivorous):  # попугай
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)

class Otter(Underwater, Predator):  # выдра
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)

class Wolf(Ground, Predator):  # волк
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)

class Hare(Ground, Herbivorous):  # заец
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)

class Roe(Ground, Herbivorous):  # косуля
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)

class Buffalo(Ground, Herbivorous):  # бизон
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)

class Ostrich(Winged, Herbivorous):  # страус
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)

class Dolphin(Underwater, Predator):  # дельфин
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)

class Tiger(Ground, Predator):  # тигр
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)

class Octopus(Underwater, Predator):  # осьминог
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)

class Crane(Winged, Herbivorous):  # журавль
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)

class Pike(Underwater, Predator):  # щука
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Underwater.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Predator.__init__(self, food)

class Zebra(Ground, Herbivorous):  # зебра
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str()):
        Ground.__init__(self, nickname, typeAnimal, predator,
                        weight, dwells, climate, clasAnimal)
        Herbivorous.__init__(self, food)

class Pigeon(Winged, Herbivorous):  # голубь
    def __init__(self, nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, typeAnimal, predator,
                 weight, dwells, climate, clasAnimal, migratory)
        Herbivorous.__init__(self, food)