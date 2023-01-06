import tkinter as tk
from working_files import WorkingMethods, WorkingFiles

"""Данные"""

class Data:
    def __init__(self):
        self.listAnimal = WorkingFiles().reading()  # создаем основной список с животными зоопарка
        self.clasMetod = WorkingMethods()
        self.listPredator = self.clasMetod.animal_sorting_tupe(True, self.listAnimal)  # создаем список с хищными животными
        self.listHerbivorous = self.clasMetod.animal_sorting_tupe(False, self.listAnimal)  # создаем список с травоядными животными
        self.listGround = self.clasMetod.animal_sorting_clas('наземный', self.listAnimal)  # создаем список с наземными животными
        self.listUnderwater = self.clasMetod.animal_sorting_clas('подводный', self.listAnimal)  # создаем список с подводными животными
        self.listWinged = self.clasMetod.animal_sorting_clas('крылатый', self.listAnimal)  # создаем список с крылатыми животными

"""Добавление животного"""

"""Просмотр животных"""

class Button2_1:  # топ 3 самых легких существа зоопарка
    def __init__(self):
        self.window2_1 = tk.Toplevel()
        self.window2_1.grab_set()
        self.window2_1['bg'] = '#33ffe6'
        self.window2_1.geometry(f'500x500+500+50')
        tk.Label(self.window2_1, text="топ 3 самых легких существа зоопарка", font=('Arial', 13)).pack(anchor='n')
        self.text = tk.Text(self.window2_1, font=('Arial', 13), bg='blue')
        self.text.place(x=60, y=60, width=300, height=100)
        WorkingMethods().view_lungs_animal(self.text, Data().listAnimal)  # вызывали метод из файла WorkingMethods
        tk.Button(self.window2_1, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_1.destroy).pack(expand=True)

class Button2_2:  # топ 5 самых больших хищников
    def __init__(self):
        self.window2_2 = tk.Toplevel()
        self.window2_2.grab_set()
        self.window2_2['bg'] = '#33ffe6'
        self.window2_2.geometry(f'500x500+500+50')
        tk.Label(self.window2_2, text="топ 5 самых больших хищников", font=('Arial', 13)).pack(anchor='n')
        self.text = tk.Text(self.window2_2, font=('Arial', 13), bg='blue')
        self.text.place(x=60, y=60, width=300, height=100)
        WorkingMethods().viewing_large_animal(self.text, Data().listPredator)  # вызывали метод из файла WorkingMethods
        tk.Button(self.window2_2, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_2.destroy).pack(expand=True)

class Button2_3:  # сипсок имен травоядных существ
    def __init__(self):
        self.window2_3 = tk.Toplevel()
        self.window2_3.grab_set()
        self.window2_3['bg'] = '#33ffe6'
        self.window2_3.geometry(f'500x500+500+50')
        tk.Label(self.window2_3, text="сипсок имен травоядных существ", font=('Arial', 13)).pack(anchor='n')
        self.text = tk.Text(self.window2_3, font=('Arial', 13), bg='blue')
        self.text.place(x=60, y=60, width=300, height=100)
        WorkingMethods().viewing_name_herbivorous(self.text, Data().listHerbivorous)
        tk.Button(self.window2_3, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_3.destroy).pack(expand=True)

class Button2_4:  # список подводных существ по мере убывания их веса
    def __init__(self):
        self.window2_4 = tk.Toplevel()
        self.window2_4.grab_set()
        self.window2_4['bg'] = '#33ffe6'
        self.window2_4.geometry(f'500x500+500+50')
        tk.Label(self.window2_4, text="список подводных существ по мере убывания их веса", font=('Arial', 13)).pack(anchor='n')
        self.text = tk.Text(self.window2_4, font=('Arial', 13), bg='blue')
        self.text.place(x=60, y=60, width=300, height=100)
        WorkingMethods().view_descending_weight(self.text, Data().listUnderwater)
        tk.Button(self.window2_4, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_4.destroy).pack(expand=True)

class Button2_5:  # список наземных животных с именем каджого и местом обитания
    def __init__(self):
        self.window2_5 = tk.Toplevel()
        self.window2_5.grab_set()
        self.window2_5['bg'] = '#33ffe6'
        self.window2_5.geometry(f'500x500+500+50')
        tk.Label(self.window2_5, text="список подводных существ по мере убывания их веса", font=('Arial', 13)).pack(anchor='n')
        self.text = tk.Text(self.window2_5, font=('Arial', 13), bg='blue')
        self.text.place(x=60, y=60, width=300, height=100)
        WorkingMethods().viewing_habitats(self.text, Data().listGround)
        tk.Button(self.window2_5, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_5.destroy).pack(expand=True)

"""Удаление животных"""