from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Registration_window import *
#?-----------------------------PACKAGES---------------------------?#


#?-----------------------------MAIN CLASS---------------------------?#
class Face_Recognition_Attendence_system:
    def __init__(self, root):
        self.root = root

        #TODO: The size of the window------------------#
        self.root.geometry("800x600+360+100")
        self.root.resizable(False, False)
        #TODO: The size of the window------------------#

        self.root.title("Face Rcognition Attendence System")

        #TODO: The logo of the window------------------#
        # img = Image.open(r'images/logo_face_recognition.png')#! image.*---->image.ico
        # img.save('icon.ico',format = 'ICO', sizes=[(100,100)])#! image.*---->image.ico
        self.root.iconbitmap(r'images\icon.ico')
        #TODO: The logo of the window------------------#

        #TODO: The background of the window------------------#
        self.root.configure(bg='#1b1b1b')
        #TODO: The background of the window------------------#

        #TODO: The background text and logo of the window------------------#
        self.text = Label(self.root, text="Face recognition Attendence System",
                          bg="#1b1b1b", fg="white", font=("Origin Tech Demo", 28))
        self.text.place(x=13, y=100)
        self.main_logo = ImageTk.PhotoImage(
            Image.open(r"images\main_logo.png"))
        self.main_logo_label = Label(image=self.main_logo, bg="#1b1b1b")
        self.main_logo_label.place(x=330, y=10)
        #TODO: The background text and logo  of the window------------------#
        
        #TODO: The background student logo ,button and text of the window------------------#
        self.student_logo = ImageTk.PhotoImage(
            Image.open(r"images\student_logo.png"))
        self.student_logo_label = Label(image=self.student_logo, bg="#1b1b1b")
        self.student_logo_label.place(x=68, y=180)
        self.student_text = Label(self.root, text="Are You A Student?",
                                  bg="#1b1b1b", fg="white", font=("cream Demo", 18))
        self.student_text.place(x=20, y=300)
        self.btn_inactive = ImageTk.PhotoImage(
            Image.open(r"images\button_off.png"))
        self.btn_active = ImageTk.PhotoImage(
            Image.open(r"images\button_on.png"))

        self.stu_img = ImageTk.PhotoImage(Image.open(r"images\student_reg_pic.png"))#! image of registraton window

        #! Student BUTTON FUNCTIONS:---------------------------
        def on_enter(event):
            self.student_button.config(image=self.btn_active)

        def on_leave(event):
            self.student_button.config(image=self.btn_inactive)

        def Stu_reg():
            openStudentWindow(self.stu_img )
        #! Student BUTTON FUNCTIONS:---------------------------

        self.student_button = Button(self.root, image=self.btn_inactive,
                                     bg="#1b1b1b", bd=0, activebackground="#1b1b1b", command=Stu_reg)
        self.student_button.place(x=70, y=380)
        self.student_button.bind("<Enter>", on_enter)
        self.student_button.bind("<Leave>", on_leave)
        #TODO: The background student logo ,button and text of the window------------------#

        #TODO: The background teacher logo ,button and text of the window-------------------#
        self.teacher_logo = ImageTk.PhotoImage(Image.open(r"images\teacher_logo.png"))
        self.teacher_logo_label = Label(image=self.teacher_logo, bg="#1b1b1b")
        self.teacher_logo_label.place(x=600, y=190)
        self.teacher_text = Label(self.root, text="Are You A Teacher?",
                                  bg="#1b1b1b", fg="white", font=("cream Demo", 18))
        self.teacher_text.place(x=540, y=300)
        self.btn_inactive1 = ImageTk.PhotoImage(
            Image.open(r"images\button_off.png"))
        self.btn_active1 = ImageTk.PhotoImage(
            Image.open(r"images\button_on.png"))
        self.teach_img = ImageTk.PhotoImage(Image.open(r"images\teacher_img.png"))#! image of registraton window
        #! Teacher BUTTON FUNCTIONS:---------------------------
        def on_enter1(event):
            self.teacher_button.config(image=self.btn_active1)

        def on_leave1(event):
            self.teacher_button.config(image=self.btn_inactive1)

        def text1():
            openTeacherWindow(self.teach_img)
        #! Teacher BUTTON FUNCTIONS:---------------------------

        self.teacher_button = Button(self.root, image=self.btn_inactive,
                                     bg="#1b1b1b", bd=0, activebackground="#1b1b1b", command=text1)
        self.teacher_button.place(x=602, y=380)
        self.teacher_button.bind("<Enter>", on_enter1)
        self.teacher_button.bind("<Leave>", on_leave1)
        #TODO: The background teacher logo ,button and text of the window------------------#

        #TODO: The background Design of the window------------------#
        self.wire_grid = ImageTk.PhotoImage(Image.open(r"images\digital_wire_LTR.png"))
        self.wire_grid_label = Label(image=self.wire_grid, bg="#1b1b1b")
        self.wire_grid_label.place(x=0, y=514)
        #TODO: The background Design of the window------------------#


#?-----------------------------MAIN CLASS---------------------------?#


#?-----------------------------MAIN METHOD---------------------------?#
if __name__ == "__main__":
    root = Tk()
    root_obj = Face_Recognition_Attendence_system(root)
    root.mainloop()
#?-----------------------------MAIN METHOD---------------------------?#
