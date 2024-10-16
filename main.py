from tkinter import *
from pymongo import MongoClient
from tkinter import ttk 
from tkinter import messagebox 
Client = MongoClient('localhost',27017)
db=Client['CRUD']
persons=db['persons']

win=Tk()
win.geometry("850x600")
# win.attributes('-fullscreen',True)
win.title('CRUD')
#win.iconbitmap('icons/python_18894.ico')
win.configure(background='#914d4d')


#def

def changeButtonStyleWithHover(e):
    btnRegister.configure(fg='#a18282',background='white')
    
def changeButtonStyleWithHoverToSelf(e):
     btnRegister.configure(fg='white',background='#a18282')

def OnClickRegister(e):
    if btnRegister.cget('state')==NORMAL:
       try: 
        
            person={'name':txtName.get(),'family':txtFamily.get(),'field':comboBoxField.get(),'age':int(txtAge.get())}
            if Exist(person)==False:
               Register(person)
               allData=ReadData()
               CleanTable()
               for data in allData:
                   InsertDataToTable(data)
               CleanTextBoxAfterUseCrud()
               messagebox.showinfo("success","your registration is complete")
            else:
                messagebox.showerror("error","you have already registered")
       except:
            messagebox.showerror("error","you must enter a number in the age field")
    # InsertDataToTable(person)

def Register(person):
    if person['age']>=18:
       persons.insert_one(person)
   
def ReadData():
    AllData=persons.find()
    return AllData 
# ReadData() 
def InsertDataToTable(person):
    table.insert('','end',values=[person['name'],person['family'],person['field'],person['age']])

def CleanTable():
    for item in table.get_children():
        table.delete(item)

def CleanTextBoxAfterUseCrud():
        Name.set('')
        Family.set('')
        # Field.set('')
        Age.set('')
        txtName.focus_set()
def ActiveBtn(e):
    if txtName.get()!= '' and txtFamily.get() != '' and comboBoxField.get() != '' and txtAge.get() != '':
        btnRegister.configure(state=NORMAL)
    else: 
        btnRegister.configure(state=DISABLED)

def Exist(person):
    allData=ReadData()
    for data in allData:
        if data['name'] == person['name'] and data['family'] == person['family'] and data['field'] == person['field'] and data['age'] == person['age']:
            return True
    return False                
      
Name=StringVar()
Family=StringVar()
# Field=StringVar() 
Age=StringVar()          

#TXT
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Name,justify='center')
txtName.bind('<KeyRelease>',ActiveBtn)
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Family,justify='center')
txtFamily.bind('<KeyRelease>',ActiveBtn)
txtFamily.place(x=100,y=160)

comboBoxField=ttk.Combobox(win,width=15,font=('arial',12,'bold'),foreground='white',background='#a18282')
comboBoxField.place(x=100,y=220)
comboBoxField['values']=['computer','electronic','chemistry','physicsgit']
# txtField=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Field,justify='center')
# txtField.bind('<KeyRelease>',ActiveBtn)
# txtField.place(x=100,y=220)


txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Age,justify='center')
txtAge.bind('<KeyRelease>',ActiveBtn)
txtAge.place(x=100,y=280)

#LBL
lblName=Label(win,text='Name',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblName.place(x=20,y=100)

lblFamily=Label(win,text='Family',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblFamily.place(x=20,y=160)

lblField=Label(win,text='Filed',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblField.place(x=20,y=220)

lblAge=Label(win,text='Age',font=('arial',12,'bold'),bg='#a18282',fg='white')
lblAge.place(x=20,y=280)

#BTN

btnRegister=Button(win,text='register',width=10,font=('arial',12,'bold'),bg='#a18282',fg='white')
btnRegister.configure(state=DISABLED)
btnRegister.bind('<Enter>',changeButtonStyleWithHover)
btnRegister.bind('<Leave>',changeButtonStyleWithHoverToSelf)
btnRegister.bind('<Button-1>',OnClickRegister)
btnRegister.place(x=125,y=350)

#table
# table=ttk.Treeview(win,columns=('name','family','field','age'),show='headings')
# table.heading('name',text='Name')
# table.heading('family',text='Family')
# table.heading('field',text='Field')
# table.heading('age',text='Age')
# table.column('name',width=100)
# table.column('family',width=100)
# table.column('field',width=100)
# table.column('age',width=100)

columns=('Name','Family','Field','Age')
table=ttk.Treeview(win,columns=columns,show='headings')
for i in range(len(columns)):
    table.heading(columns[i],text=columns[i])
    table.column(columns[i],width=100,anchor='center')

table.place(x=400,y=100)

win.mainloop()