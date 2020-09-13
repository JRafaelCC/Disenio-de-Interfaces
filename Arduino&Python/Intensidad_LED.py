# Cantero Cardenas Jose Rafael.
# Sabado 12 de Septiembre del 2020.
# Practica 1, disenio de interfaces: Intensidad de LED

# librerias
import tkinter
import pyfirmata
from time import sleep
from tkinter import *

# Configuración de Comunicacion Serial
port = 'com5'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:3:p')
top = tkinter.Tk()
top.title("Practica 1")

# Imagen Foco Encendido
imagen1 = PhotoImage(file="C:\Imagenes_gif\Foco_encendido.gif")
label1 = Label(top, image=imagen1)
label1.grid(row=1, column=1)

# Imagen Foco apagado
imagen2 = PhotoImage(file="C:\Imagenes_gif\Foco_apagado.gif")
label1 = Label(top, image=imagen2)
label1.grid(row=1, column=2)

# Color de Fondo
top.config(bg="white")

# Funcion Boton de Iniciar


def onButtonPress():
    startButton.config(state=tkinter.DISABLED)
    ledPin.write(1)


# Funcion Boton de Intensidad
def changeButtonPress():
    startButton.config(state=tkinter.ACTIVE)
    ledBrightnees = brightnessScale.get()
    ledBrightnees = float(ledBrightnees)
    ledPin.write(ledBrightnees/100.0)


# Funcion Boton de Apagar
def offButtonPress():
    startButton.config(state=tkinter.ACTIVE)
    offButton.config(state=tkinter.DISABLED)
    ledPin.write(0)
    offButton.config(state=tkinter.ACTIVE)


# Slide y Boton de Intensidad
changeButton = tkinter.Button(
    top, text="Intensidad", width=15, bg="yellow", command=changeButtonPress)
brightnessScale = tkinter.Scale(top, length=200, sliderlength=10, width=15,
                                bg="yellow", troughcolor="gray", from_=1, to=100, orient=tkinter.HORIZONTAL)
brightnessScale.grid(column=1, row=5)
changeButton.grid(column=1, row=4)

# Boton Iniciar
startButton = tkinter.Button(
    top, text="Iniciar", width=15, bg="green", command=onButtonPress)
startButton.grid(column=1, row=3)

# Boton Apagado
offButton = tkinter.Button(
    top, text="Apagar", width=15, bg="red", command=offButtonPress)
offButton.grid(column=2, row=3)

# Boton Salida
exitButton = tkinter.Button(
    top, text="Salir", width=15, bg="white", command=top.quit)
exitButton.grid(column=2, row=5)

brightnessScale.grid()
startButton.grid()
offButton.grid()
changeButton.grid()
top.mainloop()
