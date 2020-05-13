import tkinter as tk
from random import randint


# Empty window with code
window = tk.Tk()
# Scale of window
window.geometry('600x400')
# Title of window
window.title('Interface Example')


def clicked():
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',]
    color = '#'

    for _ in range(6):
        color += symbols[randint(0, 15)]

    window.configure(bg=color)

button = tk.Button(window, text='Click me', padx='20', pady='20', font=('Verdana', 50, 'bold'), command=clicked)
button.pack()

# label = tk.Label(window, text='Hello world!', font=('arial', 50))
# label.pack()

window.mainloop()