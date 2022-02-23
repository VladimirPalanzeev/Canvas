from tkinter import *
from time import sleep

def pressSpace(event):
    for i in range(200):
        # sleep(1)
        cnv.move(evil, 2, 0)


root = Tk()

WIDTH = 640
HEIGHT = 480

root.geometry(f"{WIDTH}x{HEIGHT}")

cnv = Canvas(root, width=WIDTH, height=HEIGHT)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

evilCircle = PhotoImage(file="imageForCanvas/circle.png")
evil = cnv.create_image(120, 240, image=evilCircle)

# Назначаем на пробел метод pressSpace
cnv.bind("<space>", pressSpace)

root.mainloop()
