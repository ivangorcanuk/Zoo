class Instrumen:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class MainInf:
    nickname = Instrumen()
    weight = Instrumen()
    number = Instrumen()
    dwells = Instrumen()
    climate = Instrumen()
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(), weight=int(), dwells=str(), climate=str()):
        self._number = number
        self._nickname = nickname
        self.typeAnimal = typeAnimal
        self.predator = predator
        self._weight = weight  # вес
        self._dwells = dwells  # среда обитания
        self._climate = climate
###############################################################################################################################
# class Predator:  # хищные
#     pass
#
# class NonPredator:  # нехищные
#     pass

###############################################################################################################################
class Ground(MainInf):  # наземные
    def __str__(self):
        pass

class Underwater(MainInf):  # подводные
    def __str__(self):
        pass

class Winged(MainInf):  # крылатые
    migratory = Instrumen()
    def __init__(self, number=str(), nickname=str(), typeAnimal=str(), predator=str(), weight=int(), dwells=str(), climate=str(), migratory=str()):
        super().__init__(number, nickname, typeAnimal, predator, weight, dwells, climate)
        self.migratory = migratory  # миграционные

    def __str__(self):
        pass