import tkinter as tk

calc= tk.Tk()
calc.title("Fuel calculator")

window = tk.Canvas(calc, width = 400, height = 400,  relief = 'raised')
window.pack()

def menu():
    calc.destroy()
    import main_menu

def helpo():
    from subprocess import Popen
    Popen('python fuel_economy_help.py')

#1########################################################################

label1 = tk.Label(calc, text='Fuel Economy Calculator')
label1.config(font=('helvetica', 14))
window.create_window(200, 25, window=label1)

label2 = tk.Label(calc, text='Distance (Miles)')
label2.config(font=('helvetica', 10))
window.create_window(200, 100, window=label2)

label3 = tk.Label(calc, text='Fuel used (Gallons)')
label3.config(font=('helvetica', 10))
window.create_window(200, 150, window=label3)

label5 = tk.Label(calc, text='Miles per gallon')
label5.config(font=('helvetica', 10))
window.create_window(200, 300, window=label5)

label6 = tk.Button(calc, text='Exit',command=menu)
label6.config(font=('helvetica', 10))
window.create_window(375,25, window=label6)

help = tk.Button(calc, text='Help',command=helpo)
help.config(font=('helvetica', 10))
window.create_window(335,25, window=help)

#########################################################################

entry1 = tk.Entry (calc) 
window.create_window(200, 120, window=entry1)

entry2 = tk.Entry (calc) 
window.create_window(200, 170, window=entry2)

#########################################################################

def mortageamount ():
    
    x1 = entry1.get()

    x2 = entry2.get()

    florb = eval(x1)/eval(x2)
    
    fueltotal = tk.Label(calc, text= round(florb,2),font=('helvetica', 10, 'bold'))
    window.create_window(200, 320, window=fueltotal)

#########################################################################

button1 = tk.Button(text='Calculate', command=mortageamount, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
window.create_window(200, 260, window=button1)

calc.mainloop()
