from tkinter import * 

picture = Tk()
picture.title("Mortgage help")

def menu():
    picture.destroy()

canvas = Canvas(picture, width = 1268, height = 844)
exitprog=Button(picture,fg="red",font=("Arial Rounded MT Bold", 30),text="QUIT",bg="grey",command=menu).pack(fill=X)

image = PhotoImage(file = "mortgage_help.PNG")

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

picture.mainloop()
