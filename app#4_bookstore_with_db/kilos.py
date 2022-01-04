from tkinter import *

window = Tk()

def kilos_to_pounds_etc():
    for el in list(e1_value.get()):
         if el.isalpha:
            t1.delete("1.0", END)
            t1.insert(END,"wrong vaule")
            t2.delete("1.0", END)
            t2.insert(END,"wrong vaule")
            t3.delete("1.0", END)
            t3.insert(END,"wrong vaule")

    gramms = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, gramms)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

b1 = Button(window,text="Convert",command=kilos_to_pounds_etc)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

l1 = Label(window, text="Kg", height=1, width=10)
l1.grid(row=0,column=1)

l2 = Label(window, text="Gramms", height=1, width=10)
l2.grid(row=1,column=1)

l3 = Label(window, text="Pounds", height=1, width=10)
l3.grid(row=1,column=3)

l4 = Label(window, text="Ounces", height=1, width=10)
l4.grid(row=1,column=5)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=2)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=4)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=6)

window.mainloop()
