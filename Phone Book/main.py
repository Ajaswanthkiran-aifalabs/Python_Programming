from tkinter import Tk,Entry,Label,Toplevel,Button,Text,messagebox
import tkinter as tk
import os
import json
def saveToFile(name,no,insert_top):

    data=get_all_fun()

    print(data)

    if name in data:
        mssgbox=messagebox.showerror(message="The name is already present in the Dictionary")

    else:
        with open("phone_book.txt","+a") as f:
            
            f.write(f'"{name}":{no},')

        insert_top.destroy()



def get_all_fun():

    with open("phone_book.txt","r") as f:

        data=f.read()

    data=data[:len(data)-1]
    d="{"+data+"}"

    dct=json.loads(d)

    return dct

def get_all():

    dct=get_all_fun()

    display=Toplevel()

    t=Text(display)
    t.insert(tk.END,dct)
    t.pack()


def goUpdate(name,ph,kk):
   
    dct=get_all_fun()

    dct[name]=ph

    dct_str=""
    for i,j in dct.items():

        dct_str+=f'"{i}":{j},'

    with open("phone_book.txt","w") as f:
        f.write(dct_str)

    kk.destroy()
    

def goDelete(name,kk):
   
    dct=get_all_fun()

    dct.pop(name)

    dct_str=""
    for i,j in dct.items():

        dct_str+=f'"{i}":{j},'

    with open("phone_book.txt","w") as f:
        f.write(dct_str)

    kk.destroy()
def update():
    

    
    update=Toplevel()
    update.geometry("300x300")

    t=Label(update,text="Enter name")
    t.place(x=10,y=10)
    e=Entry(update)
    e.place(x=150,y=10)
    numt=Label(update,text="Enter Phone No to update")
    numt.place(x=10,y=50)
    nume=Entry(update)
    nume.place(x=150,y=50)

    b=Button(update,text="Click to update",command=lambda: goUpdate(e.get(),nume.get(),update))
    b.place(x=120,y=90)



def insert():
    insert_top=Toplevel()
    insert_top.title("Insert Window")
    insert_top.geometry("400x400")
    nameLabel=Label(insert_top,text="Name:")
    nameLabel.place(x=10,y=10)
    
    name=Entry(insert_top)

    name.place(x=80,y=10)

    numLabel=Label(insert_top,text="Phone No:")
    numLabel.place(x=10,y=30)
    
    num=Entry(insert_top)

    num.place(x=80,y=30)

    button=Button(insert_top,text="Click to save",command=lambda: saveToFile(name.get(),num.get(),insert_top))
    button.place(x=120,y=50)

    
def delete():

    delete=Toplevel()
    delete.geometry("300x300")

    t=Label(delete,text="Enter name To delete")
    t.place(x=10,y=10)
    e=Entry(delete)
    e.place(x=150,y=10)
    

    b=Button(delete,text="Click to Delete",command=lambda: goDelete(e.get(),delete))
    b.place(x=120,y=90)

def goSearch(value,ss):

    dct=get_all_fun()
    s=str(value)+": "
    if value.isnumeric():
        for i,j in dct.items():
            if int(value)==j:
                s+=str(i)+","
    else:
        s+=str(dct[value])

    
    s=messagebox.showinfo(message=s)
    ss.destroy()

def searchName():

    search=Toplevel()
    search.geometry("300x300")

    t=Label(search,text="Enter name/phone number to search")
    t.place(x=10,y=10)
    e=Entry(search)
    e.place(x=150,y=10)
    

    b=Button(search,text="Click to Search",command=lambda: goSearch(e.get(),search))
    b.place(x=120,y=90)
def main():

    top=Tk()

    top.geometry("300x300")
    top.title("Phone Book")

    
    save=Button(text="Save",command=insert)
    save.place(x=10,y=10)

    display=Button(text="Retrieve",command=get_all)
    display.place(x=10,y=40)

    up=Button(text="Update",command=update)
    up.place(x=10,y=70)


    dele=Button(text="Delete",command=delete)
    dele.place(x=10,y=100)


    search=Button(text="Search",command=searchName)
    search.place(x=10,y=130)

    top.mainloop()

    

if __name__=="__main__":
    main()