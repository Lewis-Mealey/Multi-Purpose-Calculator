from tkinter import * 

picture = Tk()
picture.title("Menu help")

def menu():
    picture.destroy()
    import main_menu

canvas = Canvas(picture, width = 893, height = 605)
exitprog=Button(picture,fg="red",font=("Arial Rounded MT Bold", 30),text="QUIT",bg="grey",command=menu).pack(fill=X)

image = PhotoImage(file = "main_help.PNG")

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

picture.mainloop()
