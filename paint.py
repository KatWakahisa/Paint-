#from tkinter import *
#import PIL
#from PIL import Image, ImageDraw
#from tkinter.filedialog import asksaveasfile
#from canvas_image import CreateCanvasObject


from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import askcolor
import io
import datetime
import time
import PIL
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw


from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
from math import sqrt
# defined


def save():
        files = [("JPEG images","*.jpg"),
        ("All files", "*.*")]
        filename=asksaveasfile(title="Save image as...",filetypes= files, defaultextension = files)
        image1.save(filename)

def fopen():
	filename = askopenfilename(filetypes=(("All", "*")))

def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y

def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=1)
    draw.line((lastx, lasty, x, y), fill='red', width=1)
    lastx, lasty = x, y

def clear():
    cv.delete('all')


def quit():
    exit()




canvas = Tk()
canvas.title("Paint")
lastx, lasty = None, None

menubar = Menu(canvas)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Recommencer", command = clear)
menu1.add_command(label="Save", command= save)
menu1.add_command(label="Open", command= fopen)
menu1.add_separator()

menu1.add_command(label="Quitter", command=quit)
menubar.add_cascade(label="Fichier", menu = menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Gomme", command = eraser)
menubar.add_cascade(label="Outil", menu = menu2)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Ligne")
menu3.add_command(label="carré")
menu3.add_command(label="rond")
menubar.add_cascade(label="Forme", menu = menu3)



canvas.config(menu=menubar)

cv = Canvas(canvas, width=640, height=480, bg='white')
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

canvas.mainloop()
