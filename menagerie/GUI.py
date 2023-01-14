import tkinter as tk
from main import Data

class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self['bg'] = '#33ffe6'
        self.geometry(f'430x380+500+50')
        self.title('Zoo')

        self.button(self, 'Add an animal', self.open_window1).place(x=60, y=30, width=300, height=20)
        self.button(self, 'Animal Ratings', self.open_window2).place(x=60, y=60, width=300, height=20)
        self.button(self, 'See Animals', self.open_window3).place(x=60, y=90, width=300, height=20)
        self.button(self, 'Exit', self.destroy).place(x=60, y=150, width=300, height=20)

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
        addingAnimals = AddingAnimals(self)
        addingAnimals.grab_set()

    def open_window2(self):
        seeAnimals = AnimalRatings(self)
        seeAnimals.grab_set()

    def open_window3(self):
        deleteAnimal = SeeAnimals(self)
        deleteAnimal.grab_set()

"""Добавление животного"""

class AddingAnimals(tk.Toplevel):  # добавить животное
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Adding animals')
        self['bg'] = '#33ffe6'
        self.geometry(f'460x670+500+50')
        self.valueStrSubspecies = tk.StringVar(self, 'esth')  # создали переменную со строковым значением подвид животного, которое будет возвращать наша радиокнопка
        self.valueStrHabitat = tk.StringVar(self, 'est')  # аналогично для среды обитания
        self.valueStrClimate = tk.StringVar(self, 'es')  # для климатических условий
        self.valueBoolIsMigratory = tk.StringVar(self, '1')  # создали переменную с числовым значением - миграция
        self.valueBoolIsPredator = tk.StringVar(self, '2')  # создали переменную с числовым значением - хищник
        self.value_food = tk.StringVar()  # создали переменную для пищи животного
        self.value_weight = tk.StringVar()  # создали переменную для веса животного
        self.value_nickname = tk.StringVar()  # создали переменную для клички животного

        MainMenu.label(self, 'Выберите подвид животного:').place(x=10, y=10, width=240, height=20)
        MainMenu.radiobutton(self, 'ground', self.valueStrSubspecies).place(x=10, y=40, width=80, height=20)
        MainMenu.radiobutton(self, 'underwater', self.valueStrSubspecies).place(x=10, y=60, width=110, height=20)
        MainMenu.radiobutton(self, 'winged', self.valueStrSubspecies).place(x=10, y=80, width=80, height=20)

        MainMenu.label(self, 'Укажите среду обитания данного подвида:').place(x=10, y=110, width=340, height=20)
        MainMenu.radiobutton(self, 'forests', self.valueStrHabitat).place(x=10, y=140, width=80, height=20)
        MainMenu.radiobutton(self, 'mountains', self.valueStrHabitat).place(x=10, y=160, width=100, height=20)
        MainMenu.radiobutton(self, 'steppes', self.valueStrHabitat).place(x=10, y=180, width=85, height=20)
        MainMenu.radiobutton(self, 'rivers', self.valueStrHabitat).place(x=10, y=200, width=65, height=20)
        MainMenu.radiobutton(self, 'seas', self.valueStrHabitat).place(x=10, y=220, width=60, height=20)
        MainMenu.radiobutton(self, 'ocean', self.valueStrHabitat).place(x=10, y=240, width=70, height=20)

        MainMenu.label(self, 'Являются ли миграционным:').place(x=10, y=270, width=240, height=20)
        MainMenu.radiobutton(self, 'yes', self.valueBoolIsMigratory).place(x=10, y=300, width=55, height=20)
        MainMenu.radiobutton(self, 'no', self.valueBoolIsMigratory).place(x=10, y=320, width=45, height=20)

        MainMenu.label(self, 'Укажите климатические условия:').place(x=10, y=350, width=270, height=20)
        MainMenu.radiobutton(self, 'warm', self.valueStrClimate).place(x=10, y=380, width=70, height=20)
        MainMenu.radiobutton(self, 'cold', self.valueStrClimate).place(x=10, y=400, width=60, height=20)
        MainMenu.radiobutton(self, 'moderate', self.valueStrClimate).place(x=10, y=420, width=95, height=20)

        MainMenu.label(self, 'Явлиется ли зверь хищником:').place(x=10, y=450, width=245, height=20)
        MainMenu.radiobutton(self, 'yes', self.valueBoolIsPredator).place(x=10, y=480, width=55, height=20)
        MainMenu.radiobutton(self, 'no', self.valueBoolIsPredator).place(x=10, y=500, width=45, height=20)

        MainMenu.label(self, 'Какую пищу употребляет:').place(x=10, y=530, width=215, height=20)
        MainMenu.entry(self, self.value_food).place(x=230, y=530, width=220, height=20)

        MainMenu.label(self, 'Укажите вес животного:').place(x=10, y=560, width=195, height=20)
        MainMenu.entry(self, self.value_weight).place(x=230, y=560, width=220, height=20)

        MainMenu.label(self, 'Придумайте кличку для\n нового жителя зоопарка:').place(x=10, y=590, width=195, height=40)
        MainMenu.entry(self, self.value_nickname).place(x=230, y=600, width=220, height=20)

        MainMenu.button(self, 'exit', self.destroy).place(x=380, y=640, width=70, height=20)
        MainMenu.button(self, 'save', self.save).place(x=300, y=640, width=70, height=20)

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
        self.destroy()

