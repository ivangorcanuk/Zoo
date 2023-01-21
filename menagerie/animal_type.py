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
    weight = Instrumen()  # вес
    dwells = Instrumen()  # место обитания
    climate = Instrumen()  # климат
    clas_animal = Instrumen()  # какому классу животного пренадлежит

    def __init__(self, nickname, weight, dwells, climate, clas_animal):
        self._nickname = nickname
        self._weight = weight  # вес
        self._dwells = dwells  # среда обитания
        self._climate = climate
        self._clas_animal = clas_animal

    def __gt__(self, other):
        return self._weight < other


"""Классы делящие животных на хищников/травоядных"""


class Predator:  # хищные
    predator = Instrumen()  # хищник True/False
    food = Instrumen()  # еда

    def __init__(self, predator, food):
        self._predator = predator
        self._food = food

    def pred(self):
        if self._predator:
            return 'да'
        else:
            return 'нет'


class Herbivorous:  # травоядный
    predator = Instrumen()  # хищник True/False
    food = Instrumen()  # еда

    def __init__(self, predator, food):
        self._predator = predator
        self._food = food

    def pred(self):
        if self._predator:
            return 'да'
        else:
            return 'нет'


"""Классы делящие животных на наземных/подводныех/крылатых"""


class Ground(MainInf):  # наземные
    type_animal = Instrumen()  # тип животного наземный/подводный/крылатый

    def __init__(self, nickname, type_animal, weight, dwells, climate, clas_animal):
        super().__init__(nickname, weight, dwells, climate, clas_animal)
        self._type_animal = type_animal


class Underwater(MainInf):  # подводные
    type_animal = Instrumen()  # тип животного наземный/подводный/крылатый

    def __init__(self, nickname, type_animal, weight, dwells, climate, clas_animal):
        super().__init__(nickname, weight, dwells, climate, clas_animal)
        self._type_animal = type_animal


class Winged(MainInf):  # крылатые
    migratory = Instrumen()
    type_animal = Instrumen()  # тип животного наземный/подводный/крылатый

    def __init__(self, nickname, type_animal, weight, dwells, climate, clas_animal, migratory):
        super().__init__(nickname, weight, dwells, climate, clas_animal)
        self._migratory = migratory
        self._type_animal = type_animal

    def migr(self):
        if self._migratory:
            return 'да'
        else:
            return 'нет'


"""Классы делящие животных по их типу"""


class Parrot(Winged, Herbivorous):  # попугай
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal, migratory)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' + \
               self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + self.migr() + '#'


class Otter(Underwater, Predator):  # выдра
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Underwater.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Predator.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Wolf(Ground, Predator):  # волк
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Ground.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Predator.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Hare(Ground, Herbivorous):  # заец
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Ground.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Roe(Ground, Herbivorous):  # косуля
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Ground.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Buffalo(Ground, Herbivorous):  # бизон
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Ground.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Ostrich(Winged, Herbivorous):  # страус
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal, migratory)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' + \
               self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + self.migr() + '#'


class Dolphin(Underwater, Predator):  # дельфин
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Underwater.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Predator.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Tiger(Ground, Predator):  # тигр
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Ground.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Predator.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Octopus(Underwater, Predator):  # осьминог
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Underwater.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Predator.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Crane(Winged, Herbivorous):  # журавль
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal, migratory)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight)+ '#' + \
               self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + self.migr() + '#'


class Pike(Underwater, Predator):  # щука
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Underwater.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Predator.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Zebra(Ground, Herbivorous):  # зебра
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str()):
        Ground.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' \
               + self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + '-' + '#'


class Pigeon(Winged, Herbivorous):  # голубь
    def __init__(self, nickname=str(), type_animal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clas_animal=str(), food=str(), migratory=str()):
        Winged.__init__(self, nickname, type_animal, weight, dwells, climate, clas_animal, migratory)
        Herbivorous.__init__(self, predator, food)

    def __str__(self):
        return self._nickname + '#' + self._type_animal + '#' + self.pred() + '#' + str(self._weight) + '#' + \
               self._dwells + '#' + self._climate + '#' + self._clas_animal + '#' + self._food + '#' + self.migr() + '#'