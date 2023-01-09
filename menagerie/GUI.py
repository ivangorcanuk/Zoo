import tkinter as tk
from main import Button2_1, Button2_2, Button2_3, Button2_4, Button2_5

class MainMenu:  # главное меню
    def __init__(self):
        self.main = tk.Tk()
        self.main['bg'] = '#33ffe6'
        self.main.geometry(f'240x271+100+200')
        self.main.title('Zoo')
        tk.Button(self.main, text="Add an animal", font=('Arial', 13), command=self.open_window1).grid(row=1, column=0, sticky='wens', padx=50, pady=2)
        tk.Button(self.main, text="See animals", font=('Arial', 13), command=self.open_window2).grid(row=2, column=0, sticky='wens', padx=50, pady=2)
        tk.Button(self.main, text="Delete animal", font=('Arial', 13), command=self.open_window3).grid(row=3, column=0, sticky='wens', padx=50, pady=2)
        tk.Button(self.main, text="Exid", font=('Arial', 13), command=self.main.destroy).grid(row=4, column=0, sticky='wens', padx=50, pady=2)

    def open_window1(self):
        addingAnimals = AddingAnimals()

    def open_window2(self):
        seeAnimals = SeeAnimals()

    def open_window3(self):
        deleteAnimal = DeleteAnimal()

############################################################################################################################################

class AddingAnimals:  # добавить животное
    def __init__(self):
        self.addingAnimals = tk.Toplevel()
        self.addingAnimals.grab_set()
        self.addingAnimals.title('Adding animals')
        # self.addingAnimals['bg'] = '#33ffe6'
        self.addingAnimals.geometry(f'500x600+500+50')
        self.valueStrSubspecies = tk.StringVar()  # создали переменную со строковым значением подвид животного, которое будет возвращать наша радиокнопка
        self.valueStrSubspecies.set('esth')
        self.valueStrHabitat = tk.StringVar()  # аналогично для среды обитания
        self.valueStrHabitat.set('est')
        self.valueStrClimate = tk.StringVar()  # для климатических условий
        self.valueStrClimate.set('es')
        self.valueBoolIsMigratory = tk.StringVar()  # создали переменную с числовым значением - миграция
        self.valueBoolIsMigratory.set('2')
        self.valueBoolIsPredator = tk.StringVar()  # создали переменную с числовым значением - хищник
        self.valueBoolIsPredator.set('1')
        self.value_food = tk.StringVar()  # создали переменную для пищи животного
        self.value_weight = tk.StringVar()  # создали переменную для веса животного
        self.value_nickname = tk.StringVar()  # создали переменную для клички животного

        self.label('Выберите подвид животного:').grid(row=0, columnspan=3, )
        self.radiobutton('ground', self.valueStrSubspecies).grid(row=1, column=0)
        self.radiobutton('underwater', self.valueStrSubspecies).grid(row=1, column=1)
        self.radiobutton('winged', self.valueStrSubspecies).grid(row=1, column=2)

        self.label('Укажите среду обитания данного подвида:').grid(row=2, columnspan=3)
        self.radiobutton('forests', self.valueStrHabitat).grid(row=3, column=0)
        self.radiobutton('mountains', self.valueStrHabitat).grid(row=4, column=0)
        self.radiobutton('steppes', self.valueStrHabitat).grid(row=3, column=1)
        self.radiobutton('rivers', self.valueStrHabitat).grid(row=4, column=1)
        self.radiobutton('seas', self.valueStrHabitat).grid(row=3, column=2)
        self.radiobutton('ocean', self.valueStrHabitat).grid(row=4, column=2)

        self.label('Являются ли миграционным:').grid(row=5, columnspan=3)
        self.radiobutton('yes', self.valueBoolIsMigratory).grid(row=6, column=0)
        self.radiobutton('no', self.valueBoolIsMigratory).grid(row=6, column=1)

        self.label('Укажите климатические условия:').grid(row=7, columnspan=3)
        self.radiobutton('warm', self.valueStrClimate).grid(row=8, column=0)
        self.radiobutton('cold', self.valueStrClimate).grid(row=8, column=1)
        self.radiobutton('moderate', self.valueStrClimate).grid(row=8, column=2)

        self.label('Явлиется ли зверь хищником:').grid(row=9, columnspan=3)
        self.radiobutton('yes', self.valueBoolIsPredator).grid(row=10, column=0)
        self.radiobutton('no', self.valueBoolIsPredator).grid(row=10, column=1)

        self.label('Какую пищу употребляет:').grid(row=11, columnspan=3)
        self.entry(self.value_food).grid(row=12)

        self.label('Укажите вес животного:').grid(row=13, columnspan=3)
        self.entry(self.value_weight).grid(row=14)

        self.label('Придумайте кличку для нового жителя зоопарка:').grid(row=15, columnspan=3)
        self.entry(self.value_nickname).grid(row=16)

        tk.Button(self.addingAnimals, text="exit", font=('Arial', 13), command=self.addingAnimals.destroy).grid(row=17, column=0)
        tk.Button(self.addingAnimals, text="save", font=('Arial', 13), command=self.save).grid(row=17, column=2)

    def radiobutton(self, value, variable):
        return tk.Radiobutton(self.addingAnimals, text=value, font=('Arial', 13), variable=variable, value=value)

    def label(self, text):
        return tk.Label(self.addingAnimals, text=text, font=('Arial', 13))

    def entry(self, variable):
        return tk.Entry(self.addingAnimals, font=('Arial', 10), textvariable=variable)

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

