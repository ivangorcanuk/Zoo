import tkinter as tk

class AddingAnimals:
    def menu1(self):
        new_window1 = tk.Toplevel()
        new_window1.geometry('300x300+600+200')
        new_window1.title("Animal registration")
        new_window1.grab_set()
        tk.Button(text='1. Top 3 Lightest Zoo Creatures', font=('Arial', 13),command=AddingAnimals().menu1)\
                                                        .grid(row=0, column=0,sticky='wens',padx=2,pady=2)
        tk.Button(text='2. Top 5 biggest predators', font=('Arial', 13), command=SeeAnimals().menu2)\
                                                        .grid(row=1, column=0, sticky='wens', padx=2, pady=2)
        tk.Button(text='3. List of herbivore names', font=('Arial', 13), command=DeleteAnimal().menu3)\
                                                        .grid(row=2, column=0, sticky='wens', padx=2, pady=2)
        tk.Button(text='1. List of underwater creatures in decreasing order of their weight', font=('Arial', 13), command=AddingAnimals().menu1) \
                                                        .grid(row=0, column=0, sticky='wens', padx=2, pady=2)
        tk.Button(text='2. List of land animals, with each name and location', font=('Arial', 13), command=SeeAnimals().menu2) \
                                                        .grid(row=1, column=0, sticky='wens', padx=2, pady=2)
        tk.Button(text='3. Exit', font=('Arial', 13), command=DeleteAnimal().menu3) \
                                                        .grid(row=2, column=0, sticky='wens', padx=2, pady=2)
        new_window1.grid_columnconfigure(0, minsize=300)

class SeeAnimals:
    def menu2(self):
        new_window1 = tk.Toplevel()
        new_window1.geometry('300x300+600+200')
        new_window1.title("menu2")

class DeleteAnimal:
    def menu3(self):
        new_window1 = tk.Toplevel()
        new_window1.geometry('300x300+600+200')
        new_window1.title("menu2")

win = tk.Tk()
win.geometry('300x300+600+200')
win.title('Zoo')

tk.Button(text='1. add an animal', font=('Arial', 13), command=AddingAnimals().menu1).grid(row=0, column=0, sticky='wens', padx=2, pady=2)
tk.Button(text='2. see animals', font=('Arial', 13), command=SeeAnimals().menu2).grid(row=1, column=0, sticky='wens', padx=2, pady=2)
tk.Button(text='3. delete animal', font=('Arial', 13), command=DeleteAnimal().menu3).grid(row=2, column=0, sticky='wens', padx=2, pady=2)

win.grid_columnconfigure(0, minsize=300)

win.mainloop()