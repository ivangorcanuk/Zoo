import tkinter as tk
from main import Button2_1, Button2_2, Button2_3, Button2_4, Button2_5

class MainMenu:  # главное меню
    def __init__(self):
        self.main = tk.Tk()
        self.main['bg'] = '#33ffe6'
        self.main.geometry(f'240x271+100+200')
        tk.Button(self.main, text="1. add an animal", font=('Arial', 13), command=self.open_window1).grid(row=1, column=0, sticky='wens', padx=50, pady=2)
        tk.Button(self.main, text="2. see animals", font=('Arial', 13), command=self.open_window2).grid(row=2, column=0, sticky='wens', padx=50, pady=2)
        tk.Button(self.main, text="3. delete animal", font=('Arial', 13), command=self.open_window3).grid(row=3, column=0, sticky='wens', padx=50, pady=2)
        tk.Button(self.main, text="4. exid", font=('Arial', 13), command=self.main.destroy).grid(row=4, column=0, sticky='wens', padx=50, pady=2)

    def open_window1(self):
        addingAnimals = AddingAnimals()

    def open_window2(self):
        seeAnimals = SeeAnimals()

    def open_window3(self):
        deleteAnimal = DeleteAnimal()

############################################################################################################################################

class AddingAnimals:  # добавить животное
    def __init__(self):
        self.addingAnimals = tk.Tk()
        self.addingAnimals.grab_set()
        # self.addingAnimals['bg'] = '#33ffe6'
        self.addingAnimals.geometry(f'500x700+500+50')
        self.valueStrSubspecies = tk.StringVar()  # создали переменную и поместили в нее строковое значение, которое будет возвращать наш флажок подвид животного
        self.valueStrSubspecies.set('gnd')
        self.valueStrHabitat = tk.StringVar()  # для среды обитания
        self.valueStrHabitat.set('ert')
        self.valueStrClimate = tk.StringVar()  # для климатических условий
        self.valueStrClimate.set('erte')
        self.valueBoolIsMigratory = tk.BooleanVar()  # создали переменную и поместили в нее булевское значение, которое будет возвращать наш флажок
        self.valueBoolIsPredator = tk.BooleanVar()
        tk.Label(self.addingAnimals, text="Выберите подвид животного:", font=('Arial', 13)).grid(row=0, columnspan=3)
        tk.Radiobutton(self.addingAnimals, text="ground", font=('Arial', 13), variable=self.valueStrSubspecies, value="ground", command=self.defineSubspecies).grid(row=1, column=0)
        tk.Radiobutton(self.addingAnimals, text="underwater", font=('Arial', 13), variable=self.valueStrSubspecies, value="underwater", command=self.defineSubspecies).grid(row=1, column=1)
        tk.Radiobutton(self.addingAnimals, text="winged", font=('Arial', 13), variable=self.valueStrSubspecies, value="winged", command=self.defineSubspecies).grid(row=1, column=2)

        tk.Label(self.addingAnimals, text="Укажите среду обитания данного подвида:", font=('Arial', 13)).grid(row=2, columnspan=3)
        tk.Radiobutton(self.addingAnimals, text="forests", font=('Arial', 13), variable=self.valueStrHabitat, value="forests", command=self.definesHabitat).grid(row=3, column=0)
        tk.Radiobutton(self.addingAnimals, text="mountains", font=('Arial', 13), variable=self.valueStrHabitat, value="mountains", command=self.definesHabitat).grid(row=4, column=0)
        tk.Radiobutton(self.addingAnimals, text="steppes", font=('Arial', 13), variable=self.valueStrHabitat, value="steppes", command=self.definesHabitat).grid(row=3, column=1)
        tk.Radiobutton(self.addingAnimals, text="rivers", font=('Arial', 13), variable=self.valueStrHabitat, value="rivers", command=self.definesHabitat).grid(row=4, column=1)
        tk.Radiobutton(self.addingAnimals, text="seas", font=('Arial', 13), variable=self.valueStrHabitat, value="seas", command=self.definesHabitat).grid(row=3, column=2)
        tk.Radiobutton(self.addingAnimals, text="ocean", font=('Arial', 13), variable=self.valueStrHabitat, value="ocean", command=self.definesHabitat).grid(row=4, column=2)

        tk.Label(self.addingAnimals, text="Являются ли миграционным:", font=('Arial', 13)).grid(row=5, columnspan=3)
        tk.Radiobutton(self.addingAnimals, text="yes", font=('Arial', 13), variable=self.valueBoolIsMigratory, value=True, command=self.isMigratory).grid(row=6, column=0)
        tk.Radiobutton(self.addingAnimals, text="no", font=('Arial', 13), variable=self.valueBoolIsMigratory, value=False, command=self.isMigratory).grid(row=6, column=1)

        tk.Label(self.addingAnimals, text="Укажите климатические условия:", font=('Arial', 13)).grid(row=7, columnspan=3)
        tk.Radiobutton(self.addingAnimals, text="warm", font=('Arial', 13), variable=self.valueStrClimate, value='warm', command=self.definesClimate).grid(row=8, column=0)
        tk.Radiobutton(self.addingAnimals, text="cold", font=('Arial', 13), variable=self.valueStrClimate, value='cold', command=self.definesClimate).grid(row=8, column=1)
        tk.Radiobutton(self.addingAnimals, text="moderate", font=('Arial', 13), variable=self.valueStrClimate, value='moderate', command=self.definesClimate).grid(row=8, column=2)

        tk.Label(self.addingAnimals, text="Явлиется ли зверь хищником:", font=('Arial', 13)).grid(row=9, columnspan=3)
        tk.Radiobutton(self.addingAnimals, text="yes", font=('Arial', 13), variable=self.valueBoolIsPredator, value=True, command=self.isPredator).grid(row=10, column=0)
        tk.Radiobutton(self.addingAnimals, text="no", font=('Arial', 13), variable=self.valueBoolIsPredator, value=False, command=self.isPredator).grid(row=10, column=1)

        tk.Label(self.addingAnimals, text="Какую пищу употребляет:", font=('Arial', 13)).grid(row=11, columnspan=3)
        tk.Entry(self.addingAnimals, font=('Arial', 10)).grid(row=12)

        tk.Label(self.addingAnimals, text="Укажите вес животного:", font=('Arial', 13)).grid(row=13, columnspan=3)
        tk.Entry(self.addingAnimals, font=('Arial', 10)).grid(row=14)

        tk.Label(self.addingAnimals, text="Придумайте кличку для нового жителя зоопарка:", font=('Arial', 13)).grid(row=15, columnspan=3)
        tk.Entry(self.addingAnimals, font=('Arial', 10)).grid(row=16)

        tk.Button(self.addingAnimals, text="exit", font=('Arial', 13), command=self.addingAnimals.destroy).grid(row=17, column=0)
        tk.Button(self.addingAnimals, text="save", font=('Arial', 13), command=self.addingAnimals.destroy).grid(row=17, column=2)

    def defineSubspecies(self):  # определяет подвид животного
        value = self.valueStrSubspecies.get()
        print(value)

    def definesHabitat(self):  # определяет среду обитания животного
        value = self.valueStrHabitat.get()
        print(value)

    def isMigratory(self):  # Явлиется ли зверь хищником
        value = self.valueBoolIsMigratory.get()
        print(value)

    def definesClimate(self):  # определяет климатические условия
        value = self.valueStrClimate.get()
        print(value)

    def isPredator(self):  # Явлиется ли зверь хищником
        value = self.valueBoolIsPredator.get()
        print(value)

