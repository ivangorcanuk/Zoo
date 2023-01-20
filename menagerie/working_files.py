from animal_type import Parrot, Otter, Wolf, Hare, Roe, Buffalo, Ostrich, Dolphin, Tiger, Octopus, Crane, Pike, Zebra, Pigeon


class FilesUtils:

    @staticmethod
    def reading():  # считывание с файла
        with open('animals.txt', 'r', encoding="utf-8") as file:
            spisok = file.readlines()
        listAnimals = list()  # список с животными зоопарка, который будем возвращать
        spTempAnimal = list()  # список для временного хранения информации о животных
        for i in range(len(spisok)):
            if spisok[i] == '\n':
                break
            s = spisok[i].split('#')
            for j in range(len(s)):
                if s[j] != '\n':
                    spTempAnimal.append(s[j])
                else:
                    spTempAnimal[2] = spTempAnimal[2] == 'да'
                    spTempAnimal[8] = spTempAnimal[8] == 'да'
                    obj = WorkingUtils.registrationAnimal(spTempAnimal[0], spTempAnimal[1], spTempAnimal[2], float(spTempAnimal[3]),
                    spTempAnimal[4], spTempAnimal[5], spTempAnimal[6], spTempAnimal[7], spTempAnimal[8])
                    #print(obj.nickname)
                    listAnimals.append(obj)
                    spTempAnimal = list()
        return listAnimals

    @staticmethod
    def record(listAnimal):  # запись в файл
        with open('animals.txt', 'w', encoding="utf-8") as file:
            for animal in listAnimal:
                file.writelines(str(animal) + '\n')
            file.close()


class WorkingUtils:  # класс только с полезными методами не содержащий данных

    @staticmethod
    def registrationAnimal(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory):
        obj = None
        if clasAnimal == 'попугай':
            obj = Parrot(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        elif clasAnimal == 'выдра':
            obj = Otter(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'волк':
            obj = Wolf(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'заяц':
            obj = Hare(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'косуля':
            obj = Roe(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'бизон':
            obj = Buffalo(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'страус':
            obj = Ostrich(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        elif clasAnimal == 'дельфин':
            obj = Dolphin(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'тигр':
            obj = Tiger(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'осьминог':
            obj = Octopus(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'журавль':
            obj = Crane(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        elif clasAnimal == 'щука':
            obj = Pike(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'зебра':
            obj = Zebra(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'голубь':
            obj = Pigeon(nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        return obj

    @staticmethod
    def animal_sorting_tupe(tupe, listAnimal):  # сортировка животных на хищных и травоядных
        listOb = list()
        for animal in listAnimal:
            if tupe == animal.predator:
                listOb.append(animal)
        return listOb

    @staticmethod
    def animal_sorting_clas(clas, listAnimal):  # сортировка животных на наземные, подводные и крылатые
        listOb = list()
        for animal in listAnimal:
            if clas == animal.typeAnimal:
                listOb.append(animal)
        return listOb

    @staticmethod
    def view_lungs_animal(listAnimal):  # топ 3 самых легких существа зоопарка
        list_light_creatures = list()
        for i in range(len(listAnimal)):
            for j in range(i, len(listAnimal)):
                if listAnimal[i] > listAnimal[j]:
                    f = listAnimal[j]
                    listAnimal[j] = listAnimal[i]
                    listAnimal[i] = f
            list_light_creatures.append(listAnimal[i])
            if i == 2:
                return list_light_creatures

    @staticmethod
    def viewing_large_animal(listPredator):  # топ 5 самых больших хищников
        list_big_predator = list()
        for i in range(len(listPredator)):
            for j in range(i, len(listPredator)):
                if listPredator[i] < listPredator[j]:
                    f = listPredator[j]
                    listPredator[j] = listPredator[i]
                    listPredator[i] = f
            list_big_predator.append(listPredator[i])
            if i == 4:
                return list_big_predator

    @staticmethod
    def view_descending_weight(listUnderwater):  # просмотр подводных существ по мере убывания их веса
        list_under_desc_weight = list()
        for i in range(len(listUnderwater)):
            for j in range(i, len(listUnderwater)):
                if listUnderwater[i] < listUnderwater[j]:
                    f = listUnderwater[j]
                    listUnderwater[j] = listUnderwater[i]
                    listUnderwater[i] = f
            list_under_desc_weight.append(listUnderwater[i])
        return list_under_desc_weight

    @staticmethod
    def saves_animal_names(listAnimal):  # сохраняем в отдельный список клички животных
        list_animal_names = list()
        for name in listAnimal:
            list_animal_names.append(name.nickname)
        return list_animal_names

    @staticmethod
    def saves_animal_type(listAnimal):  # сохраняем в отдельный список тип животных
        list_animal_type = list()
        for animal in listAnimal:
            list_animal_type.append(animal.clasAnimal)
        return list_animal_type