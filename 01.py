from tkinter import *

def go(vector):
    if vector == UPKEY:
        cnv.move(player, 0, -2)
        cnv.move(evil, 0, 2)
    elif vector == DOWNKEY:
        cnv.move(player, 0, 2)
        cnv.move(evil, 0, -2)
    elif vector == LEFTKEY:
        cnv.move(player, -2, 0)
        cnv.move(evil, 2, 0)
    elif vector == RIGHTKEY:
        cnv.move(player, 2, 0)
        cnv.move(evil, -2, 0)


# Размеры окна
WIDTH = 640
HEIGHT = 480

root = Tk()
# root["bg"] = "#000000"

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
cnv.bind("<Up>", lambda e, x=UPKEY: go(x))
cnv.bind("<Down>", lambda e, x=DOWNKEY: go(x))
cnv.bind("<Left>", lambda e, x=LEFTKEY: go(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: go(x))


root.mainloop()
