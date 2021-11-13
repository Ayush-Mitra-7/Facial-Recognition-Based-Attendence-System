from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
def change():
    img=PhotoImage(file=r'images\button_on.png')
    global button
    button=Button(root,image=img,bg="black",bd=0)
root.geometry("400x200")
img=PhotoImage(file=r'images\button_off.png')
root.configure(bg='black')
button=Button(root,image=img,bg="black",bd=0)
button.bind("<Enter>",change)
button.pack()
root.mainloop()