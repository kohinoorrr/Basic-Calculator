from tkinter import * #Import all from Tkinter

#GUI Interaction
window=Tk()
window.geometry("300x300")
window.config(bg="pink")
window.title("Calculator")

#Creating Entry Box
e=Entry(window,width=57,borderwidth=5)
e.pack()

#Creating Functions

def click(num):
    e.insert(END,str(num))
def add():
    n1=e.get()
    global i
    global s
    s='add'
    i=int(n1)
    e.delete(0,END)
def sub():
    n1=e.get()
    global i
    global s
    i=int(n1)
    s='sub'
    e.delete(0,END)
def mul():
    n1=e.get()
    global i
    global s
    i=int(n1)
    s='mul'
    e.delete(0,END)
def div():
    n1=e.get()
    global i
    global s
    i=int(n1)
    s='div'
    e.delete(0,END)
def equal():
    n2=e.get()
    e.delete(0,END)
    if s == 'add':
        e.insert(0,i+int(n2))
    elif s == 'sub':
        e.insert(0,i-int(n2))
    elif s== 'mul':
        e.insert(0,i*int(n2))
    elif s=='div':
        try:
            e.insert(0,i/int(n2))
        except ZeroDivisionError:
            e.insert(0,"Can't Divide with Zero, Clear and Continue")
def clr():
    e.delete(0,END)
    

#Creating and configuring Buttons
b=Button(window, text='1',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(1),activebackground="blue",activeforeground="pink") #1
b.place(x=10,y=60)
b=Button(window, text='2',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(2),activebackground="blue",activeforeground="pink") #2
b.place(x=80,y=60)
b=Button(window, text='3',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(3),activebackground="blue",activeforeground="pink") #3
b.place(x=140,y=60)
b=Button(window, text='4',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(4),activebackground="blue",activeforeground="pink") #4
b.place(x=10,y=120)
b=Button(window, text='5',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(5),activebackground="blue",activeforeground="pink") #5
b.place(x=80,y=120)
b=Button(window, text='6',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(6),activebackground="blue",activeforeground="pink") #6
b.place(x=140,y=120)
b=Button(window, text='7',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(7),activebackground="blue",activeforeground="pink") #7
b.place(x=10,y=180)
b=Button(window, text='8',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(8),activebackground="blue",activeforeground="pink") #8
b.place(x=80,y=180)
b=Button(window, text='9',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(9),activebackground="blue",activeforeground="pink") #9
b.place(x=140,y=180)
b=Button(window, text='0',width=10,bg="black",fg="pink",font=("bold",12),command = lambda : click(0),activebackground="blue",activeforeground="pink") #0
b.place(x=80,y=240)
b=Button(window, text='=',width=10,bg="black",fg="pink",font=("bold",12),command= equal,activebackground="blue",activeforeground="pink") #=
b.place(x=10,y=240)
b=Button(window, text='Clear',width=10,bg="black",fg="pink",font=("bold",12),command = clr,activebackground="blue",activeforeground="pink") #Clear
b.place(x=140,y=240)
b=Button(window, text='+',width=8,bg="black",fg="pink",font=("bold",12),command = add,activebackground="blue",activeforeground="pink") # +
b.place(x=210,y=60)
b=Button(window, text='-',width=8,bg="black",fg="pink",font=("bold",12),command = sub,activebackground="blue",activeforeground="pink") # - 
b.place(x=210,y=120)
b=Button(window, text='x',width=8,bg="black",fg="pink",font=("bold",12),command = mul,activebackground="blue",activeforeground="pink") # X
b.place(x=210,y=180)
b=Button(window, text='/',width=8,bg="black",fg="pink",font=("bold",12),command = div,activebackground="blue",activeforeground="pink") # /
b.place(x=210,y=240)


window.mainloop()
