import tkinter as tk
import subprocess
from tkinter import *
import os



def calcu():
    from subprocess import Popen
    Popen('python calculator.py')
    menu.destroy()

def fuele():
    from subprocess import Popen
    Popen('python fuel_economy.py')
    menu.destroy()

def mortg():
    from subprocess import Popen
    Popen('python mortgage_calculator.py')
    menu.destroy()

def vehic():
    from subprocess import Popen
    Popen('python vehicle_calculator.py')
    menu.destroy()

def helpo():
    from subprocess import Popen
    Popen('python main_help.py')

def exito():
    menu.destroy()


menu = tk.Tk()
menu.title("Main Menu")


#################################################################################################################################################

calc = tk.Button(menu, bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),bg="grey",text="Calculator", command=calcu).pack(fill=X)
fuel = tk.Button(menu, bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),bg="grey",text="Fuel Calculator", command=fuele).pack(fill=X)
mort = tk.Button(menu, bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),bg="grey",text=" Mortgage Calculator", command=mortg).pack(fill=X)
vehi = tk.Button(menu, bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),bg="grey",text="Vehicle Calculator", command=vehic).pack(fill=X)
help = tk.Button(menu, bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),bg="grey",text="Help", command=helpo).pack(fill=X)
exit = tk.Button(menu, bd=8,padx=16,fg="red",font=("Arial Rounded MT Bold", 30),bg="grey",text="Exit", command=exito).pack(fill=X)

menu.mainloop()
