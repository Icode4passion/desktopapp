"""
A desktop app to store
Name ,DOB ,Phone-Number, and BloodGroup

View
Search
Add
Update
Delete
Close

Actions are performed


"""


from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tupil
        index=list1.curselection()[0]
        selected_tupil=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tupil[1])
        e2.delete(0,END)
        e2.insert(END,selected_tupil[2])
        e3.delete(0,END)
        e3.insert(END,selected_tupil[3])
        e4.delete(0,END)
        e4.insert(END,selected_tupil[4])
    except:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(Name_text.get(),DOB_text.get(),Phone_text.get(),Blood_group_text.get()):
        list1.insert(END,row)

def add_entry_command():
    backend.insert(Name_text.get(),DOB_text.get(),Phone_text.get(),Blood_group_text.get())
    list1.delete(0,END)
    list1.insert(END,(Name_text.get(),DOB_text.get(),Phone_text.get(),Blood_group_text.get()))

def update_command():
    backend.update(selected_tupil[0],Name_text.get(),DOB_text.get(),Phone_text.get(),Blood_group_text.get())


def delete_command():
    backend.delete(selected_tupil[0])




window=Tk()

window.wm_title("BioData")

l1 = Label(window,text="Name")
l1.grid(row=0,column=0)

l2 = Label(window,text="DOB")
l2.grid(row=0,column=2)


l3 = Label(window,text="Phone")
l3.grid(row=1,column=0)


l4 = Label(window,text="BloodGroup")
l4.grid(row=1,column=2)

Name_text = StringVar()
e1 = Entry(window,textvariable=Name_text)
e1.grid(row=0,column=1)


DOB_text = StringVar()
e2 = Entry(window,textvariable=DOB_text)
e2.grid(row=0,column=3)


Phone_text = StringVar()
e3 = Entry(window,textvariable=Phone_text)
e3.grid(row=1,column=1)


Blood_group_text = StringVar()
e4 = Entry(window,textvariable=Blood_group_text)
e4.grid(row=1,column=3)


list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_entry_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b6=Button(window,text="Delete",width=12,command=delete_command)
b6.grid(row=6,column=3)

b7=Button(window,text="Close",width=12,command=window.destroy)
b7.grid(row=7,column=2)



window.mainloop()
