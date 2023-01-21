import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from main import DataBackend

data = DataBackend()


class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self.geometry(f'430x360+500+50')
        self.title('Zoo')

        self.img = tk.PhotoImage(file='images/zoo.png')
        tk.Label(self, image=self.img).pack()

        self.button(self, 'Add an animal', self.open_window1).place(x=60, y=30, width=300, height=20)
        self.button(self, 'Animal Ratings', self.open_window2).place(x=60, y=60, width=300, height=20)
        self.button(self, 'See Animals', self.open_window3).place(x=60, y=90, width=300, height=20)
        self.button(self, 'Exit', self.exit).place(x=60, y=150, width=300, height=20)

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
        return tk.Text(window, font=('Arial', 13), bg='#a5a29c')

    def open_window1(self):
        adding_animals = AddingAnimals(self)
        adding_animals.grab_set()

    def open_window2(self):
        see_animals = AnimalRatings(self)
        see_animals.grab_set()

    def open_window3(self):
        delete_animal = SeeAnimals(self)
        delete_animal.grab_set()

    def exit(self):
        data.save_info_file()
        self.destroy()


"""Добавление животного"""


class AddingAnimals(tk.Toplevel):  # добавить животное
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Adding animals')
        self['bg'] = '#33ffe6'
        self.geometry(f'460x700+500+50')

        MainMenu.button(self, 'exit', self.exit).place(x=380, y=670, width=70, height=20)
        self.button = MainMenu.button(self, 'save', self.save)
        self.button.config(state='disabled')  # сделали кнопку неактивной
        self.button.place(x=300, y=670, width=70, height=20)

        self.list_animal_type = data.list_animal_type
        self.valueStrSubspecies = tk.StringVar(self, 'esth')  # создали переменную со строковым значением подвид животного, которое будет возвращать наша радиокнопка
        self.valueStrSubspecies.trace("r", self.data_checking)
        self.valueStrHabitat = tk.StringVar(self, 'est')  # аналогично для среды обитания
        self.valueStrHabitat.trace("r", self.data_checking)
        self.valueStrClimate = tk.StringVar(self, 'es')  # для климатических условий
        self.valueStrClimate.trace("r", self.data_checking)
        self.valueBoolIsMigratory = tk.StringVar(self, '1')  # создали переменную с числовым значением - миграция
        self.valueBoolIsPredator = tk.StringVar(self, '2')  # создали переменную с числовым значением - хищник
        self.value_food = tk.StringVar()  # создали переменную для пищи животного
        self.value_food.trace("w", self.data_checking)
        self.value_weight = tk.StringVar()  # создали переменную для веса животного
        self.value_weight.trace("w", self.data_checking)
        self.value_nickname = tk.StringVar()  # создали переменную для клички животного
        self.value_nickname.trace("w", self.data_checking)
        self.value_combo = tk.StringVar()  # создали переменную для клички животного
        self.value_combo.trace("r", self.data_checking)

        self.migratory_boolean = None
        self.predator_boolean = None

        MainMenu.label(self, 'Укажите тип животного:').place(x=10, y=10, width=200, height=20)
        self.combo = ttk.Combobox(self, values=self.list_animal_type, font=('Arial', 10), textvariable=self.value_combo)
        self.combo.place(x=220, y=10, width=230, height=20)

        MainMenu.label(self, 'Выберите подвид животного:').place(x=10, y=40, width=240, height=20)
        MainMenu.radiobutton(self, 'ground', self.valueStrSubspecies).place(x=10, y=70, width=80, height=20)
        MainMenu.radiobutton(self, 'underwater', self.valueStrSubspecies).place(x=10, y=90, width=110, height=20)
        MainMenu.radiobutton(self, 'winged', self.valueStrSubspecies).place(x=10, y=110, width=80, height=20)

        MainMenu.label(self, 'Укажите среду обитания данного подвида:').place(x=10, y=140, width=340, height=20)
        MainMenu.radiobutton(self, 'forests', self.valueStrHabitat).place(x=10, y=170, width=80, height=20)
        MainMenu.radiobutton(self, 'mountains', self.valueStrHabitat).place(x=10, y=190, width=100, height=20)
        MainMenu.radiobutton(self, 'steppes', self.valueStrHabitat).place(x=10, y=210, width=85, height=20)
        MainMenu.radiobutton(self, 'rivers', self.valueStrHabitat).place(x=10, y=230, width=65, height=20)
        MainMenu.radiobutton(self, 'seas', self.valueStrHabitat).place(x=10, y=250, width=60, height=20)
        MainMenu.radiobutton(self, 'ocean', self.valueStrHabitat).place(x=10, y=270, width=70, height=20)

        MainMenu.label(self, 'Являются ли миграционным:').place(x=10, y=300, width=240, height=20)
        MainMenu.radiobutton(self, 'yes', self.valueBoolIsMigratory).place(x=10, y=330, width=55, height=20)
        MainMenu.radiobutton(self, 'no', self.valueBoolIsMigratory).place(x=10, y=350, width=45, height=20)

        MainMenu.label(self, 'Укажите климатические условия:').place(x=10, y=380, width=270, height=20)
        MainMenu.radiobutton(self, 'warm', self.valueStrClimate).place(x=10, y=410, width=70, height=20)
        MainMenu.radiobutton(self, 'cold', self.valueStrClimate).place(x=10, y=430, width=60, height=20)
        MainMenu.radiobutton(self, 'moderate', self.valueStrClimate).place(x=10, y=450, width=95, height=20)

        MainMenu.label(self, 'Явлиется ли зверь хищником:').place(x=10, y=480, width=245, height=20)
        MainMenu.radiobutton(self, 'yes', self.valueBoolIsPredator).place(x=10, y=510, width=55, height=20)
        MainMenu.radiobutton(self, 'no', self.valueBoolIsPredator).place(x=10, y=530, width=45, height=20)

        MainMenu.label(self, 'Какую пищу употребляет:').place(x=10, y=560, width=215, height=20)
        MainMenu.entry(self, self.value_food).place(x=230, y=560, width=220, height=20)

        MainMenu.label(self, 'Укажите вес животного:').place(x=10, y=590, width=195, height=20)
        MainMenu.entry(self, self.value_weight).place(x=230, y=590, width=220, height=20)

        MainMenu.label(self, 'Придумайте кличку для\n нового жителя зоопарка:').place(x=10, y=620, width=195, height=40)
        MainMenu.entry(self, self.value_nickname).place(x=230, y=630, width=220, height=20)

    def data_checking(self, *args):
        type_value = len(self.value_combo.get()) > 1
        subspecies_value = self.valueStrSubspecies.get() != 'esth'
        habitat_value = self.valueStrHabitat.get() != 'est'
        climate_value = self.valueStrClimate.get() != 'es'
        migratory_boolean = self.valueBoolIsMigratory.get() != '1'
        predator_boolean = self.valueBoolIsPredator.get() != '2'
        food_value = len(self.value_food.get()) > 0
        weight_value = len(self.value_weight.get()) > 0
        nickname_value = len(self.value_nickname.get()) > 0
        if type_value and subspecies_value and habitat_value and climate_value and migratory_boolean and predator_boolean and food_value and float(weight_value) and nickname_value:
            self.button.config(state='normal')
        elif self.button["state"] != tk.DISABLED:
            self.button.config(state='disabled')

    def save(self):
        self.migratory_boolean = self.valueBoolIsMigratory.get() == 'yes'
        self.predator_boolean = self.valueBoolIsPredator.get() == 'no'
        print(self.value_nickname.get(), self.valueStrSubspecies.get(), self.predator_boolean, self.value_weight.get(),
              self.valueStrHabitat.get(), self.valueStrClimate.get(), self.combo.get(), self.value_food.get(), self.migratory_boolean)
        data.registration_animal(self.value_nickname.get(), self.valueStrSubspecies.get(), self.predator_boolean, self.value_weight.get(),
              self.valueStrHabitat.get(), self.valueStrClimate.get(), self.combo.get(), self.value_food.get(), self.migratory_boolean)
        self.destroy()

    def exit(self):
        com = mb.askyesno('Attention!', 'If you exit now the animal will not be saved.')
        if com:
            self.destroy()


