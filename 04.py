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

# Устанавливаем "нижним слоем" фоновое изображение
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Смещение вражеского круга
vectorX = 5
vectorY = 5

# Скорость движения квадрата
playerSpeed = 3

# Создаём и получаем ссылки на объекты
evil = cnv.create_image(32, 32, image=evilCircle)
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

# Зададим коды кнопок в константах для повышения читаемости кода
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Назначаем клавиши управления курсором

cnv.bind("<Up>", lambda e, x=UPKEY: move(x))
cnv.bind("<Down>", lambda e, x=DOWNKEY: move(x))
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))

# Запускаем движение вражеского круга
evilAfter = root.after(30, evilMove())

root.mainloop()