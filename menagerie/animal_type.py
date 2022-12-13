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
    def __init__(self, nickname=str(), weight=str(), number=str(), dwells=str(), climate=str()):
        self._nickname = nickname
        self._weight = weight  # вес
        self._number = number
        self._dwells = dwells
        self._climate = climate
###############################################################################################################################
class Predator:  # хищные
    pass

class NonPredator:  # нехищные
    pass

###############################################################################################################################
class Ground(MainInf):  # наземные
    def __str__(self):
        pass

class Underwater(MainInf):  # подводные
    def __str__(self):
        pass

class Winged(MainInf):  # крылатые
    def __str__(self):
        pass