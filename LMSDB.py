import sqlite3
from tkinter import *
from tkinter import messagebox

class AddBook:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        self.l1=Label(self.root,text="Enter Book ID")
        self.t1=Entry(self.root,width=20)
        self.l2=Label(self.root,text="Enter Book Name")
        self.t2=Entry(self.root,width=20)
        self.l3=Label(self.root,text="Enter Book Pub.")
        self.t3=Entry(self.root,width=20)
        self.l4=Label(self.root,text="Enter Book QTY")
        self.t4=Entry(self.root,width=20)
        self.b1=Button(self.root,text="Add Book",command=self.save)
        self.l1.place(x=20,y=30)
        self.t1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.t2.place(x=220,y=80)
        self.l3.place(x=20,y=130)
        self.t3.place(x=220,y=130)
        self.l4.place(x=20,y=180)
        self.t4.place(x=220,y=180)
        self.b1.place(x=20,y=230)
        self.root.mainloop()
    def save(self):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("create table if not exists books(id int primary key,name varchar(40),pub varchar(40),qty int)")
        db.execute("insert into books values(?,?,?,?)",(int(self.t1.get()),self.t2.get(),self.t3.get(),int(self.t4.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        self.t1.delete(0,"end")
        self.t2.delete(0,"end")
        self.t3.delete(0,"end")
        self.t4.delete(0,"end")
        
class AddCustomer:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        self.l1=Label(self.root,text="Enter Customer ID")
        self.t1=Entry(self.root,width=20)
        self.l2=Label(self.root,text="Enter Customer Name")
        self.t2=Entry(self.root,width=20)
        self.l3=Label(self.root,text="Enter Customer PNo")
        self.t3=Entry(self.root,width=20)
        self.b1=Button(self.root,text="Add Customer",command=self.save)
        self.l1.place(x=20,y=30)
        self.t1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.t2.place(x=220,y=80)
        self.l3.place(x=20,y=130)
        self.t3.place(x=220,y=130)
        self.b1.place(x=20,y=230)
        self.root.mainloop()
    def save(self):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("create table if not exists customers(id int primary key,name varchar(40),pno varchar(30))")
        db.execute("insert into customers values(?,?,?)",(int(self.t1.get()),self.t2.get(),self.t3.get()))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        self.t1.delete(0,"end")
        self.t2.delete(0,"end")
        self.t3.delete(0,"end")
class IssueBook:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        self.l1=Label(self.root,text="Enter Transaction ID")
        self.t1=Entry(self.root,width=20)
        self.l2=Label(self.root,text="Enter Book Id")
        self.t2=Entry(self.root,width=20)
        self.l3=Label(self.root,text="Enter Customer ID")
        self.t3=Entry(self.root,width=20)
        self.l4=Label(self.root,text="Enter Date")
        self.t4=Entry(self.root,width=20)
        
        self.b1=Button(self.root,text="Issue",command=self.save)
        self.l1.place(x=20,y=30)
        self.t1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.t2.place(x=220,y=80)
        self.l3.place(x=20,y=130)
        self.t3.place(x=220,y=130)
        self.l4.place(x=20,y=180)
        self.t4.place(x=220,y=180)
        
        self.b1.place(x=20,y=230)
        self.root.mainloop()
    def checkbookid(self):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("create table if not exists books(id int primary key,name varchar(40),pub varchar(40),qty int)")
        cursor=db.execute("select * from books where id=?",(int(self.t2.get()),))
        records=cursor.fetchall()
        if len(records)==0:
            db.close()
            return False
        else:
            print(records)
            print(type(records))
            
            
            s=int(records[0][3])
            db.close()
            if s>0:
                return True
            else:
                return False
    def checkcustomerid(self):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("create table if not exists customers(id int primary key,name varchar(40),pno varchar(30))")
        cursor=db.execute("select * from customers where id=?",(int(self.t3.get()),))
        records=cursor.fetchall()
        if len(records)==0:
            db.close()
            return False
        else:
            db.close()
            return True
    def updateqty(self):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("update books set qty=qty-1 where id=?",(int(self.t2.get()),))
        db.commit()
        db.close()
      
    def save(self):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("create table if not exists trans(id int primary key,bid int,cid int,idate varchar(50),rdate varchar(50))")
        
        if self.checkbookid()==False:
            messagebox.showinfo("Error","Sorry invalid id or insufficient copies")
            return
        if self.checkcustomerid()==False:
            messagebox.showinfo("Error","Sorry invalid id")
            return
        self.updateqty()
        
        db.execute("insert into trans values(?,?,?,?,?)",(int(self.t1.get()),int(self.t2.get()),int(self.t3.get()),self.t4.get(),"NA"))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        self.t1.delete(0,"end")
        self.t2.delete(0,"end")
        self.t3.delete(0,"end")
        self.t4.delete(0,"end")
        

class ReturnBook:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        self.l1=Label(self.root,text="Enter Transaction ID")
        self.t1=Entry(self.root,width=20)
        self.l2=Label(self.root,text="Enter Date")
        self.t2=Entry(self.root,width=20)
        self.b1=Button(self.root,text="Issue",command=self.save)
        self.l1.place(x=20,y=30)
        self.t1.place(x=220,y=30)
        self.l2.place(x=20,y=80)
        self.t2.place(x=220,y=80)
        self.b1.place(x=20,y=230)
        self.root.mainloop()
    def checktransid(self):
        db=sqlite3.connect("e:\\lms7.db")
        cursor=db.execute("select * from trans where id=?",(int(self.t1.get()),))
        records=cursor.fetchall()
        if len(records)==0:
            db.close()
            return -1
        else:
            return int(records[0][1])
    def updateqty(self,id):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("update books set qty=qty+1 where id=?",(id,))
        db.commit()
        db.close()
      
    def save(self):
        db=sqlite3.connect("e:\\lms7.db")
        bid=self.checktransid()
        if bid==-1:
            messagebox.showinfo("Error","Sorry invalid id")
            return
        self.updateqty(bid)
        db.execute("update trans set rdate=? where id=?",(self.t2.get(),int(self.t1.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Data Saved")
        



class Defaulters:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        db=sqlite3.connect("e:\\lms7.db")
        cursor=db.execute("select * from trans where rdate='NA'")
        records=cursor.fetchall()
        self.l=Listbox(self.root)
        for row in records:
            bname=self.getbookname(int(row[1]))
            c=self.getcustdetails(int(row[2]))
            cname=c[0]
            pno=c[1]
            self.l.insert("end",bname+"-"+cname+"--"+pno)
        db.close()
        self.l.place(x=30,y=60)
        self.root.mainloop()
        
    def getbookname(self,id):
        db=sqlite3.connect("e:\\lms7.db")
        db.execute("create table if not exists books(id int primary key,name varchar(40),pub varchar(40),qty int)")
        cursor=db.execute("select * from books where id=?",(id,))
        records=cursor.fetchall()
        name=records[0][1]
        db.close()
        return name
    def getcustdetails(self,id):
        db=sqlite3.connect("e:\\lms7.db")
        cursor=db.execute("select * from customers where id=?",(id,))
        records=cursor.fetchall()
        name=records[0][1]
        pno=records[0][2]
        db.close()
        return (name,pno)
    
        

def addbook():
    a=AddBook()
def addcustomer():
    a=AddCustomer()
def issuebook():
    o=IssueBook()
def returnbook():
    r=ReturnBook()
def dispdefaulters():
    d=Defaulters()


root=Tk()
root.geometry("500x500")
b1=Button(text="Add Book",command=addbook)
b2=Button(text="Add customer",command=addcustomer)
b3=Button(text="Issue Book",command=issuebook)
b4=Button(text="Return Book",command=returnbook)
b5=Button(text="Defaulter",command=dispdefaulters)
b1.place(x=30,y=50)
b2.place(x=30,y=100)
b3.place(x=30,y=150)
b4.place(x=30,y=200)
b5.place(x=30,y=250)
root.mainloop()
