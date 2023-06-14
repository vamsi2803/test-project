from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from time import strftime
from datetime import datetime
import random
import datetime
import time
import mysql.connector
#from main import Face_Recognition_System
from main import Face_Recognition_System
from main import Attendance
from main import Attendance1


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")  

        
        #bg img
        bg=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\bgimg.png")
        bg=bg.resize((1366,768),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=30,width=1330,height=45)

        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=170,width=340,height=450)

        img1=Image.open(r"Images\logi.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lbl_img1.place(x=620,y=170,width=150,height=150)



        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=100,y=140)

        #User name
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        username_lbl.place(x=60,y=185)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=210,width=270)

        #Password
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password_lbl.place(x=60,y=240)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=270,width=270)

        #*************Icon Images*************
        img2=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\log.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img1=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lbl_img1.place(x=555,y=353,width=25,height=25)

        img3=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\pwd.jpg")
        img3=img3.resize((30,30),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img1=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lbl_img1.place(x=555,y=410,width=30,height=30)

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=110,y=310,width=120,height=35)

        #register
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="white")
        registerbtn.place(x=15,y=350,width=160)

        forgotpassbtn=Button(frame,text="Forget Password",command=self.forget_pass_window,font=("times new roman",12,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="white")
        forgotpassbtn.place(x=10,y=375,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error",'All fields are required')
        elif self.txtuser.get()=="jntua.cse@gmail.com" and self.txtpass.get()=="cse2k23":
           # messagebox.showinfo("Success","Welcome to Project")
           open_main=messagebox.askyesno("YesNo","Access only Teacher")
           if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
           else:
                if not open_main:
                    return 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="registration")
            my_cursor=conn.cursor() 
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password") 
            else:
                open_main=messagebox.askyesno("YesNo","Access for students")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Attendance1(self.new_window)
                else:
                    if not open_main:
                        return 
            conn.commit()
            self.clear()
            conn.close() 

    #*************Reser password************
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="registration")
            my_cursor=conn.cursor() 
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get()) 
                my_cursor.execute(query,value) 

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login with new Password",parent=self.root2)            
                self.root2.destroy()
              
    #****************forget password window*************
    def forget_pass_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="registration")
            my_cursor=conn.cursor() 
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Please enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")  
                self.root2.geometry("340x450+520+170")   

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="darkred",bg="white") 
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15),state="read only")
                self.combo_security_Q["values"]=("Select ","Your birth place","Your favourite place","Your pet name")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)






class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")  

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()




       #bgimg
        bg=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\r.jpg")
        bg=bg.resize((1366,768),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        #*************Left Image************
        left=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\r1.jpg")
        left=left.resize((450,530),Image.ANTIALIAS)
        self.left=ImageTk.PhotoImage(left)

        left_img=Label(self.root,image=self.left)
        left_img.place(x=50,y=100,width=470,height=550)

        #**********frame
        frame=Frame(self.root,bg="white")
        frame.place(x=525,y=100,width=800,height=550)

        register_label=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_label.place(x=20,y=20)

        #Label and entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)

        #row 2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)

        #row 3
        security_q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_q.place(x=50,y=240)

        combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="read only")
        combo_security["values"]=("Select ","Your birth place","Your favourite place","Your pet name")
        combo_security.current(0)
        combo_security.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        security_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        security_entry.place(x=370,y=270,width=250)

        #row 4
        pwd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pwd.place(x=50,y=310)

        pd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        pd_entry.place(x=50,y=340,width=250)

        cpwd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        cpwd.place(x=370,y=310)

        cpwd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        cpwd_entry.place(x=370,y=340,width=250)

        #Check
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        img=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\here.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"C:\Users\muneendra\Desktop\FACE RECOGNITION SYSTEM\Images\login.png")
        img1=img1.resize((200,40),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=330,y=420,width=200)

        #************Function declaration***********
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_fname.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password mismatch") 
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mouni@12",database="registration")
            my_cursor=conn.cursor()          
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))   
            conn.commit()  
            conn.close()
            messagebox.showinfo("Success","Register Successfully")   

    def return_login(self):
        self.root.destroy()

            

if __name__=="__main__":
   main()    