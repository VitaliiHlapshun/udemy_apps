from tkinter import *
import backend


def view_func():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        print(selected_tuple)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def search_func():
    list1.delete(0, END)
    for row in backend.search(text_title.get(), year.get(), text_author.get(), isbn.get()):
        list1.insert(END, row)


def add_func():
    backend.insert(text_title.get(), year.get(), text_author.get(), isbn.get())
    list1.delete(0, END)
    list1.insert(0, (text_title.get(), year.get(), text_author.get(), isbn.get()))


def delete_record():
    backend.delete(selected_tuple[0])

def update_record():
    backend.update(selected_tuple[0], text_title.get(), year.get(), text_author.get(), isbn.get())


window = Tk()

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Year')
l2.grid(row=1, column=0)

l3 = Label(window, text='Author')
l3.grid(row=0, column=2)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

text_title = StringVar()
e1 = Entry(window, textvariable=text_title)
e1.grid(row=0, column=1)

year = StringVar()
e2 = Entry(window, textvariable=year)
e2.grid(row=1, column=1)

text_author = StringVar()
e3 = Entry(window, textvariable=text_author)
e3.grid(row=0, column=3)

isbn = StringVar()
e4 = Entry(window, textvariable=isbn)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=25)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

b1 = Button(window, text='View all', height=1, width=10, command=view_func)
b1.grid(row=2, column=3)

b1 = Button(window, text='Search entry', height=1, width=10, command=search_func)
b1.grid(row=3, column=3)

b1 = Button(window, text='Add entry', height=1, width=10, command=add_func)
b1.grid(row=4, column=3)

b1 = Button(window, text='Update', height=1, width=10, command=update_record)
b1.grid(row=5, column=3)

b1 = Button(window, text='Delete', height=1, width=10, command=delete_record)
b1.grid(row=6, column=3)

b1 = Button(window, text='Close', height=1, width=10, command=window.destroy)
b1.grid(row=7, column=3)

window.wm_title("My fucking amazing database")

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=4, sticky="ns")

sb2 = Scrollbar(window, orient='horizontal')
sb2.grid(row=7, column=0, columnspan=2, sticky="ew")

list1.configure(yscrollcommand=sb1.set)
list1.configure(xscrollcommand=sb2.set)
sb1.configure(command=list1.yview)
sb2.configure(command=list1.xview)

window.mainloop()
