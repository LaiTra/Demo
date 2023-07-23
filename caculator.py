from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Caculator basic')
root.geometry('400x400')

#insert image
image = Image.open(r'C:\Users\My computer\Downloads\u.PNG')
resize =image.resize((400,400), Image.ANTIALIAS)    #chỉnh kích cỡ của ảnh
render= ImageTk.PhotoImage(resize)  
img= Label(root, image=render)   
img.place(x=0,y=0)

#them icon
icon = Image.open(r'C:\Users\My computer\Downloads\icon.PNG')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)

nb1_var=StringVar()
nb2_var=StringVar()

#nhap lieu
text= Entry(textvariable=nb1_var,font =('Times New Roman',15),width=20)
text.place(x=140,y=70)
text.focus()

Text1= Entry(textvariable=nb2_var,font =('Times New Roman',15),width=20)
Text1.place(x=140,y=120)

#label
label = Label(text='NUMBER 1:', font =('Times New Roman',15), bg ='#F0F0F0')
label.place(x=10,y=70)
label1 = Label(text='NUMBER 2:', font =('Times New Roman',15), bg ='#F0F0F0')
label1.place(x=10,y=120)

#them chuc nang cho button
def clear():
    entry=nb1_var.get()
    nb1_var.set('')
    entry1=nb2_var.get()
    nb2_var.set('')

def cong():
    cong=Label(root,font=('Times New Roman',15),text='ket qua la:' + str(int(text.get()) + int(Text1.get())), fg='black' )
    cong.place(x=30,y=160) 
    
def tru():
    tru=Label(root,font=('Times New Roman',15),text='ket qua la:' + str(int(text.get()) - int(Text1.get())), fg='black' )
    tru.place(x=30,y=160) 

def nhan():
    nhan=Label(root,font=('Times New Roman',15),text='ket qua la:' + str(int(text.get()) * int(Text1.get())), fg='black' )
    nhan.place(x=30,y=160) 

def chia():
    chia=Label(root,font=('Times New Roman',15),text='ket qua la:' + str(int(text.get()) / int(Text1.get())), fg='black' )
    chia.place(x=30,y=160) 

#button

addition_button = Button(root,activeforeground='white',activebackground='blue',text ='Cộng',font=("Times New Roman",15),command=cong)
addition_button.place(x=120, y=200)

clear_button = Button(text ='Clear',activeforeground='white',activebackground='green',font=("Times New Roman",15),command=clear)
clear_button.place(x=10, y=200)

subtraction_button = Button(text ='Trừ',activeforeground='white',activebackground='yellow',font=("Times New Roman",15),command=tru)
subtraction_button.place(x=200, y=200)

multiplication_button = Button(text ='Nhân',activeforeground='white',activebackground='pink',font=("Times New Roman",15),command=nhan)
multiplication_button.place(x=120, y=250)

division_button = Button(text ='Chia',activebackground='orange',activeforeground='white',font=("Times New Roman",15),command= chia)
division_button.place(x=200, y=250)

root.mainloop()
