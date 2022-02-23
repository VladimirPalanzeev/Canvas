from tkinter import *

def plusSecond():
    global second, timerLink
    second += 1
    label["text"] = f"Прошло секунд: {second}"

    # Вызываем через 1 секунду
    timerLink = root.after(1000, plusSecond)


def startTimer():
    global timerLink
    timerLink = root.after(1000, plusSecond)


def stopTimer():
    global timerLink
    if timerLink != None:
        # .after_cancel прекращает вызов
        root.after_cancel(timerLink)
        timerLink = None

root = Tk()
root.geometry(f"{320}x{240}")
root.title("Таймер")

label = Label(root)
label.place(x=10, y=10)

startBtn = Button(root, text="СТАРТ")
startBtn.place(x=10, y=50)
startBtn["command"] = startTimer

stopBtn = Button(root, text="СТОП ")
stopBtn.place(x=70, y=50)
stopBtn["command"] = stopTimer

# Секунды
second = 0

timerLink = None

root.mainloop()
