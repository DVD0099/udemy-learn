from tkinter import *

window=Tk()

def convert():
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

b1=Button(window, text="convert",command=convert)
b1.grid(row=0,column=3)

e2=Label(window,text="Kg")
e2.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,text="kg",textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window, height=1, width=10)
t1.grid(row=1,column=0)
t2=Text(window, height=1,width=10)
t2.grid(row=1,column=1)
t3=Text(window,height=1,width=10)
t3.grid(row=1,column=2)

window.mainloop()
