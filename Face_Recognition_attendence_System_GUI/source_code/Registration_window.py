from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#?-----------------------------PACKAGES---------------------------?#


#?-----------------------------Main Code---------------------------?#

#?-----------------------------Main Code---------------------------?#


#?-----------------------------Functions---------------------------?#
def openStudentWindow(stu_img):
    #TODO: The size of the window------------------#
    stu_root = Toplevel()
    stu_root.title("Student Registration Window")
    stu_root.iconbitmap(r'images\icon.ico')  # !logo of the window
    stu_root.geometry("800x600+360+100")
    stu_root.resizable(False, False)
    #TODO: The size of the window------------------#

#TODO: The background of the window------------------#
    stu_root.configure(bg='#1b1b1b')
#TODO: The background of the window------------------#

#TODO: The background text of the window------------------#
    stu_img_label = Label(stu_root, image=stu_img, bg="#1b1b1b")
    stu_img_label.place(x=0, y=0)
    stu_text = Label(stu_root, text="REGISTRATION",
                     bg="#1b1b1b", fg="white", font=("Good Timing Rg", 28))
    stu_text.place(x=390, y=30)
#TODO: The background text of the window------------------#


def openTeacherWindow(stu_img):
    #TODO: The size of the window------------------#
    teach_root = Toplevel()
    teach_root.title("Teacher Registration Window")
    teach_root.iconbitmap(r'images\icon.ico')  # !logo of the window
    teach_root.geometry("800x600+360+100")
    teach_root.resizable(False, False)
    #TODO: The size of the window------------------#

#TODO: The background of the window------------------#
    teach_root.configure(bg='#1b1b1b')
#TODO: The background of the window------------------#

#TODO: The background text of the window------------------#
    stu_img_label = Label(teach_root, image=stu_img, bg="#1b1b1b")
    stu_img_label.place(x=0, y=0)
    stu_text = Label(teach_root, text="REGISTRATION",
                     bg="#1b1b1b", fg="white", font=("Good Timing Rg", 28))
    stu_text.place(x=390, y=30)
#TODO: The background text of the window------------------#
#?-----------------------------Functions---------------------------?#
