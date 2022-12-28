import tkinter as tk

class AddingAnimals:
    def menu0(self):
        print('1')
        win = tk.Tk()
        win.geometry('300x300+600+200')
        tk.Button(text='lupa', font=('Arial', 13), command=AddingAnimals().menu0).grid(row=0, column=0,
                                                                                                   sticky='wens',
                                                                                                   padx=2, pady=2)
        win.grid_columnconfigure(0, minsize=300)

class SeeAnimals:
    def menu1(self):
        print('2')

class DeleteAnimal:
    def menu2(self):
        print('3')

win = tk.Tk()
win.geometry('300x300+600+200')
win.title('Zoo')

tk.Button(text='1. add an animal', font=('Arial', 13), command=AddingAnimals().menu0).grid(row=0, column=0, sticky='wens', padx=2, pady=2)
tk.Button(text='2. see animals', font=('Arial', 13), command=SeeAnimals().menu1).grid(row=1, column=0, sticky='wens', padx=2, pady=2)
tk.Button(text='3. delete animal', font=('Arial', 13), command=DeleteAnimal().menu2).grid(row=2, column=0, sticky='wens', padx=2, pady=2)

win.grid_columnconfigure(0, minsize=300)

win.mainloop()