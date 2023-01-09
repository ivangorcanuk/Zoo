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


class SeeAnimals:  # просмотр животных
    def __init__(self):
        self.seeAnimals = tk.Toplevel()
        self.seeAnimals.grab_set()
        self.seeAnimals['bg'] = '#33ffe6'
        self.seeAnimals.geometry(f'550x500+500+50')
        self.seeAnimals.title('See animals')

        self.button('Top 3 Lightest Zoo Creatures', self.open_window, 1).grid(row=1, column=0, padx=30, pady=2)
        self.button('Top 5 biggest predators', self.open_window, 2).grid(row=2, column=0, padx=30, pady=2)
        self.button('List of herbivore names', self.open_window, 3).grid(row=3, column=0, padx=30, pady=2)
        self.button('List of underwater creatures in decreasing order of their weight', self.open_window, 4).grid(row=4, column=0, padx=30, pady=2)
        self.button('List of land animals, with each name and location', self.open_window, 5).grid(row=5, column=0, padx=30, pady=2)
        self.button('Exit', self.seeAnimals.destroy, 6).grid(row=6, column=0, padx=30, pady=2)

    def button(self, text, command, wagrw):
        self.value_button = wagrw
        return tk.Button(self.seeAnimals, text=text, font=('Arial', 13), command=command)

    def label(self, text):
        return tk.Label(self.seeAnimals, text=text, font=('Arial', 13))

    def text(self):
        return tk.Text(self.seeAnimals, font=('Arial', 13), bg='#33ffe6')

    def open_window(self):
        self.label('Top 3 Lightest Zoo Creatures').grid(row=7, column=0, padx=30, pady=2)
        self.text1 = self.text()
        self.text1.place(x=120, y=270, width=300, height=100)
        print('re')
        if self.value_button == 1:
            print('rr')
            WorkingMethods().view_lungs_animal(self.text, Data().listAnimal)  # вызывали метод из файла WorkingMethods
        elif self.value_button == 2:
            WorkingMethods().viewing_large_animal(self.text, Data().listPredator)
        elif self.value_button == 3:
            WorkingMethods().viewing_name_herbivorous(self.text, Data().listHerbivorous)
        elif self.value_button == 4:
            WorkingMethods().view_descending_weight(self.text, Data().listUnderwater)
        elif self.value_button == 5:
            WorkingMethods().viewing_habitats(self.text, Data().listGround)

# class Button2_1:  # топ 3 самых легких существа зоопарка
#     def __init__(self):
#         self.window2_1 = tk.Toplevel()
#         self.window2_1.grab_set()
#         self.window2_1['bg'] = '#33ffe6'
#         self.window2_1.geometry(f'500x500+500+50')
#         tk.Label(self.window2_1, text="топ 3 самых легких существа зоопарка", font=('Arial', 13)).pack(anchor='n')
#         self.text = tk.Text(self.window2_1, font=('Arial', 13), bg='blue')
#         self.text.place(x=60, y=60, width=300, height=100)
#         WorkingMethods().view_lungs_animal(self.text, Data().listAnimal)  # вызывали метод из файла WorkingMethods
#         tk.Button(self.window2_1, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_1.destroy).pack(expand=True)
#
# class Button2_2:  # топ 5 самых больших хищников
#     def __init__(self):
#         self.window2_2 = tk.Toplevel()
#         self.window2_2.grab_set()
#         self.window2_2['bg'] = '#33ffe6'
#         self.window2_2.geometry(f'500x500+500+50')
#         tk.Label(self.window2_2, text="топ 5 самых больших хищников", font=('Arial', 13)).pack(anchor='n')
#         self.text = tk.Text(self.window2_2, font=('Arial', 13), bg='blue')
#         self.text.place(x=60, y=60, width=300, height=100)
#         WorkingMethods().viewing_large_animal(self.text, Data().listPredator)  # вызывали метод из файла WorkingMethods
#         tk.Button(self.window2_2, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_2.destroy).pack(expand=True)
#
# class Button2_3:  # сипсок имен травоядных существ
#     def __init__(self):
#         self.window2_3 = tk.Toplevel()
#         self.window2_3.grab_set()
#         self.window2_3['bg'] = '#33ffe6'
#         self.window2_3.geometry(f'500x500+500+50')
#         tk.Label(self.window2_3, text="сипсок имен травоядных существ", font=('Arial', 13)).pack(anchor='n')
#         self.text = tk.Text(self.window2_3, font=('Arial', 13), bg='blue')
#         self.text.place(x=60, y=60, width=300, height=100)
#         WorkingMethods().viewing_name_herbivorous(self.text, Data().listHerbivorous)
#         tk.Button(self.window2_3, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_3.destroy).pack(expand=True)
#
# class Button2_4:  # список подводных существ по мере убывания их веса
#     def __init__(self):
#         self.window2_4 = tk.Toplevel()
#         self.window2_4.grab_set()
#         self.window2_4['bg'] = '#33ffe6'
#         self.window2_4.geometry(f'500x500+500+50')
#         tk.Label(self.window2_4, text="список подводных существ по мере убывания их веса", font=('Arial', 13)).pack(anchor='n')
#         self.text = tk.Text(self.window2_4, font=('Arial', 13), bg='blue')
#         self.text.place(x=60, y=60, width=300, height=100)
#         WorkingMethods().view_descending_weight(self.text, Data().listUnderwater)
#         tk.Button(self.window2_4, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_4.destroy).pack(expand=True)
#
# class Button2_5:  # список наземных животных с именем каджого и местом обитания
#     def __init__(self):
#         self.window2_5 = tk.Toplevel()
#         self.window2_5.grab_set()
#         self.window2_5['bg'] = '#33ffe6'
#         self.window2_5.geometry(f'500x500+500+50')
#         tk.Label(self.window2_5, text="список подводных существ по мере убывания их веса", font=('Arial', 13)).pack(anchor='n')
#         self.text = tk.Text(self.window2_5, font=('Arial', 13), bg='blue')
#         self.text.place(x=60, y=60, width=300, height=100)
#         WorkingMethods().viewing_habitats(self.text, Data().listGround)
#         tk.Button(self.window2_5, width=20, text="1. Exid", font=('Arial', 13), command=self.window2_5.destroy).pack(expand=True)
#
# """Удаление животных"""