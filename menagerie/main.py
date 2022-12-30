from GUI import *

"""Добавление животного"""

"""Просмотр животных"""

class Button2_1(tk.Toplevel):  # топ 3 самых легких существа зоопарка
    def __init__(self, parent):
        super().__init__(parent)
        self.label2_1 = tk.Label(self, text="топ 3 самых легких существа зоопарка")
        self.button2_1 = tk.Button(self, text="1. Exid", command=self.destroy)

        self.label2_1.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)

class Button2_2(tk.Toplevel):  # топ 5 самых больших хищников
    def __init__(self, parent):
        super().__init__(parent)
        self.label2_1 = tk.Label(self, text="топ 5 самых больших хищников")
        self.button2_1 = tk.Button(self, text="1. Exid", command=self.destroy)

        self.label2_1.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)

class Button2_3(tk.Toplevel):  # сипсок имен травоядных существ
    def __init__(self, parent):
        super().__init__(parent)
        self.label2_1 = tk.Label(self, text="сипсок имен травоядных существ")
        self.button2_1 = tk.Button(self, text="1. Exid", command=self.destroy)

        self.label2_1.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)

class Button2_4(tk.Toplevel):  # список подводных существ по мере убывания их веса\
    def __init__(self, parent):
        super().__init__(parent)
        self.label2_1 = tk.Label(self, text="список подводных существ по мере убывания их веса")
        self.button2_1 = tk.Button(self, text="1. Exid", command=self.destroy)

        self.label2_1.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)

class Button2_5(tk.Toplevel):  # список наземных животных с именем каджого и местом обитания
    def __init__(self, parent):
        super().__init__(parent)
        self.label2_1 = tk.Label(self, text="список наземных животных с именем каджого и местом обитания")
        self.button2_1 = tk.Button(self, text="1. Exid", command=self.destroy)

        self.label2_1.pack(padx=20, pady=20)
        self.button2_1.pack(pady=5, ipadx=2, ipady=2)

"""Удаление животных"""