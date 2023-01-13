import tkinter as tk
from main import Data

class MainMenu:  # главное меню
    def __init__(self):
        self.main = tk.Tk()
        self.main['bg'] = '#33ffe6'
        self.main.geometry(f'430x380+500+50')
        self.main.title('Zoo')

        self.button(self.main, 'Add an animal', self.open_window1).place(x=60, y=30, width=300, height=20)
        self.button(self.main, 'Animal Ratings', self.open_window2).place(x=60, y=60, width=300, height=20)
        self.button(self.main, 'See Animals', self.open_window3).place(x=60, y=90, width=300, height=20)
        self.button(self.main, 'Exit', self.main.destroy).place(x=60, y=150, width=300, height=20)

    @staticmethod
    def button(window, text, command):
        return tk.Button(window, text=text, font=('Arial', 13), command=command)

    @staticmethod
    def label(window, text):
        return tk.Label(window, text=text, font=('Arial', 13))

    @staticmethod
    def entry(window, variable):
        return tk.Entry(window, font=('Arial', 10), textvariable=variable)

    @staticmethod
    def radiobutton(window, value, variable):
        return tk.Radiobutton(window, text=value, font=('Arial', 13), variable=variable, value=value)

    @staticmethod
    def text(window):
        return tk.Text(window, font=('Arial', 13), bg='#33ffe6')

    def open_window1(self):
        addingAnimals = AddingAnimals()

    def open_window2(self):
        seeAnimals = AnimalRatings()

    def open_window3(self):
        deleteAnimal = SeeAnimals()

"""Добавление животного"""

class AddingAnimals:  # добавить животное
    def __init__(self):
        self.addingAnimals = tk.Toplevel()
        self.addingAnimals.grab_set()
        self.addingAnimals.title('Adding animals')
        self.addingAnimals['bg'] = '#33ffe6'
        self.addingAnimals.geometry(f'460x670+500+50')
        self.valueStrSubspecies = tk.StringVar(self.addingAnimals, 'esth')  # создали переменную со строковым значением подвид животного, которое будет возвращать наша радиокнопка
        self.valueStrHabitat = tk.StringVar(self.addingAnimals, 'est')  # аналогично для среды обитания
        self.valueStrClimate = tk.StringVar(self.addingAnimals, 'es')  # для климатических условий
        self.valueBoolIsMigratory = tk.StringVar(self.addingAnimals, '1')  # создали переменную с числовым значением - миграция
        self.valueBoolIsPredator = tk.StringVar(self.addingAnimals, '2')  # создали переменную с числовым значением - хищник
        self.value_food = tk.StringVar()  # создали переменную для пищи животного
        self.value_weight = tk.StringVar()  # создали переменную для веса животного
        self.value_nickname = tk.StringVar()  # создали переменную для клички животного

        MainMenu.label(self.addingAnimals, 'Выберите подвид животного:').place(x=10, y=10, width=240, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'ground', self.valueStrSubspecies).place(x=10, y=40, width=80, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'underwater', self.valueStrSubspecies).place(x=10, y=60, width=110, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'winged', self.valueStrSubspecies).place(x=10, y=80, width=80, height=20)

        MainMenu.label(self.addingAnimals, 'Укажите среду обитания данного подвида:').place(x=10, y=110, width=340, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'forests', self.valueStrHabitat).place(x=10, y=140, width=80, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'mountains', self.valueStrHabitat).place(x=10, y=160, width=100, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'steppes', self.valueStrHabitat).place(x=10, y=180, width=85, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'rivers', self.valueStrHabitat).place(x=10, y=200, width=65, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'seas', self.valueStrHabitat).place(x=10, y=220, width=60, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'ocean', self.valueStrHabitat).place(x=10, y=240, width=70, height=20)

        MainMenu.label(self.addingAnimals, 'Являются ли миграционным:').place(x=10, y=270, width=240, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'yes', self.valueBoolIsMigratory).place(x=10, y=300, width=55, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'no', self.valueBoolIsMigratory).place(x=10, y=320, width=45, height=20)

        MainMenu.label(self.addingAnimals, 'Укажите климатические условия:').place(x=10, y=350, width=270, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'warm', self.valueStrClimate).place(x=10, y=380, width=70, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'cold', self.valueStrClimate).place(x=10, y=400, width=60, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'moderate', self.valueStrClimate).place(x=10, y=420, width=95, height=20)

        MainMenu.label(self.addingAnimals, 'Явлиется ли зверь хищником:').place(x=10, y=450, width=245, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'yes', self.valueBoolIsPredator).place(x=10, y=480, width=55, height=20)
        MainMenu.radiobutton(self.addingAnimals, 'no', self.valueBoolIsPredator).place(x=10, y=500, width=45, height=20)

        MainMenu.label(self.addingAnimals, 'Какую пищу употребляет:').place(x=10, y=530, width=215, height=20)
        MainMenu.entry(self.addingAnimals, self.value_food).place(x=230, y=530, width=220, height=20)

        MainMenu.label(self.addingAnimals, 'Укажите вес животного:').place(x=10, y=560, width=195, height=20)
        MainMenu.entry(self.addingAnimals, self.value_weight).place(x=230, y=560, width=220, height=20)

        MainMenu.label(self.addingAnimals, 'Придумайте кличку для\n нового жителя зоопарка:').place(x=10, y=590, width=195, height=40)
        MainMenu.entry(self.addingAnimals, self.value_nickname).place(x=230, y=600, width=220, height=20)

        MainMenu.button(self.addingAnimals, 'exit', self.addingAnimals.destroy).place(x=380, y=640, width=70, height=20)
        MainMenu.button(self.addingAnimals, 'save', self.save).place(x=300, y=640, width=70, height=20)

    def save(self):
        subspecies_value = self.valueStrSubspecies.get()
        habitat_value = self.valueStrHabitat.get()
        climate_value = self.valueStrClimate.get()
        migratory_boolean = self.valueBoolIsMigratory.get() == 'yes'
        predator_boolean = self.valueBoolIsPredator.get() == 'yes'
        food_value = self.value_food.get()
        weight_value = self.value_weight.get()
        nickname_value = self.value_nickname.get()
        print(subspecies_value, habitat_value, climate_value, migratory_boolean, predator_boolean, food_value, weight_value, nickname_value)
        self.addingAnimals.destroy()

