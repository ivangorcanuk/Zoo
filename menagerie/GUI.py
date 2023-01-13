import tkinter as tk
from main import Data

class MainMenu:  # главное меню
    def __init__(self):
        self.main = tk.Tk()
        self.main['bg'] = '#33ffe6'
        self.main.geometry(f'240x271+100+200')
        self.main.title('Zoo')

        self.button(self.main, 'Add an animal', self.open_window1).grid(row=1, column=0, sticky='wens', padx=50, pady=2)
        self.button(self.main, 'Animal Ratings', self.open_window2).grid(row=2, column=0, sticky='wens', padx=50, pady=2)
        self.button(self.main, 'See Animals', self.open_window3).grid(row=3, column=0, sticky='wens', padx=50, pady=2)
        self.button(self.main, 'Exid', self.main.destroy).grid(row=4, column=0, sticky='wens', padx=50, pady=2)

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
        self.addingAnimals.geometry(f'500x600+500+50')
        self.valueStrSubspecies = tk.StringVar(self.addingAnimals, 'esth')  # создали переменную со строковым значением подвид животного, которое будет возвращать наша радиокнопка
        self.valueStrHabitat = tk.StringVar(self.addingAnimals, 'est')  # аналогично для среды обитания
        self.valueStrClimate = tk.StringVar(self.addingAnimals, 'es')  # для климатических условий
        self.valueBoolIsMigratory = tk.StringVar(self.addingAnimals, '1')  # создали переменную с числовым значением - миграция
        self.valueBoolIsPredator = tk.StringVar(self.addingAnimals, '2')  # создали переменную с числовым значением - хищник
        self.value_food = tk.StringVar()  # создали переменную для пищи животного
        self.value_weight = tk.StringVar()  # создали переменную для веса животного
        self.value_nickname = tk.StringVar()  # создали переменную для клички животного

        MainMenu.label(self.addingAnimals, 'Выберите подвид животного:').grid(row=0, columnspan=3)
        MainMenu.radiobutton(self.addingAnimals, 'ground', self.valueStrSubspecies).grid(row=1, column=0)
        MainMenu.radiobutton(self.addingAnimals, 'underwater', self.valueStrSubspecies).grid(row=1, column=1)
        MainMenu.radiobutton(self.addingAnimals, 'winged', self.valueStrSubspecies).grid(row=1, column=2)

        MainMenu.label(self.addingAnimals, 'Укажите среду обитания данного подвида:').grid(row=2, columnspan=3)
        MainMenu.radiobutton(self.addingAnimals, 'forests', self.valueStrHabitat).grid(row=3, column=0)
        MainMenu.radiobutton(self.addingAnimals, 'mountains', self.valueStrHabitat).grid(row=4, column=0)
        MainMenu.radiobutton(self.addingAnimals, 'steppes', self.valueStrHabitat).grid(row=3, column=1)
        MainMenu.radiobutton(self.addingAnimals, 'rivers', self.valueStrHabitat).grid(row=4, column=1)
        MainMenu.radiobutton(self.addingAnimals, 'seas', self.valueStrHabitat).grid(row=3, column=2)
        MainMenu.radiobutton(self.addingAnimals, 'ocean', self.valueStrHabitat).grid(row=4, column=2)

        MainMenu.label(self.addingAnimals, 'Являются ли миграционным:').grid(row=5, columnspan=3)
        MainMenu.radiobutton(self.addingAnimals, 'yes', self.valueBoolIsMigratory).grid(row=6, column=0)
        MainMenu.radiobutton(self.addingAnimals, 'no', self.valueBoolIsMigratory).grid(row=6, column=1)

        MainMenu.label(self.addingAnimals, 'Укажите климатические условия:').grid(row=7, columnspan=3)
        MainMenu.radiobutton(self.addingAnimals, 'warm', self.valueStrClimate).grid(row=8, column=0)
        MainMenu.radiobutton(self.addingAnimals, 'cold', self.valueStrClimate).grid(row=8, column=1)
        MainMenu.radiobutton(self.addingAnimals, 'moderate', self.valueStrClimate).grid(row=8, column=2)

        MainMenu.label(self.addingAnimals, 'Явлиется ли зверь хищником:').grid(row=9, columnspan=3)
        MainMenu.radiobutton(self.addingAnimals, 'yes', self.valueBoolIsPredator).grid(row=10, column=0)
        MainMenu.radiobutton(self.addingAnimals, 'no', self.valueBoolIsPredator).grid(row=10, column=1)

        MainMenu.label(self.addingAnimals, 'Какую пищу употребляет:').grid(row=11, column=0)
        MainMenu.entry(self.addingAnimals, self.value_food).grid(row=11, column=1)

        MainMenu.label(self.addingAnimals, 'Укажите вес животного:').grid(row=12, column=0)
        MainMenu.entry(self.addingAnimals, self.value_weight).grid(row=12, column=1)

        MainMenu.label(self.addingAnimals, 'Придумайте кличку \n для нового жителя зоопарка:').grid(row=13, column=0)
        MainMenu.entry(self.addingAnimals, self.value_nickname).grid(row=13, column=1)

        MainMenu.button(self.addingAnimals, 'exit', self.addingAnimals.destroy).grid(row=17, column=0)
        MainMenu.button(self.addingAnimals, 'save', self.save).grid(row=17, column=2)

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
        self.animalRatings.geometry(f'550x500+500+50')
        self.animalRatings.title('Animal Ratings')

        MainMenu.button(self.animalRatings, 'Top 3 Lightest Zoo Creatures', lambda: self.open_window(1)).grid(row=1, column=0, padx=30, pady=2)
        MainMenu.button(self.animalRatings, 'Top 5 biggest predators', lambda: self.open_window(2)).grid(row=2, column=0, padx=30, pady=2)
        MainMenu.button(self.animalRatings, 'List of herbivore names', lambda: self.open_window(3)).grid(row=3, column=0, padx=30, pady=2)
        MainMenu.button(self.animalRatings, 'List of underwater creatures in decreasing order of their weight', lambda: self.open_window(4)).grid(row=4, column=0, padx=30, pady=2)
        MainMenu.button(self.animalRatings, 'List of land animals, with each name and location', lambda: self.open_window(5)).grid(row=5, column=0, padx=30, pady=2)
        MainMenu.button(self.animalRatings, 'Exit', self.animalRatings.destroy).grid(row=6, column=0, padx=30, pady=2)
        self.text = MainMenu.text(self.animalRatings)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=120, y=270, width=300, height=100)

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
        MainMenu.label(self.seeAnimals, 'Список всех животных зоопарка').place(x=90, y=40, width=250, height=20)
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
        print('ter')
        name_animal = self.choice_animal.get()
        if self.examination(name_animal):  # вызвали функицю класс-метод
            window_animal = tk.Toplevel()
            window_animal.grab_set()
            window_animal.geometry(f'350x300+500+50')
            window_animal['bg'] = '#33ffe6'
            window_animal.title('Animal Information')
            MainMenu.button(window_animal, 'exit', window_animal.destroy).place(x=120, y=370, width=50, height=30)
            MainMenu.button(window_animal, 'delete', window_animal.destroy).place(x=100, y=370, width=60, height=30)
            text = MainMenu.text(window_animal)
            text.place(x=120, y=70, width=300, height=160)
            text.insert('end', f'{self.view_all_animals(name_animal)}')
        else:
            print('xzfg')

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
                tyh = f'Кличка - {anm.nickname}\n' \
                      f'Тип - {anm.typeAnimal}\n' \
                      f'Хищник - {predator}\n' \
                      f'Масса - {anm.weight}\n' \
                      f'Место обитания - {anm.dwells}\n' \
                      f'Климат - {anm.climate}\n' \
                      f'Название животного - {anm.clasAnimal}\n'
                if anm.typeAnimal == 'крылатый':
                    if anm.migratory:
                        migratory = 'да'
                    else:
                        migratory = 'нет'
                    tyh = tyh + f'Миграционный - {migratory}\n'
                return tyh


mainMenu = MainMenu().main
mainMenu.mainloop()