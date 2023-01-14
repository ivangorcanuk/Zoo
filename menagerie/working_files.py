from animal_type import Parrot, Otter, Wolf, Hare, Roe, Buffalo, Ostrich, Dolphin, Tiger, Octopus, Crane, Pike, Zebra, Pigeon
class WorkingFiles:
    def reading(self):  # считывание с файла
        with open('animals.txt', 'r', encoding="utf-8") as file:
            self.spisok = file.readlines()
        listAnimals = list()  # список с животными зоопарка, который будем возвращать
        spTempAnimal = list()  # список для временного хранения информации о животных
        for i in range(len(self.spisok)):
            if self.spisok[i] == '\n':
                break
            s = self.spisok[i].split('#')
            for j in range(len(s)):
                if s[j] != '\n':
                    spTempAnimal.append(s[j])
                else:
                    obj = WorkingMethods().registrationAnimal(spTempAnimal[0], spTempAnimal[1], spTempAnimal[2], spTempAnimal[3],
                    float(spTempAnimal[4]), spTempAnimal[5], spTempAnimal[6], spTempAnimal[7], spTempAnimal[8], spTempAnimal[9])
                    listAnimals.append(obj)
                    spTempAnimal = list()
        return listAnimals

    def record(self, listAnimal):  # запись в файл
        with open('animals.txt', 'w', encoding="utf-8") as file:
            for animal in listAnimal:
                file.writelines(str(animal) + '\n')
            file.close()

class WorkingMethods:
    def registrationAnimal(self, number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory):
        obj = None
        predator = predator == 'да'
        migratory = migratory == 'да'
        if clasAnimal == 'попугай':
            obj = Parrot(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        elif clasAnimal == 'выдра':
            obj = Otter(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'волк':
            obj = Wolf(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'заец':
            obj = Hare(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'косуля':
            obj = Roe(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'бизон':
            obj = Buffalo(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'страус':
            obj = Ostrich(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        elif clasAnimal == 'дельфин':
            obj = Dolphin(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'тигр':
            obj = Tiger(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'осьминог':
            obj = Octopus(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'журавль':
            obj = Crane(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        elif clasAnimal == 'щука':
            obj = Pike(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'зебра':
            obj = Zebra(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food)
        elif clasAnimal == 'голубь':
            obj = Pigeon(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, food, migratory)
        return obj

    def animal_sorting_tupe(self, tupe, listAnimal):  # сортировка животных на хищных и травоядных
        listOb = list()
        for animal in listAnimal:
            if tupe == animal.predator:
                listOb.append(animal)
        return listOb

    def animal_sorting_clas(self, clas, listAnimal):  # сортировка животных на наземные, подводные и крылатые
        listOb = list()
        for animal in listAnimal:
            if clas == animal.typeAnimal:
                listOb.append(animal)
        return listOb

    # def view_all_animals(self, text, listAnimal):  # просмотр всех животных
    #     for animals in listAnimal:
    #         stroka = animals.nickname + ' ' + animals.clasAnimal
    #         text.insert('end', f'{stroka}\n')  # выводим строку

    def view_lungs_animal(self, listAnimal):  # топ 3 самых легких существа зоопарка
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

    def viewing_large_animal(self, listPredator):  # топ 5 самых больших хищников
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

    # def viewing_name_herbivorous(self, text, listHerbivorous):  # просмотр кличек травоядных существ
    #     for herbivorous in listHerbivorous:
    #         stroka = herbivorous.nickname + ' ' + herbivorous.clasAnimal
    #         text.insert('end', f'{stroka}\n')

    def view_descending_weight(self, listUnderwater):  # просмотр подводных существ по мере убывания их веса
        list_under_desc_weight = list()
        for i in range(len(listUnderwater)):
            for j in range(i, len(listUnderwater)):
                if listUnderwater[i] < listUnderwater[j]:
                    f = listUnderwater[j]
                    listUnderwater[j] = listUnderwater[i]
                    listUnderwater[i] = f
            list_under_desc_weight.append(listUnderwater[i])
        return list_under_desc_weight

    # def viewing_habitats(self, text, listGround):  # просмотр наземных животных с кличкой каждого и местом обитания
    #     for ground in listGround:
    #         stroka = ground.nickname + ' ' + ground.clasAnimal + ' ' + ground.dwells + ' кг'
    #         text.insert('end', f'{stroka}\n')

    def number_assignment(self, listAnimal):  # присвоение уникального номера животному
        for animal in listAnimal:
            pass