"""Просмотр рейтингов"""

class AnimalRatings:  # просмотр животных
    def __init__(self):
        self.animalRatings = tk.Toplevel()
        self.animalRatings.grab_set()
        self.animalRatings['bg'] = '#33ffe6'
        self.animalRatings.geometry(f'430x380+500+50')
        self.animalRatings.title('Animal Ratings')

        MainMenu.button(self.animalRatings, 'Top 3 Lightest Zoo Creatures', lambda: self.open_window(1)).place(x=60, y=30, width=300, height=20)
        MainMenu.button(self.animalRatings, 'Top 5 biggest predators', lambda: self.open_window(2)).place(x=60, y=60, width=300, height=20)
        MainMenu.button(self.animalRatings, 'List of herbivore names', lambda: self.open_window(3)).place(x=60, y=90, width=300, height=20)
        MainMenu.button(self.animalRatings, 'List of underwater creatures\n in decreasing order of their weight', lambda: self.open_window(4)).place(x=60, y=120, width=300, height=40)
        MainMenu.button(self.animalRatings, 'List of land animals,\n with each name and location', lambda: self.open_window(5)).place(x=60, y=170, width=300, height=40)
        MainMenu.button(self.animalRatings, 'Exit', self.animalRatings.destroy).place(x=60, y=350, width=300, height=20)
        self.text = MainMenu.text(self.animalRatings)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=60, y=230, width=300, height=100)

    def open_window(self, ark):
        self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне
        if ark == 1:
            list_animal = Data().listAnimal
            for i in range(len(list_animal)):  # топ 3 самых легких существа зоопарка
                for j in range(i, len(list_animal)):
                    if list_animal[i] > list_animal[j]:
                        f = list_animal[j]
                        list_animal[j] = list_animal[i]
                        list_animal[i] = f
                stroka = list_animal[i].nickname + ' ' + list_animal[i].clasAnimal + ' ' + str(list_animal[i].weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')  # выводим строку
                if i == 2:
                    break
        elif ark == 2:
            list_predator = Data().listPredator
            for i in range(len(list_predator)):  # топ 5 самых больших хищников
                for j in range(i, len(list_predator)):
                    if list_predator[i] < list_predator[j]:
                        f = list_predator[j]
                        list_predator[j] = list_predator[i]
                        list_predator[i] = f
                stroka = list_predator[i].nickname + ' ' + list_predator[i].clasAnimal + ' ' + str(list_predator[i].weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')
                if i == 4:
                    break
        elif ark == 3:
            list_herbivorous = Data().listHerbivorous
            for herbivorous in list_herbivorous:  # просмотр кличек травоядных существ
                stroka = herbivorous.nickname + ' ' + herbivorous.clasAnimal
                self.text.insert('end', f'{stroka}\n')
        elif ark == 4:
            list_underwater = Data().listUnderwater
            for i in range(len(list_underwater)):  # просмотр подводных существ по мере убывания их веса
                for j in range(i, len(list_underwater)):
                    if list_underwater[i] < list_underwater[j]:
                        f = list_underwater[j]
                        list_underwater[j] = list_underwater[i]
                        list_underwater[i] = f
                stroka = list_underwater[i].nickname + ' ' + list_underwater[i].clasAnimal + ' ' + str(list_underwater[i].weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')
        elif ark == 5:
            list_ground = Data().listGround
            for ground in list_ground:  # просмотр наземных животных с кличкой каждого и местом обитания
                stroka = ground.nickname + ' ' + ground.clasAnimal + ' ' + str(ground.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')

"""Просмотр животных"""

class SeeAnimals:  # просмотр
    def __init__(self):
        self.seeAnimals = tk.Toplevel()
        self.seeAnimals.grab_set()
        self.seeAnimals['bg'] = '#33ffe6'
        self.seeAnimals.geometry(f'430x380+500+50')
        self.seeAnimals.title('See Animals')
        self.choice_animal = tk.StringVar()  # создали переменную для выбора животного

        MainMenu.label(self.seeAnimals, text='Enter the name of the animal:').place(x=10, y=10, width=220, height=20)
        MainMenu.entry(self.seeAnimals, self.choice_animal).place(x=240, y=10, width=100, height=20)
        self.label = MainMenu.label(self.seeAnimals, 'Список всех животных зоопарка')
        self.label.place(x=90, y=40, width=285, height=20)
        MainMenu.button(self.seeAnimals, 'exit', self.seeAnimals.destroy).place(x=350, y=350, width=70, height=20)
        MainMenu.button(self.seeAnimals, 'search', self.selected_animal).place(x=350, y=10, width=70, height=20)
        self.text = MainMenu.text(self.seeAnimals)
        self.brings_out_animals()
        self.text.place(x=70, y=70, width=300, height=270)

    def brings_out_animals(self):
        for an in Data().listAnimal:
            stroka = an.nickname + ' ' + an.clasAnimal
            self.text.insert('end', f'{stroka}\n')

    def selected_animal(self):
        name_animal = self.choice_animal.get()
        if self.examination(name_animal):  # вызвали функицю класс-метод
            if self.label['text'] != 'Список всех животных зоопарка':
                self.label.config(text='Список всех животных зоопарка')
            window_animal = tk.Toplevel()
            window_animal.grab_set()
            window_animal.geometry(f'430x380+500+50')
            window_animal['bg'] = '#33ffe6'
            window_animal.title('Animal Information')
            MainMenu.button(window_animal, 'exit', window_animal.destroy).place(x=350, y=350, width=70, height=20)
            MainMenu.button(window_animal, 'delete', window_animal.destroy).place(x=260, y=350, width=80, height=20)
            text = MainMenu.text(window_animal)
            text.place(x=70, y=70, width=300, height=175)
            text.insert('end', f'{self.view_all_animals(name_animal)}')
        else:
            self.label.config(text='Вы указали неверное имя животного')

    def examination(self, animalName):  # проверяем есть ли выбранное животное в общем списке
        for name in Data().listAnimal:
            if name.nickname == animalName:
                return True
        return False

    def view_all_animals(self, name_animal):  # проверяем есть ли выбранное животное в общем списке
        for anm in Data().listAnimal:
            if anm.nickname == name_animal:
                if anm.predator:
                    predator = 'да'
                else:
                    predator = 'нет'
                tyh = f'Животное - {anm.clasAnimal}\n' \
                      f'Кличка - {anm.nickname}\n' \
                      f'Тип - {anm.typeAnimal}\n' \
                      f'Хищник - {predator}\n' \
                      f'Масса - {anm.weight}\n' \
                      f'Место обитания - {anm.dwells}\n' \
                      f'Климат - {anm.climate}\n' \
                      f'Употребляемая пища - мясо'
                if anm.typeAnimal == 'крылатый':
                    if anm.migratory:
                        migratory = 'да'
                    else:
                        migratory = 'нет'
                    tyh = tyh + f'\nМиграционный - {migratory}'
                return tyh

