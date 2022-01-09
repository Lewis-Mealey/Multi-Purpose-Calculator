from tkinter import *
import math

calc = Tk()
calc.title("Simple Calculator")
operator=""
userinput=StringVar()

#Defines what happens whenever a number or symbol is clicked
def click(numbers):
    global operator
    operator=operator+str(numbers)
    userinput.set(operator)

#Adds the numbers on the screen using whatever the user inputed
def clickequals():
    global operator
    sumtotal=str(eval(operator))
    userinput.set(sumtotal)
    operator=""

#Makes the enter screen blank
def clickclear():
    global operator
    operator=""
    userinput.set("")

def menu():
    calc.destroy()
    import main_menu

def helpo():
    from subprocess import Popen
    Popen('python calculator_help.py')

#############################################################################################################################################################################################

output=Entry(calc,font=("Arial Rounded MT Bold", 30),textvariable=userinput,bd=18,insertwidth=4,bg="grey",justify="right").grid(columnspan=3)

exitprog=Button(calc,fg="red",font=("Arial Rounded MT Bold", 30),text="QUIT",bg="grey",command=menu).grid(row=0,column=3)

helpen=Button(calc,fg="red",font=("Arial Rounded MT Bold", 30),text="HELP",bg="grey",command=helpo).grid(row=0,column=4)

#############################################################################################################################################################################################

num7=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="7",bg="grey",command=lambda:click(7)).grid(row=1,column=0)

num8=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="8",bg="grey",command=lambda:click(8)).grid(row=1,column=1)

num9=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="9",bg="grey",command=lambda:click(9)).grid(row=1,column=2)

numplus=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="+",bg="grey",command=lambda:click("+")).grid(row=1,column=3)

sqroot=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="√",bg="grey",command=lambda:click("math.sqrt(")).grid(row=1,column=4)

#############################################################################################################################################################################################

num4=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="4",bg="grey",command=lambda:click(4)).grid(row=2,column=0)

num5=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="5",bg="grey",command=lambda:click(5)).grid(row=2,column=1)

num6=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="6",bg="grey",command=lambda:click(6)).grid(row=2,column=2)

numminus=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="-",bg="grey",command=lambda:click("-")).grid(row=2,column=3)

#openbracket=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="(",bg="grey",command=lambda:click("(")).grid(row=2,column=4)

#############################################################################################################################################################################################

num1=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="1",bg="grey",command=lambda:click(1)).grid(row=3,column=0)

num2=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="2",bg="grey",command=lambda:click(2)).grid(row=3,column=1)

num3=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="3",bg="grey",command=lambda:click(3)).grid(row=3,column=2)

nummult=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="*",bg="grey",command=lambda:click("*")).grid(row=3,column=3)

closedbracket=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text=")",bg="grey",command=lambda:click(")")).grid(row=3,column=4)

#############################################################################################################################################################################################
    
num0=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="0",bg="grey",command=lambda:click(0)).grid(row=4,column=0)

numclear=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="C",bg="grey",command=clickclear).grid(row=4,column=1)

numequals=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="=",bg="grey",command=clickequals).grid(row=4,column=2)

numdivide=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="/",bg="grey",command=lambda:click("/")).grid(row=4,column=3)

power=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text="^",bg="grey",command=lambda:click("**")).grid(row=4,column=4)

decimal=Button(calc,bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),text=".",bg="grey",command=lambda:click(".")).grid(row=2,column=4)

#############################################################################################################################################################################################

calc.mainloop()
