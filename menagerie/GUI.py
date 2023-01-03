import tkinter as tk
from main import Button2_1, Button2_2, Button2_3, Button2_4, Button2_5

class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        # main = tk.Tk()
        # main['bg'] = '#33ffe6'
        # main.geometry(f'240x271+100+200')
        self.button1 = tk.Button(text="1. add an animal", command=self.open_window1)
        self.button2 = tk.Button(text="2. see animals", command=self.open_window2)
        self.button3 = tk.Button(text="3. delete animal", command=self.open_window3)
        self.button4 = tk.Button(text="4. exid", command=self.destroy)

        self.button1.pack(pady=5, ipadx=2, ipady=2)
        self.button2.pack(pady=5, ipadx=2, ipady=2)
        self.button3.pack(pady=5, ipadx=2, ipady=2)
        self.button4.pack(pady=5, ipadx=2, ipady=2)
        # main.mainloop()

    def open_window1(self):
        addingAnimals = AddingAnimals(self)
        addingAnimals.grab_set()

    def open_window2(self):
        seeAnimals = SeeAnimals(self)
        seeAnimals.grab_set()

    def open_window3(self):
        deleteAnimal = DeleteAnimal(self)
        deleteAnimal.grab_set()

############################################################################################################################################

class AddingAnimals(tk.Toplevel):  # добавить животное
    def __init__(self, parent):
        super().__init__(parent)
        self.value = tk.BooleanVar()  # создали переменную и поместили в нее булевское значение, которое будет возвращать наш флажок
        tk.Label(self, text="Выберите подвид животного:").pack()
        tk.Radiobutton(self, text="ground", variable=self.value, value=1, command=self.defines).pack()
        tk.Radiobutton(self, text="underwater", variable=self.value, value=2, command=self.defines).pack()
        tk.Radiobutton(self, text="winged", variable=self.value, value=3, command=self.defines).pack()

        tk.Label(self, text="Укажите среду обитания данного подвида:").pack()
        tk.Radiobutton(self, text="forests", variable=self.value, value=4, command=self.defines).pack()
        tk.Radiobutton(self, text="mountains", variable=self.value, value=5, command=self.defines).pack()
        tk.Radiobutton(self, text="steppes", variable=self.value, value=6, command=self.defines).pack()
        tk.Radiobutton(self, text="rivers", variable=self.value, value=7, command=self.defines).pack()
        tk.Radiobutton(self, text="seas", variable=self.value, value=8, command=self.defines).pack()
        tk.Radiobutton(self, text="ocean", variable=self.value, value=9, command=self.defines).pack()

        tk.Label(self, text="Являются ли миграционным:").pack()
        tk.Radiobutton(self, text="yes", variable=self.value, value=10, command=self.defines).pack()
        tk.Radiobutton(self, text="no", variable=self.value, value=11, command=self.defines).pack()

        tk.Label(self, text="Укажите климатические условия:").pack()
        tk.Radiobutton(self, text="warm", variable=self.value, value=12, command=self.defines).pack()
        tk.Radiobutton(self, text="cold", variable=self.value, value=13, command=self.defines).pack()
        tk.Radiobutton(self, text="moderate", variable=self.value, value=14, command=self.defines).pack()

        tk.Label(self, text="Явлиется ли зверь хищником:").pack()
        tk.Radiobutton(self, text="yes", variable=self.value, value=15, command=self.defines).pack()
        tk.Radiobutton(self, text="no", variable=self.value, value=16, command=self.defines).pack()

        tk.Label(self, text="Какую пищу употребляет:").pack()
        tk.Entry(self, font=('Arial',15)).pack()

        tk.Label(self, text="Укажите вес животного:").pack()
        tk.Entry(self, font=('Arial', 15)).pack()

        tk.Label(self, text="Придумайте кличку для нового жителя зоопарка:").pack()
        tk.Entry(self, font=('Arial', 15)).pack()

        tk.Button(self, text="exit", command=self.destroy).pack()
        tk.Button(self, text="save", command=self.destroy).pack()

        #self.button1_1.pack(pady=5, ipadx=2, ipady=2)

    def defines(self):
        value = self.value.get()
        print(value)

##################################################################################################################################

class SeeAnimals(tk.Toplevel):  # просмотр животных
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Это всплывающее окно 2")
        self.button2_1 = tk.Button(self, text="1. Top 3 Lightest Zoo Creatures", command=self.open_window2_1, justify=tk.LEFT)
        self.button2_2 = tk.Button(self, text="2. Top 5 biggest predators", command=self.open_window2_2, justify=tk.LEFT)
        self.button2_3 = tk.Button(self, text="3. List of herbivore names", command=self.open_window2_3, justify=tk.LEFT)
        self.button2_4 = tk.Button(self, text="4. List of underwater creatures in decreasing order of their weight", command=self.open_window2_4, justify=tk.LEFT)
        self.button2_5 = tk.Button(self, text="5. List of land animals, with each name and location", command=self.open_window2_5, justify=tk.LEFT)
        self.button2_6 = tk.Button(self, text="6. Exit", command=self.destroy)

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

class DeleteAnimal(tk.Toplevel):  # удалить животных
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Это всплывающее окно 3")
        self.button3_1 = tk.Button(self, text="6. Exit", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button3_1.pack(pady=5, ipadx=2, ipady=2)

#########################################################################################################################################3

if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.mainloop()