"""Просмотр рейтингов"""

class AnimalRatings(tk.Toplevel):  # просмотр животных
    def __init__(self, parent):
        super().__init__(parent)
        self['bg'] = '#33ffe6'
        self.geometry(f'430x380+500+50')
        self.title('Animal Ratings')

        MainMenu.button(self, 'Top 3 Lightest Zoo Creatures', lambda: self.open_window(1)).place(x=60, y=30, width=300, height=20)
        MainMenu.button(self, 'Top 5 biggest predators', lambda: self.open_window(2)).place(x=60, y=60, width=300, height=20)
        MainMenu.button(self, 'List of herbivore names', lambda: self.open_window(3)).place(x=60, y=90, width=300, height=20)
        MainMenu.button(self, 'List of underwater creatures\n in decreasing order of their weight', lambda: self.open_window(4)).place(x=60, y=120, width=300, height=40)
        MainMenu.button(self, 'List of land animals,\n with each name and location', lambda: self.open_window(5)).place(x=60, y=170, width=300, height=40)
        MainMenu.button(self, 'Exit', self.destroy).place(x=60, y=350, width=300, height=20)
        self.text = MainMenu.text(self)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=60, y=230, width=300, height=100)

    def open_window(self, ark):
        self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне

        if ark == 1:
            list_light_creatures = Data().top_3
            for creature in list_light_creatures:  # топ 3 самых легких существа зоопарка
                stroka = creature.nickname + ' ' + creature.clasAnimal + ' ' + str(creature.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')  # выводим строку

        elif ark == 2:
            list_big_predator = Data().top_5
            for pred in list_big_predator:  # топ 5 самых больших хищников
                stroka = pred.nickname + ' ' + pred.clasAnimal + ' ' + str(pred.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')

        elif ark == 3:
            list_herbivorous = Data().listHerbivorous
            for herbivorous in list_herbivorous:  # просмотр кличек травоядных существ
                stroka = herbivorous.nickname + ' ' + herbivorous.clasAnimal
                self.text.insert('end', f'{stroka}\n')

        elif ark == 4:
            list_under_desc_weight = Data().top_7
            for under in list_under_desc_weight:  # просмотр подводных существ по мере убывания их веса
                stroka = under.nickname + ' ' + under.clasAnimal + ' ' + str(under.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')

        elif ark == 5:
            list_ground = Data().listGround
            for ground in list_ground:  # просмотр наземных животных с кличкой каждого и местом обитания
                stroka = ground.nickname + ' ' + ground.clasAnimal + ' ' + str(ground.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')

"""Просмотр животных"""

class SeeAnimals(tk.Toplevel):  # просмотр
    def __init__(self, parent):
        super().__init__(parent)
        self['bg'] = '#33ffe6'
        self.geometry(f'430x380+500+50')
        self.title('See Animals')
        self.choice_animal = tk.StringVar()  # создали переменную для выбора животного

        MainMenu.label(self, text='Enter the name of the animal:').place(x=10, y=10, width=220, height=20)
        MainMenu.entry(self, self.choice_animal).place(x=240, y=10, width=100, height=20)
        self.label = MainMenu.label(self, 'Список всех животных зоопарка')
        self.label.place(x=90, y=40, width=285, height=20)
        MainMenu.button(self, 'exit', self.destroy).place(x=350, y=350, width=70, height=20)
        MainMenu.button(self, 'search', self.selected_animal).place(x=350, y=10, width=70, height=20)
        self.text = MainMenu.text(self)
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

