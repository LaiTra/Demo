
from googletrans import Translator
from tkinter import*
from PIL import ImageTk, Image

root =Tk()
root.title("GOOGLETRANS")
root.geometry('400x600')

#chèn ảnh vào giao diện 
load = Image.open(r"C:\Users\My computer\Downloads\bg.PNG")
resize =load.resize((400,400), Image.ANTIALIAS)    #chỉnh kích cỡ của ảnh
render= ImageTk.PhotoImage(resize)     
img= Label(root, image=render)
img.place(x=0,y=0)


name= Label(root, text="Translator",font= ("Times New Roman",30),bg= '#FC7F2D',fg = 'black', bd=0 )
name.place(x=128,y=10)

button_frame=Frame(root).pack(side=BOTTOM)

# tạo xóa cho nút
def xoa():
    box.delete(1.0,END)
    box1.delete(1.0,END)

#tạo dịch cho nút
def dich():
    INPUT=box.get(1.0,END)
    print(INPUT)
    t=Translator()
    a=t.translate(INPUT,src='vi',dest='en')
    b=a.text
    box1.insert(END,b)
                    
# tạo box
box=Text(width=20, height=5, font=("Times New Roman",16))
box.pack(pady=80)
box1=Text(width=20, height=5, font=("Times New Roman",16))
box1.pack(pady=70)


#tạo nút
button= Button(button_frame,text ='translator',font =("Times New Roman",20),command=dich)
button.place(x=200,y=250)

clear_button=Button(button_frame,text="clear",font=("Times New Roman",20),fg='black',command=xoa)
clear_button.place(x=80,y=250)



root.mainloop()