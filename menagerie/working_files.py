from animal_type import Ground, Underwater, Winged
class WorkingFiles:
    def reading(self):  # считывание с файла
        with open('animals.txt', 'r', encoding="utf-8") as file:
            self.spisok = file.readlines()
        listAnimals = list()  # список с комнатами отеля, который будем возвращать
        spTempAnimal = list()  # список для временного хранения информации о комнатах
        for i in range(len(self.spisok)):
            if self.spisok[i] == '\n':
                break
            s = self.spisok[i].split('#')
            for j in range(len(s)):
                if s[j] != '\n':
                    spTempAnimal.append(s[j])
                else:
                    if spTempAnimal[2] == 'наземный':
                        listAnimals.append(Ground(spTempAnimal[1], int(spTempAnimal[4]), spTempAnimal[0], spTemporyRoom[4]))
                    elif spTempAnimal[2] == 'подводный':
                        listAnimals.append(Ground(spTemporyRoom[0], int(spTemporyRoom[1]), int(spTemporyRoom[2]),
                                             int(spTemporyRoom[3]), spTemporyRoom[4], isVideo))
                    elif spTempAnimal[2] == 'крылатый':
                        listAnimals.append(Ground(spTemporyRoom[0], int(spTemporyRoom[1]), int(spTemporyRoom[2]),
                                             int(spTemporyRoom[3]), spTemporyRoom[4], isVideo))
                    spTemporyRoom = list()
        return spAnimal

    def record(self):  # запись в файл
        pass