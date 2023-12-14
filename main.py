from tkinter import *

window = Tk()
window.geometry('300x600')
window.config(bg="light grey")
window.title("SECRET TEXT")
FONT = ('Comic Sans' , 15 , 'normal')
Var = IntVar()

def rest_button():
    enter1.delete(0,'end')
    enter2.delete(0,'end')
    text1.delete(1.0,"end")

def call_back():
    pass

img = PhotoImage(file='topsecret.png')
Label(window,image=img,bg="white").place(x=90,y=0)

label1 = Label(window,text="Enter your secret tittle")
label1.config(bg="light grey",fg="black",font=FONT)
label1.place(x=65,y=120)

enter1 = Entry(window,width=15)
enter1.config(bg="white",fg="black")
enter1.place(x=65,y=145)

label2= Label(window,text="Enter Your Secret ")
label2.config(bg="light grey",fg="black",font=FONT)
label2.place(x=65,y=185)

text1= Text(window,width=20,height=10)
text1.config(bg="white",fg="black")
text1.place(x=65,y=210)

label3= Label(window,text="Enter Master Key ")
label3.config(bg="light grey",fg="black",font=FONT)
label3.place(x=65,y=370)

enter2 = Entry(window,width=15)
enter2.config(bg="white",fg="black")
enter2.place(x=65,y=395)

re_bt = Button(window,text="Delete",font=FONT,command=rest_button,width=3)
re_bt.place(x=65,y=550)

sa_bt = Button(window,text="Save",font=FONT,command=Var,width=3)
sa_bt.place(x=65,y=500)

ca_bck = Button(window,text="Call Back",font=FONT,command=call_back(),width=5)
ca_bck.place(x=65,y=450)

exit_bt = Button(window,text="EXİT",command=lambda:window.destroy())
exit_bt.place(x=200,y=550)

window.mainloop()