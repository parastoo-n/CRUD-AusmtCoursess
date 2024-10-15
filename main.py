from tkinter import *


win=Tk()
win.geometry("800x600")
# win.attributes('-fullscreen',True)
win.title('CRUD')
# win.iconbitmap('icons/python_18894.ico')
win.configure(background='#914d4d')

#TXT
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white')
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white')
txtFamily.place(x=100,y=160)

txtfiled=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white')
txtfiled.place(x=100,y=220)


txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white')
txtAge.place(x=100,y=280)

#LBL
lblName=Label(win,text='Name',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblName.place(x=20,y=100)

lblFamily=Label(win,text='Family',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblFamily.place(x=20,y=160)

lblFiled=Label(win,text='Filed',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblFiled.place(x=20,y=220)

lblAge=Label(win,text='Age',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblAge.place(x=20,y=280)

#BTN
Button
Register=Button()

win.mainloop()