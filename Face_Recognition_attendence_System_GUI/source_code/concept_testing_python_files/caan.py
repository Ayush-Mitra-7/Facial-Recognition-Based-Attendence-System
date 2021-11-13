# from tkinter import *
# root=Tk()
# # create the canvas, size in pixels
# canvas = Canvas(root,width=800, height=600, bg='black')

# # pack the canvas into a frame/form
# canvas.pack(expand=YES, fill=BOTH)

# # load the .gif image file
# gif1 = PhotoImage(file='images/main_backgrnd.png')

# # put gif image on canvas
# # pic's upper left corner (NW) on the canvas is at x=50 y=10
# canvas.create_image(0, 0, image=gif1, anchor=NW)

# student_button_img=PhotoImage(file='images/register_button_inactive.png')
# button=Button(root,text="click me!",image=student_button_img,  anchor=NW)
# button_window=canvas.create_window(0,0,anchor=NW,window=button)
# # run it ...
# root.mainloop()
# import everything from tkinter module
# from tkinter import *

# root = Tk()

# root.geometry('430x300')

# title = Label(root, text="Geeksforgeeks", bg="green", font=("bold", 30))
# title.pack()
# # c = Canvas(root, width=330, height=200, bg="red")
# # c.place(x=50, y=50)
# student_button_img=PhotoImage(file='images/button_off.png')
# btn = Button(root,image=student_button_img,height=20,width=110 ,bd='0' ,command=root.destroy,borderwidth=0)

# btn.place(x=65, y=100)

# root.mainloop()
from tkinter import *

count = 0

def shiftImage(event):
     if count % 2 == 0:
         canvas1.itemconfig(button, image=stopImage)

     else:
         canvas1.itemconfig(button, image=blankImage)
     globals()['count'] += 1
    #print("hello")
def change(event):
    blank = canvas1.create_image(130, 322, anchor=NW, image=stopImage, state=NORMAL)
def changeBack(event):
    blank = canvas1.create_image(130, 322, anchor=NW, image=blankImage, state=NORMAL)
root = Tk()
root.title('Button over image tkinter canvas')
root.resizable(width=False, height=False)
root.geometry('+750+150')
root.geometry('400x400')
root.configure(bg='SystemButtonFace')

playImage = PhotoImage(file=r'images\button_off.png')
stopImage = PhotoImage(file=r'images\button_on.png')
blankImage = PhotoImage(file=r'images\button_off.png')

canvas1 = Canvas(root, width=400, height=400,bg="black")
button = canvas1.create_image(100, 100, anchor=NW, image=playImage)
blank = canvas1.create_image(130, 322, anchor=NW, image=blankImage, state=NORMAL)

canvas1.tag_bind(blank," <Button-1> ",change)

canvas1.pack()

root.mainloop()



#root.update_idletasks()
#root.update()
#canvas1.itemconfig(blank, state=DISABLED) ...makes blank-button inactive