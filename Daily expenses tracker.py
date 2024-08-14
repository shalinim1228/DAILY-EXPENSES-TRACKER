from tkinter import *

from tkinter import messagebox, ttk

win=Tk()

win.title("page")

win.geometry("1920x1080")

win.config(bg="#800000")

f1=Frame(win,bg="#ffff00")

f1.pack(side=TOP,fil=X)

l1=Label(f1,text="DAILY EXPENSES TRACKER",font=("times",18,"bold"))

l1.grid(row=0,columnspan=2,padx=10,pady=10,sticky="w")

l2=Label(f1,text="Price",font=("times",14,"bold"))

l2.grid(row=1,column=0,padx=10,pady=10,sticky="w")

e1=Entry(f1,width=30)

e1.grid(row=1,column=1,padx=10,pady=10,sticky="w")

l3=Label(f1,text="Date",font=("times",14,"bold"))

l3.grid(row=1,column=2,padx=10,pady=10,sticky="w")

e2=Entry(f1,width=30)

e2.grid(row=1,column=3,padx=10,pady=10,sticky="w")

l4=Label(f1,text="Category",font=("times",14,"bold"))

l4.grid(row=2,column=0,padx=10,pady=10,sticky="w")

c1=ttk.Combobox(f1,width=30,state="read only")
c1["values"]=("travel","food","gift","coffee")
c1.grid(row=2,column=1,padx=10,pady=10,sticky="w")

l5=Label(f1,text="Payment",font=("times",14,"bold"))

l5.grid(row=2,column=2,padx=10,pady=10,sticky="w")

c2=ttk.Combobox(f1,width=30,state="read only")
c2["values"]=("Cash","Upi","Card")
c2.grid(row=2,column=3,padx=10,pady=10,sticky="w")

f2=Frame(f1,bg="orange")

f2.grid(row=3,columnspan=4,padx=10,pady=10)

b1=Button(f2,text="INSERT")
b1.grid(row=0,column=1,padx=10,pady=10)

b2=Button(f2,text="DELETE")
b2.grid(row=0,column=2,padx=10,pady=10)

b3=Button(f2,text="UPDATE")
b3.grid(row=0,column=3,padx=10,pady=10)

b4=Button(f2,text="CLEAR")
b4.grid(row=0,column=4,padx=10,pady=10)

win.mainloop()