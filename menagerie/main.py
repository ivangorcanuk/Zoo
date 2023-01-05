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
        self.window2_1.geometry(f'500x700+500+50')
        self.label2_1 = tk.Label(self.window2_1, text="топ 3 самых легких существа зоопарка", font=('Arial', 13)).pack()
        self.text = tk.Text(self.window2_1, width=50, height=50, bg='blue').pack()
        for i in range(7):
            self.text.(tk.INSERT, 'end', f'A{i + 2} = (1 - 1) * 2 + 2\n')
        self.button2_1 = tk.Button(self.window2_1, text="1. Exid", font=('Arial', 13), command=self.window2_1.destroy).pack()

class Button2_2:  # топ 5 самых больших хищников
    def __init__(self):
        self.window2_2 = tk.Toplevel()
        self.window2_2.grab_set()
        self.label2_2 = tk.Label(self.window2_2, text="топ 5 самых больших хищников", font=('Arial', 13))
        self.button2_2 = tk.Button(self.window2_2, text="1. Exid", font=('Arial', 13), command=self.window2_2.destroy)

        self.label2_2.pack(padx=20, pady=20)
        self.button2_2.pack(pady=5, ipadx=2, ipady=2)

class Button2_3:  # сипсок имен травоядных существ
    def __init__(self):
        self.window2_3 = tk.Toplevel()
        self.window2_3.grab_set()
        self.label2_3 = tk.Label(self.window2_3, text="сипсок имен травоядных существ", font=('Arial', 13))
        self.button2_3 = tk.Button(self.window2_3, text="1. Exid", font=('Arial', 13), command=self.window2_3.destroy)

        self.label2_3.pack(padx=20, pady=20)
        self.button2_3.pack(pady=5, ipadx=2, ipady=2)

class Button2_4:  # список подводных существ по мере убывания их веса\
    def __init__(self):
        self.window2_4 = tk.Toplevel()
        self.window2_4.grab_set()
        self.label2_4 = tk.Label(self.window2_4, text="список подводных существ по мере убывания их веса", font=('Arial', 13))
        self.button2_4 = tk.Button(self.window2_4, text="1. Exid", font=('Arial', 13), command=self.window2_4.destroy)

        self.label2_4.pack(padx=20, pady=20)
        self.button2_4.pack(pady=5, ipadx=2, ipady=2)

class Button2_5:  # список наземных животных с именем каджого и местом обитания
    def __init__(self):
        self.window2_5 = tk.Toplevel()
        self.window2_5.grab_set()
        self.label2_5 = tk.Label(self.window2_5, text="список наземных животных с именем каджого и местом обитания", font=('Arial', 13))
        self.button2_5 = tk.Button(self.window2_5, text="1. Exid", font=('Arial', 13), command=self.window2_5.destroy)

        self.label2_5.pack(padx=20, pady=20)
        self.button2_5.pack(pady=5, ipadx=2, ipady=2)

"""Удаление животных"""