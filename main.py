# импорт библиотеки tkinter
import tkinter
from tkinter import scrolledtext

# размер приложения
root = tkinter.Tk()
root.title('Text Editor')
root.geometry('500x650')
# удаление возможности развёртывания во весь экран
root.resizable(width=False, height=False)

# создание поля для текста
entry_field = scrolledtext.ScrolledText(root, width=60, height=40)
entry_field.grid(column=0, row=0)

root.mainloop()
