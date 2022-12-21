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

    @migratory.setter
    def migratory(self, migratory):
        self._migratory = None
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

    def viewing_habitats(self, listAnimal):  # просмотр наземных животных с кличкой каждого и местом обитания
        for ground in listAnimal:
            if ground.typeAnimal == 'наземный':
                print(ground.nickname, ground.clasAnimal, ground.dwells)


class Underwater(MainInf):  # подводные
    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + \
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

    def view_descending_weight(self, listUnderwater):  # просмотр подводных существ по мере убывания их веса
        for i in range(len(listUnderwater)):
            for j in range(i, len(listUnderwater)):
                if listUnderwater[i] < listUnderwater[j]:
                    f = listUnderwater[j]
                    listUnderwater[j] = listUnderwater[i]
                    listUnderwater[i] = f
            print(listUnderwater[i].nickname, listUnderwater[i].clasAnimal, listUnderwater[i].weight)

class Winged(MainInf):  # крылатые
    #migratory = Instrumen()
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(),
                 weight=float(), dwells=str(), climate=str(), clasAnimal=str(), migratory=str()):
        super().__init__(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, migratory)
        #self._migratory = migratory  # миграционные

    @property
    def migratory(self):
        return self._migratory

    @migratory.setter
    def migratory(self, migratory):
        self._migratory = migratory

    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + str(self._weight)\
               + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + self._migratory + '#'

###########################################################################################################################################

class Parrot(Winged, Herbivorous):  # попугай
    pass

class Otter(Underwater, Predator):  # выдра
    pass

class Wolf(Ground, Predator):  # волк
    pass

class Hare(Ground, Herbivorous):  # заец
    pass

class Roe(Ground, Herbivorous):  # косуля
    pass

class Buffalo(Ground, Herbivorous):  # бизон
    pass

class Ostrich(Winged, Herbivorous):  # страус
    pass

class Dolphin(Underwater, Herbivorous):  # дельфин
    pass

class Tiger(Ground, Predator):  # тигр
    pass

class Octopus(Underwater, Herbivorous):  # осьминог
    pass

class Crane(Winged, Herbivorous):  # журавль
    pass

class Pike(Underwater, Predator):  # щука
    pass

class Zebra(Ground, Herbivorous):  # зебра
    pass

class Pigeon(Winged, Herbivorous):  # голубь
    pass