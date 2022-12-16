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
                    obj = None
                    if spTempAnimal[2] == 'наземный':
                        obj = Ground(spTempAnimal[0], spTempAnimal[1], spTempAnimal[2], spTempAnimal[3],
                                    float(spTempAnimal[4]), spTempAnimal[5], spTempAnimal[6], spTempAnimal[7])
                    elif spTempAnimal[2] == 'подводный':
                        obj = Underwater(spTempAnimal[0], spTempAnimal[1], spTempAnimal[2], spTempAnimal[3],
                                     float(spTempAnimal[4]), spTempAnimal[5], spTempAnimal[6], spTempAnimal[7])
                    elif spTempAnimal[2] == 'крылатый':
                        obj = Winged(spTempAnimal[0], spTempAnimal[1], spTempAnimal[2], spTempAnimal[3],
                                     float(spTempAnimal[4]), spTempAnimal[5], spTempAnimal[6], spTempAnimal[7], spTempAnimal[8])
                    listAnimals.append(obj)
                    spTempAnimal = list()
        return listAnimals

    def record(self):  # запись в файл
        pass

class WorkingMethods:
    def registrationAnimal(self):
        return 2 + 2