"""Просмотр рейтингов"""


class AnimalRatings(tk.Toplevel):  # просмотр рейтингов
    def __init__(self, parent):
        super().__init__(parent)
        self['bg'] = '#33ffe6'
        self.geometry(f'430x380+500+50')
        self.title('Animal Ratings')

        self.img = tk.PhotoImage(file='images/zoo2.png')
        tk.Label(self, image=self.img).pack()

        MainMenu.button(self, 'Топ 3 легких существ зоопарка', lambda: self.open_window(1)).place(x=60, y=30, width=300, height=20)
        MainMenu.button(self, 'Топ 5 больших хищников', lambda: self.open_window(2)).place(x=60, y=60, width=300, height=20)
        MainMenu.button(self, 'Сипсок имен травоядных существ', lambda: self.open_window(3)).place(x=60, y=90, width=300, height=20)
        MainMenu.button(self, 'Список подводных существ\n по мере убывания их веса', lambda: self.open_window(4)).place(x=60, y=120, width=300, height=40)
        MainMenu.button(self, 'Список наземных животных с\n именем каджого и местом обитания', lambda: self.open_window(5)).place(x=60, y=170, width=300, height=40)
        MainMenu.button(self, 'Exit', self.destroy).place(x=60, y=350, width=300, height=20)
        self.text = MainMenu.text(self)
        self.text.insert('end', f'Выберите текс')
        self.text.place(x=60, y=230, width=300, height=100)

    def open_window(self, ark):
        self.text.delete('1.0', 'end')  # удалили предыдущий текст в текстовом окне

        if ark == 1:
            list_light_creatures = data.top_3
            for creature in list_light_creatures:  # топ 3 самых легких существа зоопарка
                stroka = creature.nickname + ' ' + creature.clas_animal + ' ' + str(creature.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')  # выводим строку

        elif ark == 2:
            list_big_predator = data.top_5
            for pred in list_big_predator:  # топ 5 самых больших хищников
                stroka = pred.nickname + ' ' + pred.clas_animal + ' ' + str(pred.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')

        elif ark == 3:
            list_herbivorous = data.listHerbivorous
            for herbivorous in list_herbivorous:  # просмотр кличек травоядных существ
                stroka = herbivorous.nickname + ' ' + herbivorous.clas_animal
                self.text.insert('end', f'{stroka}\n')

        elif ark == 4:
            list_under_desc_weight = data.top_7
            for under in list_under_desc_weight:  # просмотр подводных существ по мере убывания их веса
                stroka = under.nickname + ' ' + under.clas_animal + ' ' + str(under.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')

        elif ark == 5:
            list_ground = data.listGround
            for ground in list_ground:  # просмотр наземных животных с кличкой каждого и местом обитания
                stroka = ground.nickname + ' ' + ground.clas_animal + ' ' + str(ground.weight) + ' кг'
                self.text.insert('end', f'{stroka}\n')


"""Просмотр животных"""


class SeeAnimals(tk.Toplevel):  # просмотр
    def __init__(self, parent):
        super().__init__(parent)
        self['bg'] = '#33ffe6'
        self.geometry(f'430x410+500+50')
        self.title('See Animals')
        self.choice_animal = tk.StringVar()  # создали переменную для выбора животного
        self.choice_animal.trace('w', self.combo_box)
        self.typ_animal = str()  # переменная куда бует сохраняться выбранное животное
        self.img = None  # переменная в которой лежит картинка животного
        self.listAnimal = data.listAnimal
        self.list_animal_type = list()  # список с типом животн, который выводится в комбобксе
        self.list_animal_name = list()  # список с именами животных, определенного типа
        for typ in self.listAnimal:
            if typ.clas_animal not in self.list_animal_type:
                self.list_animal_type.append(typ.clas_animal)

        MainMenu.label(self, text='Choose an animal type:').place(x=10, y=10, width=220, height=20)

        self.combo_typ = ttk.Combobox(self, values=self.list_animal_type, textvariable=self.choice_animal)
        self.combo_typ.place(x=240, y=10, width=100, height=20)

        MainMenu.label(self, text='Enter the name of the animal:').place(x=10, y=40, width=220, height=20)

        self.combo_name = ttk.Combobox(self, values=self.list_animal_name)
        self.combo_name.place(x=240, y=40, width=100, height=20)

        self.label = MainMenu.label(self, 'Список всех животных зоопарка')
        self.label.place(x=90, y=70, width=285, height=20)
        MainMenu.button(self, 'exit', self.destroy).place(x=350, y=380, width=70, height=20)
        MainMenu.button(self, 'search', self.selected_animal).place(x=350, y=25, width=70, height=20)
        self.text = MainMenu.text(self)
        for an in self.listAnimal:
            stroka = an.clas_animal + ' - ' + an.nickname
            self.text.insert('end', f'{stroka}\n')
        self.text.place(x=70, y=100, width=300, height=270)

    def combo_box(self, *args):
        for i in self.listAnimal:
            if self.choice_animal.get() == i.clas_animal:
                self.list_animal_name.append(i.nickname)
                print('wd')

    def selected_animal(self):
        self.typ_animal = self.combo_typ.get()
        if self.typ_animal in self.list_animal_type:  # вызвали функицю класс-метод
            if self.label['text'] != 'Список всех животных зоопарка':
                self.label.config(text='Список всех животных зоопарка')

            window_animal = tk.Toplevel()
            window_animal.grab_set()
            window_animal.geometry(f'430x380+500+50')
            window_animal['bg'] = '#33ffe6'
            window_animal.title('Animal Information')

            menu_win_an = tk.Menu(window_animal)  # создали меню
            window_animal.configure(menu=menu_win_an)  # разместили меню
            first_item = tk.Menu(menu_win_an, tearoff=0)  # создали элементы меню
            menu_win_an.add_cascade(label='change', font=('Arial', 13), menu=first_item)  # распалагаем 1-ый пункт меню
            first_item.add_command(label='вес', font=('Arial', 13))
            first_item.add_command(label='пищу', font=('Arial', 13))

            self.img = tk.PhotoImage(file=self.picture_selection())
            tk.Label(window_animal, image=self.img).place(x=150, y=10)
            MainMenu.button(window_animal, 'exit', window_animal.destroy).place(x=350, y=350, width=70, height=20)
            text = MainMenu.text(window_animal)
            text.place(x=70, y=165, width=300, height=175)
            text.insert('end', f'{self.view_all_animals()}')
        else:
            self.label.config(text='Вы указали неверное имя животного')

    # def examination(self):  # проверяем есть ли выбранное животное в общем списке
    #     for name in self.listAnimal:
    #         if name.nickname == self.name_animal:
    #             return True
    #     return False

    def view_all_animals(self):  # выводим информацию о животном
        for anm in self.listAnimal:
            if anm.nickname == self.name_animal:
                if anm.predator:
                    predator = 'да'
                else:
                    predator = 'нет'
                tyh = f'Животное - {anm.clas_animal}\n' \
                      f'Кличка - {anm.nickname}\n' \
                      f'Тип - {anm.type_animal}\n' \
                      f'Хищник - {predator}\n' \
                      f'Масса - {anm.weight}\n' \
                      f'Место обитания - {anm.dwells}\n' \
                      f'Климат - {anm.climate}\n' \
                      f'Употребляемая пища - {anm.food}'
                if anm.type_animal == 'крылатый':
                    if anm.migratory:
                        migratory = 'да'
                    else:
                        migratory = 'нет'
                    tyh = tyh + f'\nМиграционный - {migratory}'
                return tyh

    def picture_selection(self):
        if self.name_animal == 'попугай':
            return 'images/popugay.png'

        elif self.name_animal == 'выдра':
            return 'images/otter.png'

        elif self.name_animal == 'волк':
            return 'images/wolf.png'

        elif self.name_animal == 'заяц':
            return 'images/hare.png'

        elif self.name_animal == 'косуля':
            return 'images/roe.png'

        elif self.name_animal == 'бизон':
            return 'images/buffalo.png'

        elif self.name_animal == 'страус':
            return 'images/ostrich.png'

        elif self.name_animal == 'дельфин':
            return 'images/dolphin.png'

        elif self.name_animal == 'тигр':
            return 'images/tiger.png'

        elif self.name_animal == 'осьминог':
            return 'images/octopus.png'

        elif self.name_animal == 'журавль':
            return 'images/crane.png'

        elif self.name_animal == 'щука':
            return 'images/pike.png'

        elif self.name_animal == 'зебра':
            return 'images/zebra.png'

        elif self.name_animal == 'голубь':
            return 'images/pigeon.png'