##################################################################################################################################

class SeeAnimals:  # просмотр животных
    def __init__(self):
        self.seeAnimals = tk.Toplevel()
        self.seeAnimals.grab_set()
        self.seeAnimals['bg'] = '#33ffe6'
        self.seeAnimals.geometry(f'500x700+500+50')
        self.label = tk.Label(self.seeAnimals, text="Это всплывающее окно 2").grid(row=0)
        tk.Button(self.seeAnimals, text="1. Top 3 Lightest Zoo Creatures", font=('Arial', 13), command=self.open_window2_1).grid(row=1)
        tk.Button(self.seeAnimals, text="2. Top 5 biggest predators", font=('Arial', 13), command=self.open_window2_2).grid(row=2)
        tk.Button(self.seeAnimals, text="3. List of herbivore names", font=('Arial', 13), command=self.open_window2_3).grid(row=3)
        tk.Button(self.seeAnimals, text="4. List of underwater creatures in decreasing order of their weight", font=('Arial', 13), command=self.open_window2_4).grid(row=4)
        tk.Button(self.seeAnimals, text="5. List of land animals, with each name and location", font=('Arial', 13), command=self.open_window2_5).grid(row=5)
        tk.Button(self.seeAnimals, text="6. Exit", font=('Arial', 13), command=self.seeAnimals.destroy).grid(row=6)

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