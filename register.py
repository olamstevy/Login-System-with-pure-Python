from tkinter import *
import tkinter.messagebox
import os
import smtplib
import random

def register_user():
        reg_username = username1.get()
        reg_password = password1.get()

        file = open(reg_username, "w")
        file.write(reg_password)
        file.close()

        username_reg.delete(0, END)
        password_reg.delete(0, END)

        screen2.destroy()
        tkinter.messagebox.showinfo("", "Registration Success")
        login()

def save():
    saved1 = filename.get()
    saved2 = written.get()

    file_saved = open(saved1, "w")
    file_saved.write(saved2)
    file_saved.close()
    screen4.destroy()
    

def write_note():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("WRITE NOTES")
    screen4.resizable(False, False)

    global written
    global written_text
    global filename
    global save_file
    written_text = StringVar()
    save_file = StringVar()

    Label(screen4, text="Write Your Note in the box Below").pack()
    written = Entry(screen4, width=40, bg="black", fg="white", textvariable=written_text)
    written.pack()

    Label(screen4, text="Filename").pack()
    filename = Entry(screen4, width=40, textvariable=save_file)
    filename.pack()
    Button(screen4, text="Save", command=save).pack()
    screen4.mainloop()
    
def view():
    try:
            screen7 = Toplevel(screen)
            screen7.title("NOTES")
            screen7.resizable(False, False)
            
            Open = view_file.get()
            data = open(Open, "r")
            data1 = data.read()
            Label(screen7, text=data1).pack scrollbar = Scrollbar(screen7, orient="vertical", command=screen7.yview)
            screen7.mainloop()
    except FileNotFoundError:
            tkinter.messagebox.showerror("", "This File does not exit")
            screen7.destroy()

def view_note():
    screen5 = Toplevel(screen)
    screen5.title("VIEW NOTES")
    screen5.resizable(False, False)

    global files_available
    global file_open
    global view_file
    view_file = StringVar()
    
    files_available = os.listdir()
    Label(screen5, text=files_available).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Input Name Below to Open").pack()
    file_open = Entry(screen5, width=40, textvariable=view_file)
    file_open.pack()
    Button(screen5, text="View File", command=view).pack()
    screen5.mainloop()

def Delete():
        try:
                Open = view_file1.get()
                os.remove(Open)
                tkinter.messagebox.showinfo("", Open+" "+"has been deleted")
                screen6.destroy()
        except FileNotFoundError:
                tkinter.messagebox.showerror("", "This File does not exit")
                
def delete_note():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("DELETE NOTES")
    screen6.resizable(False, False)

    global view_file1
    view_file1 = StringVar()
    
    files_available1 = os.listdir()
    Label(screen6, text=files_available1).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Input Name of file Below to Delete").pack()
    file_open1 = Entry(screen6, width=40, textvariable=view_file1)
    file_open1.pack()
    Button(screen6, text="Delete File", command=Delete).pack()
    screen6.mainloop()


def view_page():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Home")
    screen3.resizable(False, False)

    Button(screen3, text="Write Note", command=write_note).pack()
    Button(screen3, text="View Note", command=view_note).pack()
    Button(screen3, text="Delete Note", command=delete_note).pack()
    screen3.mainloop
    
def login_verfiy():
        username_v = username.get()
        password_v = password.get()
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        list_of_files = os.listdir()
        if username_v in list_of_files:
                file1 =  open(username_v, "r")
                verify = file1.read().splitlines()
                if password_v in verify:
                    screen1.destroy()
                    view_page()
                        
                else:
                        tkinter.messagebox.showinfo("", "Password incorrect")
        else:
                tkinter.messagebox.showinfo("", "Invalid User\nType in a valid account")



