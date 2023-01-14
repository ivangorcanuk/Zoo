from working_files import WorkingMethods, WorkingFiles
from GUI import *

"""Данные"""
class Data:
    def __init__(self):
        self.listAnimal = WorkingFiles().reading()  # создаем основной список с животными зоопарка
        self.clasMetod = WorkingMethods()
        self.listPredator = self.clasMetod.animal_sorting_tupe(True, self.listAnimal)  # создаем список с хищными животными
        self.listHerbivorous = self.clasMetod.animal_sorting_tupe(False, self.listAnimal)  # создаем список с травоядными животными
        self.listGround = self.clasMetod.animal_sorting_clas('наземный', self.listAnimal)  # создаем список с наземными животными
        self.listUnderwater = self.clasMetod.animal_sorting_clas('подводный', self.listAnimal)  # создаем список с подводными животными
        self.listWinged = self.clasMetod.animal_sorting_clas('крылатый', self.listAnimal)  # создаем список с крылатыми животными

        self.top_3 = self.clasMetod.view_lungs_animal(self.listAnimal)  # топ 3 самых легких существа зоопарка
        self.top_5 = self.clasMetod.viewing_large_animal(self.listPredator)  # топ 3 самых легких существа зоопарка
        self.top_7 = self.clasMetod.view_descending_weight(self.listUnderwater)  # топ 3 самых легких существа зоопарка


if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.mainloop()