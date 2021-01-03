import tkinter
from tkinter import scrolledtext

root = tkinter.Tk()
root.title('Text Editor')
root.geometry('500x650')
root.resizable(width=False, height=False)

entry_field = scrolledtext.ScrolledText(root, width=60, height=40)
entry_field.grid(column=0, row=0)

root.mainloop()
