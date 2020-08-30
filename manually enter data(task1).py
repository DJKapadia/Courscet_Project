'''
In this project we manually add data into our database. In this project there are 4 button create,insert,display,group display and one combobx.
1.)First of we create database by pressing create button
2.)After creating dataset we enter data into the given entry level and click insert to insert data in our dataset
3.)If we want to see all data then we press display button
4.)After all of this process, let we move on the combo box. Select entry into that combobax and if we want to display this combobox result then press group display button
'''
from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter.ttk import Combobox
import sqlite3
import tkinter.ttk as ttk
from sqlite3 import Error
root = Tk()
root.geometry('900x900')
root.title("Task1")
#display our  data group wise
def print_me():
    value=combo.get()
    if value=='Country':
        db = sqlite3.connect('Dhruv.db')#create and connect dhruv database
        cursor = db.cursor()
        a = "select Country,count(Firstname) as Count_of_user,ROUND((count(*)*100)/(SELECT count(*) FROM Exam)) as percentage from Exam group by Country"
        cur = db.cursor()
        cur.execute(a)
        b = cur.fetchall()
        for v in b:
            if (v == None):
                break
            print(v)
        db.close()
    elif value=='Department':
        db = sqlite3.connect('Dhruv.db')
        cursor = db.cursor()
        a = "select Department,count(Firstname) as Count_of_user, ROUND((count(*)*100)/(SELECT count(*) FROM Exam)) as percentage from Exam group by Department"
        cur = db.cursor()
        cur.execute(a)
        b = cur.fetchall()
        for v in b:
            if (v == None):
                break
            print(v)
        db.close()
    else:
        db = sqlite3.connect('Dhruv.db')
        cursor = db.cursor()
        a = "select Salary_Slab,count(Firstname) as Count_of_user,ROUND((count(*)*100)/(SELECT count(*) FROM Exam)) as percentage from Exam group by Salary_Slab"
        cur = db.cursor()
        cur.execute(a)
        b = cur.fetchall()
        for v in b:
            if (v == None):
                break
            print(v)
        db.close()
#create databse with name of dhruv.db
def create():
    try:
        sqliteConnection = sqlite3.connect('Dhruv.db')#create and connect dhruv database
        #create exam table
        sqlite_create_table_query = '''CREATE TABLE Exam (
                                    id INTEGER PRIMARY KEY,
                                    Firstname TEXT ,
                                    LastName TEXT  ,
                                    Department TEXT,
                                    Salary_Slab TEXT,
                                    City TEXT,
                                    Country TEXT);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()#close our databse connection

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

#insert data into our database
def insertVaribleIntoTable(id, Firstname, LastName, Department, Salary_Slab, City, Country):
    try:
        sqliteConnection = sqlite3.connect('Dhruv.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Exam
                          (id,Firstname, LastName, Department, Salary_Slab, City, Country) 
                          VALUES (?, ?, ?, ?, ?,?,?);"""

        data_tuple = (id, Firstname, LastName, Department, Salary_Slab, City, Country)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
def Insert():
    ide=i.get()
    fname=sname.get()
    lname=erno.get()
    dep=sem.get()
    sala=b.get()
    ci=sub.get()
    coun=g.get()
    #insert data into function
    insertVaribleIntoTable(ide, fname, lname, dep, sala,ci,coun)
#display our whole data
def Display():
    db = sqlite3.connect('Dhruv.db')
    cursor = db.cursor()
    a = "select *from Exam"
    cur = db.cursor()
    cur.execute(a)
    # while True:
    b = cur.fetchall()
    for v in b:
        if (v == None):
            break
        print(v)
    db.close()
i=IntVar() #fetch int data from entry label
sname=StringVar()#fetch string data from entry label
erno=StringVar()#fetch string data from entry label
sem=StringVar()#fetch string data from entry label
b=StringVar()#fetch string data from entry label
sub=StringVar()#fetch string data from entry label
g=StringVar()#fetch string data from entry label
lb = Label(root, text="id",font="30")
e  = Entry(root,width=30,textvariable=i)
lb1 = Label(root, text="Firstname",font="30")
e1  = Entry(root,width=30,textvariable=sname)
lb2 = Label(root, text="LastName",font="30")
e2  = Entry(root,width=30,textvariable=erno)
lb3 = Label(root, text="Department",font="30")
e3  = Entry(root,width=30,textvariable=sem)
lb4 = Label(root, text="Salary_Slab",font="30")
e4  = Entry(root,width=30,textvariable=b)
lb5 = Label(root, text="City",font="30")
e5  = Entry(root,width=30,textvariable=sub)
lb6 = Label(root, text="Country",font="30")
e6  = Entry(root,width=30,textvariable=g)
lb.place(x=150,y=250)
lb1.place(x=150,y=300)
lb2.place(x=150,y=350)
lb3.place(x=150,y=400)
lb4.place(x=150,y=450)
lb5.place(x=150,y=500)
lb6.place(x=150,y=550)
e.place(x=430,y=250)
e1.place(x=430,y=300)
e2.place(x=430,y=350)
e3.place(x=430,y=400)
e4.place(x=430,y=450)
e5.place(x=430,y=500)
e6.place(x=430,y=550)
v=["Department","Salary_sab","Country"]
combo=Combobox(root,values=v,width=15)
combo.place(x=450,y=750)
button=Button(root,text="Group display",command=print_me)
button.place(x=600,y=750)
B = Button(root, text ="create", command = create)
ins = Button(root, text ="Insert", command = Insert)
dis = Button(root, text ="Display", command = Display)
B.place(x=150,y=750)
ins.place(x=220,y=750)
dis.place(x=320,y=750)
print(sname.get())
root.mainloop()