from working_files import WorkingUtils, FilesUtils
from GUI import *

"""Данные"""
class DataBackend:
    def __init__(self):
        self.listAnimal = FilesUtils.reading()  # создаем основной список с животными зоопарка
        self.listPredator = WorkingUtils.animal_sorting_tupe(True, self.listAnimal)  # создаем список с хищными животными
        self.listHerbivorous = WorkingUtils.animal_sorting_tupe(False, self.listAnimal)  # создаем список с травоядными животными
        self.listGround = WorkingUtils.animal_sorting_clas('наземный', self.listAnimal)  # создаем список с наземными животными
        self.listUnderwater = WorkingUtils.animal_sorting_clas('подводный', self.listAnimal)  # создаем список с подводными животными
        self.listWinged = WorkingUtils.animal_sorting_clas('крылатый', self.listAnimal)  # создаем список с крылатыми животными
        self.list_animal_type = WorkingUtils.saves_animal_type(self.listAnimal)  # сохраняем в отдельный список тип животных

        self.animal = None  # новоиспеченное животное

        self.top_3 = WorkingUtils.view_lungs_animal(self.listAnimal.copy())  # топ 3 самых легких существа зоопарка
        self.top_5 = WorkingUtils.viewing_large_animal(self.listPredator.copy())  # топ 3 самых легких существа зоопарка
        self.top_7 = WorkingUtils.view_descending_weight(self.listUnderwater.copy())  # топ 3 самых легких существа зоопарка
        print('создался объект класса DataBackend')

    def registration_animal(self, nickname, typeAnimal, predator, weight, dwells, climate, clas_animal, food, migratory):
        self.animal = WorkingUtils.registrationAnimal(nickname, typeAnimal, predator, weight, dwells, climate, clas_animal, food, migratory)
        self.listAnimal.append(self.animal)

    def save_info_file(self):
        FilesUtils.record(self.listAnimal)


if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.mainloop()