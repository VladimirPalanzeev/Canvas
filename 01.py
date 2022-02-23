from tkinter import *

root = Tk()
root["bg"] = "#000000"
root.geometry("480x360")

# Создаём виджет Canvas
cnv = Canvas(root, width=240, height=180, bg="#AAAAAA")
# Убираем рамку
cnv.config(highlightthickness=0)

# Устанавливаем в область окна
cnv.place(x=50, y=50)

root.mainloop()
