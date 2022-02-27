from tkinter import *

# Перемещение квадрата игрока
def move(vector):
    # vector - направление движения
    if vector == UPKEY:
        cnv.move(player, 0, -playerSpeed)
    elif vector == DOWNKEY:
        cnv.move(player, 0, playerSpeed)
    elif vector == LEFTKEY:
        cnv.move(player, -playerSpeed, 0)
    elif vector == RIGHTKEY:
        cnv.move(player, playerSpeed, 0)


# Неумолимое движение вражеского круга
def evilMove():
    global evilAfter, vectorX, vectorY

    # Передвигаем вражеский круг
    cnv.move(evil, vectorX, vectorY)

    # Получаем координаты в отдельные переменные так легче читать и считать код
    # cnv.coords возвращает список, в котором на нулевой позиции стоит координата x,
    # на первой - координата y
    x = cnv.coords(evil)[0]
    y = cnv.coords(evil)[1]

    # Проверяем: ударился ли красный круг щ границы окна
    if x > WIDTH - 32 or x < 32:
        vectorX = -vectorX
    if y > HEIGHT - 32 or y < 32:
        vectorY = -vectorY

    # Получаем координаты игрока
    xP = cnv.coords(player)[0]
    yP = cnv.coords(player)[1]

    # Считаем по теореме Пифагора. Если расстояние между координатами меньше диаметра круга,
    # то засчитываем соприкосновение и останавливаем перемещение вражеского круга

    distance = (abs(x - xP) ** 2 + abs(y - yP) ** 2) ** 0.5
    if distance < 64:
        # Если соприкосновение, то останавливаем evilAfter
        root.after_cancel(evilAfter)
    else:
        # Если соприкосновения нет, то перемещаем вражеский круг дальше
        evilAfter = root.after(30, evilMove)



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