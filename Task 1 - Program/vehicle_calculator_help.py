from tkinter import * 

picture = Tk()
picture.title("Vehicle help")

def menu():
    picture.destroy()

canvas = Canvas(picture, width = 1211, height = 788)
exitprog=Button(picture,fg="red",font=("Arial Rounded MT Bold", 30),text="                                                      QUIT                                                     ",bg="grey",command=menu).pack()

image = PhotoImage(file = "vehicle_calculator_help.PNG")

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

picture.mainloop()
