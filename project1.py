from tkinter import *

window = Tk()
window.geometry('500x440')
window.config(bg='#333333')
window.title('Login form')


log = Label(window,text='Log In',font=('Tahomah',14,'bold'),bg='#333333',fg='yellow')
log.place(relx=.45,rely=.1)
name = Label(window,text='Username',font=('Tahoma',12),bg='#333333',fg='yellow')
name.place(relx=0.05,rely=.245)
name_entry = Entry(window,width=35,font=('Tahoma',12))
name_entry.place(relx=0.22,rely=.25)
password = Label(window,text='Password',font=('Tahoma',12),bg='#333333',fg='yellow')
password.place(relx=0.05,rely=.4)
password_entry = Entry(window,width=35,font=('Tahoma',12),show='*')
password_entry.place(relx=0.22,rely=.4)
sub = Button(window,width=20,text='Login',font=('Tahoma',12,'bold'),bg='yellow',fg='#333333')
sub.place(relx=.32,rely=.6)

window.mainloop()