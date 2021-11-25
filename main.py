from tkinter import *
from tkinter import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab
window = Tk()
window.state("zoomed")
window.title("Paint App project(team)")

#variables
eraser_color = "white"
pen_color = "black"
#canvas
canvas =Canvas(window, bg="white",bd=5, relief=GROOVE, height=640, width=1500)
canvas.place(x=12, y=120)

#function

def canvas_color():
    global eraser_color
    color = colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color = color[1]

def saved():
    file_name = filedialog.asksaveasfile(defaultextension=".jpg")
    x= window.winfo_rootx() + canvas.winfo_x()
    y= window.winfo_rooty() + canvas.winfo_y()
    x1= x + canvas.winfo_width()
    y1= y + canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("Notification Paint", "L'image a été sauvegardée" + str(file_name))


def eraser():
    global pen_color
    pen_color = eraser_color
def clear():
    canvas.delete("all")

def paint(event):
    x1,y1 = (event.x-2),(event.y-2)
    x2,y2 = (event.x+2),(event.y+2),
    canvas.create_oval(x1,y1,x2,y2, fill=pen_color, outline=pen_color, width=pen_size.get())

canvas.bind("<B1-Motion>",paint)

def select_color(col):
    global  pen_color
    pen_color = col

#frame(cadre)
color_frame = LabelFrame(window, text="Couleur", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
color_frame.place(x=10, y=10, width=426, height=60)

tool_frame = LabelFrame(window, text="Outils", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
tool_frame.place(x=450, y=10, width=230, height=60)

pen_size = LabelFrame(window, text="Taille", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
pen_size.place(x=750, y=10, width=224, height=70)

#Color(couleurs)
#           red       purple     pink      orange     yellow      green     blue         aquamarine      white     black       grey     skyblue

colors = ["#FF0000", "#800080","#FFC0CB", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#A52A2A", "#FFFFFF", "#000000", "#808080", "#ADD8E6" ]


#Button(bouttons)
i=j=0
for color in colors:
    Button(color_frame, bd=3,  bg=color, relief=RIDGE, width=3, command=lambda col=color:select_color(col)).grid(row=j, column=i, padx=1)
    i=1+i

#Tool_button(Bouttons outils)

canvas_color_b = Button(tool_frame, text="Toile", command=canvas_color, relief=RIDGE)
canvas_color_b.grid(row=0, column=0, padx=2)

save_b2 =Button(tool_frame, text="Enregistrer", command=saved, relief=RIDGE)
save_b2.grid(row=0, column=1, padx=2)

eraser_b3 = Button(tool_frame, text="Effacer", command=eraser, relief=RIDGE)
eraser_b3.grid(row=0, column=2, padx=2)

clear_4 =Button(tool_frame, text="Nettoyer", command=clear, relief=RIDGE)
clear_4.grid(row=0, column=3, padx=2)

#Pen and eraser(Stylet et effaceur)
pen_size = Scale(pen_size, orient=HORIZONTAL, from_=0, to=50, length=170)
pen_size.set(1)
pen_size.grid(row=0, column=0)

window.mainloop()


#
