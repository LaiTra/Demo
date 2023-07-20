from tkinter import*
from tkinter.ttk import*

root = Tk()
root.title("comboBox")
root.geometry('300x300')

#tao label

label= Label(root, text ='fruits list', font = ('Times New Roman', 15))
label.place(x=20, y=30)

#tạo comboBox
combo = Combobox(root , font=('Times New Roman',15), width=15)
combo['value'] = ('cà rốt', 'cà chua', 'rau má', 'lá ngón')
combo.current(3)
combo.place(x=110,y=30)

#tao button
def click():
    name=Label(root, text= 'your choice : ' + combo.get(), font = ("Times New Roman",15))
    name.place(x=20, y=110)
button = Button(root, text= "click here!", command=click)
button.place(x=100,y=80)
root.mainloop()