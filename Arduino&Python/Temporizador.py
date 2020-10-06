# Cantero Cardenas Jose Rafael
# Miercoles  de Septiembre del 2020
# Disenio de Interfaces: Temporizador de Tiro

import tkinter
import pyfirmata
from time import sleep
from tkinter import *

# Serial
'''port = 'com5'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:3:p')'''

# Window Buttons
top = tkinter.Tk()
top.title("Botones Inicio/Fin")

# Window Timer
top1 = tkinter.Tk()
top1.geometry("750x700")
top1.title("Temporizador")
label1 = Label(top1, text="", font=("Helvetica", 500), fg="blue", bg="white")
label1.grid(row=1, column=1)


# Function Timer
def countdown():
    t = 24
    startButton.config(state=tkinter.DISABLED)
    if t > 0:
        label1.config(text=t)
        t = t-1
        label1.after(1000, countdown)
    elif t == 0:
        label1.config(text="alarma")
        # ledPin.write(1)
        sleep(2)
        # ledPin.write(0)
        startButton.config(state=tkinter.ACTIVE)


# Function End Button
def offButtonPress():
    startButton.config(state=tkinter.ACTIVE)
    offButton.config(state=tkinter.DISABLED)
    sleep(1)
    offButton.config(state=tkinter.ACTIVE)


# Function Exit Button
def exitButtonPress():
    top.quit()
    top1.quit()


# Button start
startButton = tkinter.Button(
    top, text="Start", width=15, height=10, bg="green", command=countdown)
startButton.grid(column=1, row=1, padx=5)

# Button end
offButton = tkinter.Button(top, text="END", width=15,
                           height=10, bg="red", command=offButtonPress)
offButton.grid(column=2, row=1, padx=5)

# Button exit
exitButton = tkinter.Button(
    top, text="Salir", width=15, bg="gray", command=exitButtonPress)
exitButton.grid(column=1, row=2)

# Start the program
top.resizable(0, 0)
top.mainloop()
top1.mainloop()
