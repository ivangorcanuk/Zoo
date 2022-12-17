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

    @property
    def migratory(self):
        return self._migratory

    @migratory.setter
    def migratory(self, migratory):
        self._migratory = None
###############################################################################################################################
class Predator:  # хищные
    def view_large(self):  # просмотр самых больших хищников
        pass

class Herbivorous:  # травоядный
    def viewing_name(self, listAnimal):  # просмотр кличек травоядных существ
        for herbivorous in listAnimal:
            if herbivorous.predator == 'нет':
                print(herbivorous.nickname, herbivorous.clasAnimal)

###############################################################################################################################
class Ground(MainInf):  # наземные
    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' +\
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

    def viewing_habitats(self, listAnimal):  # просмотр наземных животных с кличкой каждого и местом обитания
        for ground in listAnimal:
            if ground.typeAnimal == 'наземный':
                print(ground.nickname, ground.dwells)


class Underwater(MainInf):  # подводные
    def __str__(self):
        return self._number + '#' + self._nickname + '#' + self._typeAnimal + '#' + self._predator + '#' + \
               str(self._weight) + '#' + self._dwells + '#' + self._climate + '#' + self._clasAnimal + '-' + '#'

    def view_descending_weight(self):  # просмотр подводных существ по мере убывания их веса
        pass

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