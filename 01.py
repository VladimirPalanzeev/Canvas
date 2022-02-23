from tkinter import *

# Размеры окна
WIDTH = 640
HEIGHT = 480

root = Tk()
# root["bg"] = "#000000"

root.geometry(f"{WIDTH}x{HEIGHT}")

# Создаём виджет Canvas
cnv = Canvas(root, width=WIDTH, height=HEIGHT)
# Убираем рамку
cnv.config(highlightthickness=1)
# Устанавливаем в область окна
cnv.place(x=0, y=0)
# Устанавливаем фокус внимания
cnv.focus_set()

# Загружаем фоновую картинку
back = PhotoImage(file="imageForCanvas/background.png")
# И устанавливаем её на Canvas
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

root.mainloop()
