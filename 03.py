from tkinter import *

def move(vector):
    # vector - направление движения игрока
    if vector == UPKEY:
        cnv.move(player, 0, -2)
    elif vector == DOWNKEY:
        cnv.move(player, 0, 2)
    elif vector == LEFTKEY:
        cnv.move(player, -2, 0)
    elif vector == RIGHTKEY:
        cnv.move(player, 2, 0)

def evilMove():
    pass

# Размеры окна
WIDTH = 640
HEIGHT = 480

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")

# Создаём виджет Canvas
cnv = Canvas(root, width=WIDTH, height=HEIGHT)
# Убираем рамку
cnv.config(highlightthickness=0)
# Устанавливаем в область окна
cnv.place(x=0, y=0)
# Устанавливаем фокус внимания
cnv.focus_set()

# Загружаем фоновую картинку
back = PhotoImage(file="imageForCanvas/background.png")
# И устанавливаем её на Canvas
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Изображение красного круга
evilCircle = PhotoImage(file="imageForCanvas/circle.png")
evil = cnv.create_image(32, 32, image=evilCircle)

# Изображение зеленого квадрата
playerSquare = PhotoImage(file="imageForCanvas/square.png")
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

# Закодируем кнопки константами для повышения читаемости кода
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Назначим клавиши управления курсором
cnv.bind("<Up>", lambda e, x=UPKEY: move(x))
cnv.bind("<Down>", lambda e, x=DOWNKEY: move(x))
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))

#

root.mainloop()
