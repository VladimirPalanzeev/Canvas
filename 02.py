from tkinter import *
from time import sleep

def pressSpace(event):
    global countAnimation
    countAnimation += 1

    # Не обрабатываем пробел
    cnv.unbind("<space>")

    if countAnimation < 20:
        cnv.move(evil, 1, 0)
        root.after(5, lambda e=event: pressSpace(e))
    else:
        countAnimation = 0
        # Вновь задаем реакцию на нажатие клавиши
        cnv.bind("<space>", pressSpace)


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

# Количество рекурсий
countAnimation = 0
root.mainloop()
