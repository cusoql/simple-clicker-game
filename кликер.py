import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import *



root = tk.Tk()

root.geometry('800x600')
root.resizable(False, False)
root.configure(bg = "#052F6D")
root.title("Кликер - $")


n = 0
p = 1
f = 100
f1 = 1000
f2 = 100000
ff = 10000
ps = 1

def Add():
    global n
    global p

    # n = n + p
    n +=p
    if n <= 0:
        lb["text"] = " $" + str(n) 
    else:
        lb["text"] = " $" + str(n)

    pass


def Upgrade100():
    global f
    global p
    global n
    '''условие на прокачку'''
    # p = 0
    # f = 2

    # f = upgrade * 2
    # f = upgrade * 1.5

    if n >= f:
        n = n - f
        # lb['text'] = " $" +  str(n)
        p +=1
        lb['text'] = " $" + str(n)
        f *=2
        btn6['text'] = " Улучшение " + str(f) + ": +1"

        # n >= f:
    elif n < f:
        lb["text"] = "Недостаточно денек"

    pass

def Upgrade1000():
    global f1
    global p
    global n



    if n >= f1:
        n = n - f1
        p +=100
        lb['text'] = " $" + str(n)
        f1 *=2
        btn1['text'] = " Улучшение " + str(f1) + ": +100"

    elif n < f1:
        lb["text"] = "Недостаточно денек"

    pass

def Upgrade10001():
    global f2
    global p
    global n

    if n >= f2:
        n = n - f2
        p +=1000
        lb['text'] = " $" + str(n)
        f2 *= 2
        btn2['text'] = " Улучшение " + str(f2) + ": +1000"
    elif n < f2:
        lb["text"] = "Недостаточно денек"


def PerSecond():
    global ff
    global ps
    global n

    if n >= ff:
        n = n - ff

        # root.after(1000, s)
        ff *= 2
        btn3['text'] = " Улучшение  " + str(ff) + ": +1/s"
    elif n < ff:
        lb["text"] = "Недостаточно денек"


def Tick():
    global ps, n

    n +=ps
    lb['text'] = " $" + str(n)
    root.after(1000, Tick )
    pass

def ob():
    Tick()
    PerSecond()
    pass
# def vixod():
#     return mainloop()
lb = tk.Label(root, bg="#052F6D", height=3, width=20, highlightthickness=0, text="$0", font=("calibre", 32, "bold"), )
lb.place(x = 150 , y = 20)

# lb2 = tk.Label(root, bg="cyan", height=3, width=10, highlightthickness=0, text="$0/s", font=("calibre", 22, "bold"))
# lb2.place(x = 300 , y = 40)

s = Style()

s.configure('TButton', font = ('calibri', 18 , 'bold') )
s.map('TButton', foreground = [('active', '!disabled', 'black')],
                     background = [('active', 'black')])

btn = Button(root, text="Денек добавить", command=Add)
btn.place(x = 250, y =150) 


btn1 = Button(root, text="Улучшение 1000: +100", command=Upgrade1000)
btn1.place(x = 250, y =250)

btn2 = Button(root, text="Улучшение 100000: +1000", command=Upgrade10001)
btn2.place(x = 250, y =300)

btn3 = Button(root, text="Улучшение 10000: +1/s", command=ob)
btn3.place(x = 250, y =350)

btn4 = Button(root, text="Улучшение 200000: +5/s", command=None)
btn4.place(x = 250, y =400)

btn5 = Button(root, text="Улучшение 1000000: +10/s", command= None)
btn5.place(x = 250, y =450)

btn6 = Button(root, text="Улучшение 100: +1", command=Upgrade100)
btn6.place(x = 250, y =200)




root.mainloop()