def register():
        global screen2
        screen2 = Toplevel(screen)
        screen2.title("Sign Up")
        screen2.resizable(False, False)

        global username1
        global password1
        global username_reg
        global password_reg
        username1 = StringVar()
        password1 = StringVar()

        Label(screen2, text="Enter details to Sign-Up", bg="grey").pack(fill=X)
        Label(screen2, text="").pack()
        Label(screen2, text="USERNAME").pack()
        username_reg = Entry(screen2, textvariable=username1)
        username_reg.pack()
        Label(screen2, text="").pack()
        Label(screen2, text="PASSWORD").pack()
        password_reg = Entry(screen2, textvariable=password1)
        password_reg.pack()
        Label(screen2, text="").pack()
        Button(screen2, text="Sign Up", height=1, bg="green", fg="white", command=register_user).pack()
        
        screen2.mainloop()

def reset_code():
    gmail_user = ''
    gmail_password = ''

    sent_from = 'Account reset Code'
    to = ['']
    subject = 'PASSWORD RESET'
    body = ("Your password reset code is ", code)
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    Label(screen8, text="A code as been sent to your email Enter the code below").pack()

def save_changes():
    new_password2 = ressetting_password.get()
    password_username = reset_name.get()

    change_file = open(password_username, "w")
    change_file.write(new_password2)
    change_file.close()
    tkinter.messagebox.showinfo("SUCCESS", "Your Password has been saved and changed and saved")
    screen8.destroy()
    login()


def checking_code():
    check_code = s_code.get()
    if check_code == code:
        global ressetting_password
        ressetting_password = StringVar()
        Label(screen8, text="").pack()
        Label(screen8, text="Enter new password").pack()
        res_password = Entry(screen8, textvariable=ressetting_password)
        res_password.delete(0, END)
        res_password.pack()
        Label(screen8, text="Password has been Changed")
        Button(screen8, text="save", command=save_changes).pack()
        
    else:
        Label(screen8, text="Code is Incorrect")
    
def reset_password():
    global rs_ps
    rs_ps = reset_name.get()
    list_of_username = os.listdir()
    if rs_ps in list_of_username:
        global reset
        reset = open(rs_ps, "w")
        reset.truncate()
        reset.close()
        
        global code
        code = random.randint(1000, 9999)
        reset_code()
        
        global s_code
        s_code = IntVar()
        sent_code = Entry(screen8, text= "Enter the Code sent to your Email", textvariable=s_code)
        sent_code.pack()
        Button(screen8, text="Verify Code", command=checking_code).pack()

    else:
        Label(screen8, text="Username not Found").pack()


def ps_reset():
    screen1.destroy()
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Reset Password")
    screen8.resizable(False, False)

    global reset_name
    reset_name = StringVar()

    Label(screen8, text="Enter Username").pack()
    username_reset = Entry(screen8, textvariable=reset_name)
    username_reset.pack()
    Button(screen8, text="Reset Password", command=reset_password).pack()


def login():
        global screen1
        screen1 =  Toplevel(screen)
        screen1.title("Login Page")
        screen1.resizable(False, False)

        Label(screen1, text="Enter details to login").pack()
        Label(screen1, text="").pack()

        global username
        global password
        username = StringVar()
        password = StringVar()

        global username_entry
        global password_entry
        Label(screen1, text="USERNAME").pack()
        username_entry = Entry(screen1, textvariable=username)
        username_entry.pack()
        Label(screen1, text="").pack()
        Label(screen1, text="PASSWORD").pack()
        password_entry = Entry(screen1, textvariable=password, show="*")
        password_entry.pack()
        Label(screen1, text="").pack()
        Button(screen1, text="Login", bg="green", fg="white", command=login_verfiy).pack()
        Label(screen1, text="").pack()
        Button(screen1, text="Forgotten Password\nReset Password?", bg="green", fg="white", command=ps_reset).pack()
        Label(screen1, text="").pack()
        screen1.mainloop()

def main_screen():
	global screen
	screen =  Tk()
	screen.resizable(False, False)
	screen.title("OLAMstevy")
	Label(text="Welcome\nPlease Choose an Option", bg="grey", height="2", font=("Calibri", 13)).pack()
	Label(text = "", height=1).pack()
	Button(text = "Login", width=20, height=2, bg="green", fg="white", command=login).pack()
	Label(text = "", height=1).pack()
	Button(text = "Register", width=20, height=2, bg="green", fg="white", command=register).pack()
	screen.mainloop()

main_screen()
