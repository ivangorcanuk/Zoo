import tkinter as tk
from main import Button2_1, Button2_2, Button2_3, Button2_4, Button2_5

class MainMenu:  # главное меню
    def __init__(self):
        #super().__init__()
        self.main = tk.Tk()
        self.main['bg'] = '#33ffe6'
        self.main.geometry(f'240x271+100+200')
        tk.Button(self.main, text="1. add an animal", command=self.open_window1).pack(pady=5, ipadx=2, ipady=2)
        tk.Button(self.main, text="2. see animals", command=self.open_window2).pack(pady=5, ipadx=2, ipady=2)
        tk.Button(self.main, text="3. delete animal", command=self.open_window3).pack(pady=5, ipadx=2, ipady=2)
        tk.Button(self.main, text="4. exid", command=self.main.destroy).pack(pady=5, ipadx=2, ipady=2)

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
        self.value = tk.BooleanVar()  # создали переменную и поместили в нее булевское значение, которое будет возвращать наш флажок
        tk.Label(self.addingAnimals, text="Выберите подвид животного:", font=('Arial', 10)).pack()
        tk.Radiobutton(self.addingAnimals, text="ground", variable=self.value, value=1, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="underwater", variable=self.value, value=2, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="winged", variable=self.value, value=3, command=self.defines).pack()

        tk.Label(self.addingAnimals, text="Укажите среду обитания данного подвида:").pack()
        tk.Radiobutton(self.addingAnimals, text="forests", variable=self.value, value=4, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="mountains", variable=self.value, value=5, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="steppes", variable=self.value, value=6, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="rivers", variable=self.value, value=7, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="seas", variable=self.value, value=8, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="ocean", variable=self.value, value=9, command=self.defines).pack()

        tk.Label(self.addingAnimals, text="Являются ли миграционным:").pack()
        tk.Radiobutton(self.addingAnimals, text="yes", variable=self.value, value=10, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="no", variable=self.value, value=11, command=self.defines).pack()

        tk.Label(self.addingAnimals, text="Укажите климатические условия:").pack()
        tk.Radiobutton(self.addingAnimals, text="warm", variable=self.value, value=12, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="cold", variable=self.value, value=13, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="moderate", variable=self.value, value=14, command=self.defines).pack()

        tk.Label(self.addingAnimals, text="Явлиется ли зверь хищником:").pack()
        tk.Radiobutton(self.addingAnimals, text="yes", variable=self.value, value=15, command=self.defines).pack()
        tk.Radiobutton(self.addingAnimals, text="no", variable=self.value, value=16, command=self.defines).pack()

        tk.Label(self.addingAnimals, text="Какую пищу употребляет:").pack()
        tk.Entry(self.addingAnimals, font=('Arial',10)).pack()

        tk.Label(self.addingAnimals, text="Укажите вес животного:").pack()
        tk.Entry(self.addingAnimals, font=('Arial', 10)).pack()

        tk.Label(self.addingAnimals, text="Придумайте кличку для нового жителя зоопарка:").pack()
        tk.Entry(self.addingAnimals, font=('Arial', 10)).pack()

        tk.Button(self.addingAnimals, text="exit", command=self.addingAnimals.destroy).pack()
        tk.Button(self.addingAnimals, text="save", command=self.addingAnimals.destroy).pack()

        #self.button1_1.pack(pady=5, ipadx=2, ipady=2)

    def defines(self):
        value = self.value.get()
        print(value)

##################################################################################################################################

class SeeAnimals:  # просмотр животных
    def __init__(self):
        self.seeAnimals = tk.Toplevel()
        self.seeAnimals.grab_set()
        self.label = tk.Label(self.seeAnimals, text="Это всплывающее окно 2")
        self.button2_1 = tk.Button(self.seeAnimals, text="1. Top 3 Lightest Zoo Creatures", command=self.open_window2_1, justify=tk.LEFT)
        self.button2_2 = tk.Button(self.seeAnimals, text="2. Top 5 biggest predators", command=self.open_window2_2, justify=tk.LEFT)
        self.button2_3 = tk.Button(self.seeAnimals, text="3. List of herbivore names", command=self.open_window2_3, justify=tk.LEFT)
        self.button2_4 = tk.Button(self.seeAnimals, text="4. List of underwater creatures in decreasing order of their weight", command=self.open_window2_4, justify=tk.LEFT)
        self.button2_5 = tk.Button(self.seeAnimals, text="5. List of land animals, with each name and location", command=self.open_window2_5, justify=tk.LEFT)
        self.button2_6 = tk.Button(self.seeAnimals, text="6. Exit", command=self.seeAnimals.destroy)

        self.label.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)
        self.button2_2.pack(pady=5, ipadx=2, ipady=2)
        self.button2_3.pack(pady=5, ipadx=2, ipady=2)
        self.button2_4.pack(pady=5, ipadx=2, ipady=2)
        self.button2_5.pack(pady=5, ipadx=2, ipady=2)
        self.button2_6.pack(pady=5, ipadx=2, ipady=2)

    def open_window2_1(self):
        button2_1 = Button2_1(self)
        button2_1.grab_set()

    def open_window2_2(self):
        button2_2 = Button2_2(self)
        button2_2.grab_set()

    def open_window2_3(self):
        button2_3 = Button2_3(self)
        button2_3.grab_set()

    def open_window2_4(self):
        button2_4 = Button2_4(self)
        button2_4.grab_set()

    def open_window2_5(self):
        button2_5 = Button2_5(self)
        button2_5.grab_set()

##########################################################################################################################################

class DeleteAnimal:  # удалить животных
    def __init__(self):
        self.deleteAnimal = tk.Toplevel()
        #self.trye.grab_set()
        self.label = tk.Label(self.deleteAnimal, text="Это всплывающее окно 3")
        #self.button3_1 = tk.Button(self.trye, text="6. Exit", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        #self.button3_1.pack(pady=5, ipadx=2, ipady=2)

#########################################################################################################################################3

mainMenu = MainMenu().main
mainMenu.mainloop()