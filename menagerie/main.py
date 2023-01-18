from working_files import WorkingMethods, WorkingFiles
from GUI import *

"""Данные"""
class DataBackend:
    def __init__(self):
        self.clasFiles = WorkingFiles()
        self.clasMetod = WorkingMethods()
        self.listAnimal = self.clasFiles.reading()  # создаем основной список с животными зоопарка
        self.listPredator = self.clasMetod.animal_sorting_tupe(True, self.listAnimal)  # создаем список с хищными животными
        self.listHerbivorous = self.clasMetod.animal_sorting_tupe(False, self.listAnimal)  # создаем список с травоядными животными
        self.listGround = self.clasMetod.animal_sorting_clas('наземный', self.listAnimal)  # создаем список с наземными животными
        self.listUnderwater = self.clasMetod.animal_sorting_clas('подводный', self.listAnimal)  # создаем список с подводными животными
        self.listWinged = self.clasMetod.animal_sorting_clas('крылатый', self.listAnimal)  # создаем список с крылатыми животными
        self.list_animal_names = self.clasMetod.saves_animal_names(self.listAnimal)  # сохраняем в отдельный список клички животных
        self.list_animal_type = self.clasMetod.saves_animal_type(self.listAnimal)  # сохраняем в отдельный список тип животных

        self.animal = None  # новоиспеченное животное

        self.top_3 = self.clasMetod.view_lungs_animal(self.listAnimal)  # топ 3 самых легких существа зоопарка
        self.top_5 = self.clasMetod.viewing_large_animal(self.listPredator)  # топ 3 самых легких существа зоопарка
        self.top_7 = self.clasMetod.view_descending_weight(self.listUnderwater)  # топ 3 самых легких существа зоопарка
        print('lur')

    def registration_animal(self, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory):
        self.animal = self.clasMetod.registrationAnimal(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        self.listAnimal.append(self.animal)
        print('mu')


if __name__ == "__main__":
    # for i in DataBackend().listAnimal:
    #     print(i.nickname)
    mainMenu = MainMenu()
    mainMenu.mainloop()