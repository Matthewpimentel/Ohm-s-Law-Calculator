from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from idlelib import window
import math
Frame = Tk()

Frame.title("Ohm's Law")

Frame.geometry ("400x250")

    
Enter = tk.Label ( text ="Enter at least 2 values to get the other values")
Enter.place(x=5,y=5)


Resistance = Label(text="Resistance Ω")
Resistance.place(x=75,y=50)

Current = Label(text="Current A")
Current.place(x=75,y=80)

Voltage= Label(text="Voltage V")
Voltage.place(x=75,y=110)

Power= Label(text="Power W")
Power.place(x=75,y=140)

R1=IntVar()
R = Entry(textvariable = R1)
R.place(x=150,y=50)

A1=IntVar()
A = Entry(textvariable = A1)
A.place(x=150,y=80)

V1=IntVar()
V = Entry(textvariable = V1)
V.place(x=150,y=110)

P1=IntVar()
P = Entry(textvariable = P1)
P.place(x=150,y=140)


def Calc():
    
    
    if int(A.get()) > 0 and int(R.get()) > 0:
        V.delete(0)
        Vresult= (R1.get() * A1.get())
        V.insert(0,Vresult)
        P.delete(0)
        Presult= (Vresult * A1.get())
        P.insert(0,Presult)
        
        
    elif int(A.get()) > 0 and int(V.get()) > 0:
        P.delete(0)
        Presult = (V1.get() * A1.get())
        P.insert(0,Presult)
        R.delete(0)
        Rresult = (V1.get() / A1.get())
        R.insert(0,Rresult)
        
    
    elif int(A.get()) > 0 and int(P.get()) > 0: 
        R.delete(0)
        Rresult = (P1.get() / (A1.get()**2))
        R.insert(0,Rresult)
        V.delete(0)
        Vresult = (P1.get() / A1.get())
        V.insert(0,Vresult)

    elif int(V.get()) > 0 and int(P.get()) > 0: 
        A.delete(0)
        Aresult = (P1.get() / V1.get())
        A.insert(0,Aresult)
        R.delete(0)
        Rresult = ((V1.get()**2) / P1.get())
        R.insert(0,Rresult)
    
    elif int(V.get()) > 0 and int(R.get()) > 0:
        P.delete(0)
        Presult = ((V1.get()**2) / R1.get())
        P.insert(0,Presult)
        A.delete(0)
        Aresult = ((V1.get() / R1.get()))
        A.insert(0,Aresult)
    
    elif int(P.get()) > 0 and int(R.get()) > 0:
        V.delete(0)
        Vresult = math.sqrt((P1.get() * R1.get()))
        V.insert(0,Vresult)
        
        
        
def Reset():
        R.delete(first=0, last=999999999)
        A.delete(first=0, last=999999999)
        V.delete(first=0, last=999999999)
        P.delete(first=0, last=999999999)
        R.insert(0,0)
        A.insert(0,0)
        V.insert(0,0)
        P.insert(0,0)        
    


Calcbutton = Button(Frame, text="Calculate", command=Calc)
Calcbutton.place(x=300,y=180)

Resetbutton = Button(Frame, text="Reset", command=Reset)
Resetbutton.place(x=25,y=180)

Frame.mainloop()