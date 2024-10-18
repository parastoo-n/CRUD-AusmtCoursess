from tkinter import *
from pymongo import MongoClient
from tkinter import ttk 
from tkinter import messagebox 
Client = MongoClient('localhost',27017)
db=Client['CRUD']
persons=db['persons1']

win=Tk()
# win.geometry("850x600")
win.attributes('-fullscreen',True)
win.title('CRUD')
#win.iconbitmap('icons/python_18894.ico')
win.configure(background='#914d4d')


#def

def changeButtonStyleWithHoverRegister(e):
    btnRegister.configure(fg='#a18282',background='white')
    
def changeButtonStyleWithHoverToSelfRegister(e):
     btnRegister.configure(fg='white',background='#a18282')

def changeButtonStyleWithHoverSearch(e):
    btnSearch.configure(fg='#a18282',background='white')
    
def changeButtonStyleWithHoverToSelfSearch(e):
     btnSearch.configure(fg='white',background='#a18282') 

def changeButtonStyleWithHover(e):
     if e.widget['text']=='Delete':
        btnDelete.configure(fg='white',background='#D00A0A')
     elif e.widget['taxt']== 'Update':
          btnUpdate.configure(fg='#a18282',background='white')

    
def changeButtonStyleWithHoverToSelf(e):
    if e.widget['text']=='Delete':
        btnDelete.configure(fg='white',background='red')
    elif e.widget['taxt']== 'Update':
          btnUpdate.configure(fg='white',background='#a18282')     
        

def OnClickRegister(e):
    if btnRegister.cget('state')==NORMAL:
       try: 

            person={'name':txtName.get(),'family':txtFamily.get(),'field':comboBoxField.get(),'age':int(txtAge.get())}
            if Exist(person)==False:
               Register(person)
            #    allData=ReadData()
               CleanTable()
            #    for data in allData:
            #        InsertDataToTable(data)
               Load()
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

def OnClickSearch(e):
    searchRequestUser=txtSearch.get()
    if searchRequestUser=='':
        CleanTable()
        Load()
    else:    
        result=search(searchRequestUser)
        CleanTable()
        for data in result:
            InsertDataToTable(data)

def search(searchRequestUser):
    resultSearch=[]
    allData=ReadData()
    for data in allData:
        if data['name'] == searchRequestUser or data['family'] == searchRequestUser or data['field'] == searchRequestUser or str(data['age']) == searchRequestUser :
           resultSearch.append(data)   
    return resultSearch

def Load():
    alldata=ReadData()
    for data in alldata:
     InsertDataToTable(data) 

def OnClickDelete(e):
    dialog=messagebox.askyesno('Delete Data','Are you sure you want to delete your data?')
    if dialog:
       select=table.selection()
       if select !=():
          Data=table.item(select)['values']
          person={'name':Data[0],'family':Data[1],'field':Data[2],'age':int(Data[3])}
          Delete(person)
          table.delete(select)


def Delete(person):
    result=FindData(person)
    if result !=False:
        persons.delete_one(person)


def Selection(e):
    select=table.selection()
    if select !=():
      data=table.item(select)['values']
      Name.set(data[0])
      Family.set(data[1])
      comboBoxField.set(data[2])
      Age.set(data[3])

def OnClickUpdate(e):
   dialog=messagebox.askyesno('Update Data','Are you sure you want to update your data?')
   if dialog:
       select=table.selection()
       if select !=():
          Data=table.item(select)['values']
          Oldperson={'name':Data[0],'family':Data[1],'field':Data[2],'age':int(Data[3])}
          Newperson={'name':txtName.get(), 'family':txtFamily.get(),'field':comboBoxField.get(),'age':int(txtAge.get())}
          Update(Oldperson,Newperson)
          CleanTable()
          Load()

def Update(Oldperson,Newperson):
    result=FindData(Oldperson)
    if result != False:
       newData={'$set':Newperson} 
       persons.update_one(Oldperson,newData)

def FindData(Data):
    alldata=ReadData()
    for data in alldata:
        if data['name'] == Data['name'] and data['family'] == Data['family'] and data['field'] == Data['field'] and data['age'] == Data['age']:
            return data
    return False

def DestroyWindow(e):
   win.destroy()
 #Texvariable     
Name=StringVar()
Family=StringVar()
# Field=StringVar() 
Age=StringVar() 
Search=StringVar() 

#image
closeImage=PhotoImage(file='images/close-window-16.png')

#TXTbox
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

txtSearch=Entry(win,width=20,bd=5,font=('arial',15,'bold'),bg='#a18282',fg='white',textvariable=Search,justify='center')
txtSearch.place(x=550,y=50)

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
btnRegister.bind('<Enter>',changeButtonStyleWithHoverRegister)
btnRegister.bind('<Leave>',changeButtonStyleWithHoverToSelfRegister)
btnRegister.bind('<Button-1>',OnClickRegister)
btnRegister.place(x=125,y=350)

btnSearch=Button(win,text='search',width=10,font=('arial',12,'bold'),bg='#a18282',fg='white')
btnSearch.bind('<Enter>',changeButtonStyleWithHoverSearch)
btnSearch.bind('<Leave>',changeButtonStyleWithHoverToSelfSearch)
btnSearch.bind('<Button-1>',OnClickSearch)
btnSearch.place(x=400,y=50)

btnDelete=Button(win,text='Delete',width=9,font=('arial',12,'bold'),bg='red',fg='white')
btnDelete.bind('<Enter>',changeButtonStyleWithHover)
btnDelete.bind('<Leave>',changeButtonStyleWithHoverToSelf)
btnDelete.bind('<Button-1>',OnClickDelete)
btnDelete.place(x=700 ,y=330)

btnUpdate=Button(win,text='Update',width=9,font=('arial',12,'bold'),bg='#a18282',fg='white')
btnUpdate.bind('<Enter>',changeButtonStyleWithHover)
btnUpdate.bind('<Leave>',changeButtonStyleWithHoverToSelf)
btnUpdate.bind('<Button-1>',OnClickUpdate)
btnUpdate.place(x=400 ,y=330)



btnUpdate=Button(win,text='Update',width=9,font=('arial',12,'bold'),bg='#a18282',fg='white')
btnUpdate.bind('<Enter>',changeButtonStyleWithHover)
btnUpdate.bind('<Leave>',changeButtonStyleWithHoverToSelf)
btnUpdate.bind('<Button-1>',OnClickUpdate)
btnUpdate.place(x=400 ,y=330)

CloseBtn=Button(win,image=closeImage)
CloseBtn.bind('<Button-1>',DestroyWindow)
CloseBtn.place(x=10,y=10)

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
table.bind('<Button-1>',Selection)
table.place(x=400,y=100)

Load()

win.mainloop()