import tkinter as tk

calc= tk.Tk()
calc.title("Vehicle calculator")

window = tk.Canvas(calc, width = 400, height = 400,  relief = 'raised')
window.pack()

def menu():
    calc.destroy()
    import main_menu

def helpo():
    from subprocess import Popen
    Popen('python vehicle_calculator_help.py')

#########################################################################

label1 = tk.Label(calc, text='Vehicle Calculator')
label1.config(font=('helvetica', 14))
window.create_window(200, 25, window=label1)

label2 = tk.Label(calc, text='Vehicle amount')
label2.config(font=('helvetica', 10))
window.create_window(200, 100, window=label2)

label3 = tk.Label(calc, text='Interest rate monthly (%)')
label3.config(font=('helvetica', 10))
window.create_window(200, 150, window=label3)

label4 = tk.Label(calc, text='Payment period (years)')
label4.config(font=('helvetica', 10))
window.create_window(200, 200, window=label4)

label5 = tk.Label(calc, text='Monthly payments')
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

entry3 = tk.Entry (calc) 
window.create_window(200, 220, window=entry3)

#########################################################################

def mortageamount ():
    
    x1 = entry1.get()

    x2 = entry2.get()

    x3 = entry3.get()

    amountpayments = eval(x3)*12
    monthly_interest = eval(x2)/(100 * 12)    
    monthly_payment = eval(x1) * ( monthly_interest / (1 - (1 + monthly_interest) ** (- amountpayments)))
    
    vehicletotal = tk.Label(calc, text= round(monthly_payment,2),font=('helvetica', 10, 'bold'))
    window.create_window(200, 320, window=vehicletotal)

#########################################################################

button1 = tk.Button(text='Calculate', command=mortageamount, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
window.create_window(200, 260, window=button1)

calc.mainloop()
