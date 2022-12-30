import tkinter as tk

class MainMenu(tk.Tk):  # главное меню
    def __init__(self):
        super().__init__()
        self.btn1 = tk.Button(self, text="1. add an animal", command=self.open_window1)
        self.btn2 = tk.Button(self, text="2. see animals", command=self.open_window2)
        self.btn3 = tk.Button(self, text="3. delete animal", command=self.open_window3)
        self.btn4 = tk.Button(self, text="3. exid", command=self.destroy)
        self.btn1.pack(padx=50, pady=20)
        self.btn2.pack(padx=50, pady=20)
        self.btn3.pack(padx=50, pady=20)
        self.btn4.pack(padx=50, pady=20)

    def open_window1(self):
        about = AddingAnimals(self)
        about.grab_set()

    def open_window2(self):
        about = SeeAnimals(self)
        about.grab_set()

    def open_window3(self):
        about = DeleteAnimal(self)
        about.grab_set()
class AddingAnimals(tk.Toplevel):
    pass
class SeeAnimals(tk.Toplevel):  # просмотр животных
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Это всплывающее окно")
        self.button2_1 = tk.Button(self, text="1. Top 3 Lightest Zoo Creatures", command=self.destroy)
        self.button2_2 = tk.Button(self, text="2. Top 5 biggest predators", command=self.destroy)
        self.button2_3 = tk.Button(self, text="3. List of herbivore names", command=self.destroy)
        self.button2_4 = tk.Button(self, text="4. List of underwater creatures in decreasing order of their weight", command=self.destroy)
        self.button2_5 = tk.Button(self, text="5. List of land animals, with each name and location", command=self.destroy)
        self.button2_6 = tk.Button(self, text="6. Exit", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)
        self.button2_2.pack(pady=5, ipadx=2, ipady=2)
        self.button2_3.pack(pady=5, ipadx=2, ipady=2)
        self.button2_4.pack(pady=5, ipadx=2, ipady=2)
        self.button2_5.pack(pady=5, ipadx=2, ipady=2)
        self.button2_6.pack(pady=5, ipadx=2, ipady=2)

class DeleteAnimal(tk.Toplevel):  # удалить животных
    pass

if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.mainloop()