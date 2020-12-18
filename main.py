import tkinter
from tkinter import scrolledtext

root = tkinter.Tk()
root.title('Text Editor')
root.geometry('500x650')
root.resizable(width=False, height=False)

text = scrolledtext.ScrolledText(root, width=60, height=40)
text.grid(column=0, row=0)

root.mainloop()