##################################################################################################################################

class SeeAnimals:  # просмотр животных
    def __init__(self):
        self.seeAnimals = tk.Toplevel()
        self.seeAnimals.grab_set()
        self.seeAnimals['bg'] = '#33ffe6'
        self.seeAnimals.geometry(f'550x300+500+50')
        self.seeAnimals.title('See animals')
        tk.Button(self.seeAnimals, text="Top 3 Lightest Zoo Creatures", font=('Arial', 13), command=self.open_window2_1).grid(row=1, padx=30, pady=2)
        tk.Button(self.seeAnimals, text="Top 5 biggest predators", font=('Arial', 13), command=self.open_window2_2).grid(row=2, padx=30, pady=2)
        tk.Button(self.seeAnimals, text="List of herbivore names", font=('Arial', 13), command=self.open_window2_3).grid(row=3, padx=30, pady=2)
        tk.Button(self.seeAnimals, text="List of underwater creatures in decreasing order of their weight", font=('Arial', 13), command=self.open_window2_4).grid(row=4, padx=30, pady=2)
        tk.Button(self.seeAnimals, text="List of land animals, with each name and location", font=('Arial', 13), command=self.open_window2_5).grid(row=5, padx=30, pady=2)
        tk.Button(self.seeAnimals, text="Exit", font=('Arial', 13), command=self.seeAnimals.destroy).grid(row=6, padx=30, pady=2)

    def open_window2_1(self):
        button2_1 = Button2_1()

    def open_window2_2(self):
        button2_2 = Button2_2()

    def open_window2_3(self):
        button2_3 = Button2_3()

    def open_window2_4(self):
        button2_4 = Button2_4()

    def open_window2_5(self):
        button2_5 = Button2_5()

##########################################################################################################################################

class DeleteAnimal:  # удалить животных
    def __init__(self):
        self.deleteAnimal = tk.Toplevel()
        self.deleteAnimal.grab_set()
        self.deleteAnimal['bg'] = '#33ffe6'
        self.deleteAnimal.geometry(f'240x271+100+200')
        self.label = tk.Label(self.deleteAnimal, text="Это всплывающее окно 3")
        self.button3_1 = tk.Button(self.deleteAnimal, text="6. Exit", command=self.deleteAnimal.destroy)

        self.label.pack(padx=20, pady=20)
        self.button3_1.pack(pady=5, ipadx=2, ipady=2)

#########################################################################################################################################3

mainMenu = MainMenu().main
mainMenu.mainloop()