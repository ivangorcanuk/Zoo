from animal_type import Ground, Underwater, Winged
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
                                     float(spTempAnimal[4]), spTempAnimal[5], spTempAnimal[6], spTempAnimal[7], spTempAnimal[8])
                    listAnimals.append(obj)
                    spTempAnimal = list()
        return listAnimals

    def record(self, listAnimal):  # запись в файл
        with open('animals.txt', 'w', encoding="utf-8") as file:
            for animal in listAnimal:
                file.writelines(str(animal) + '\n')
            file.close()

class WorkingMethods:
    def registrationAnimal(self, number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, migratory):
        obj = None
        if typeAnimal == 'наземный':
            obj = Ground(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal)
        elif typeAnimal == 'подводный':
            obj = Underwater(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal)
        elif typeAnimal == 'крылатый':
            obj = Winged(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, migratory)
        return obj

    def view_lungs_animal(self, listAnimal):  # топ 3 самых легких существа зоопарка
        for i in range(len(listAnimal)):
            for j in range(i, len(listAnimal)):
                if listAnimal[i] > listAnimal[j]:
                    f = listAnimal[j]
                    listAnimal[j] = listAnimal[i]
                    listAnimal[i] = f
            print(listAnimal[i].nickname, listAnimal[i].clasAnimal, listAnimal[i].weight)
            if i == 2:
                break

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

    def viewing_name_herbivorous(self, listHerbivorous):  # просмотр кличек травоядных существ
        for herbivorous in listHerbivorous:
            if herbivorous.predator == 'нет':
                print(herbivorous.nickname, herbivorous.clasAnimal)

    def viewing_large_animal(self, listPredator):  # топ 5 самых больших хищников
        for i in range(len(listPredator)):
            for j in range(i, len(listPredator)):
                if listPredator[i] < listPredator[j]:
                    f = listPredator[j]
                    listPredator[j] = listPredator[i]
                    listPredator[i] = f
            print(listPredator[i].nickname, listPredator[i].clasAnimal, listPredator[i].weight)
            if i == 4:
                break
