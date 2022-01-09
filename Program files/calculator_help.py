from tkinter import * 

picture = Tk()
picture.title("Calculator help")

def menu():
    picture.destroy()

canvas = Canvas(picture, width = 1277, height = 854)
exitprog=Button(picture,fg="red",font=("Arial Rounded MT Bold", 30),text="QUIT",bg="grey",command=menu).pack(fill=X)

image = PhotoImage(file = "calculator_help.PNG")

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

picture.mainloop()
