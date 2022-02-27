from tkinter import *

# Перемещение квадрата игрока
def move(veknor):
    pass

# Неумолимое движение вражеского круга
def evilMove():
    pass


# *****************************************************
# ************** ОСНОВНОЙ БЛОК ************************
# *****************************************************

root = Tk()
root.resizable(False, False)

WIDTH = 640
HEIGHT = 480

POS_X = root.winfo_screenwidth() // 2 -WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Создаём виджет
cnv = Canvas(root, width=WIDTH, height=HEIGHT)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

# Классически загружаем изображения
back = PhotoImage(file="imageForCanvas/background.png")
evilCircle = PhotoImage(file="imageForCanvas/circle.png")
playerSquare = PhotoImage(file="imageForCanvas/square.png")

# Устанавливаем "нижним слоем"  д
root.mainloop()