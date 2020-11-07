import tkinter
from tkinter import *
from tkinter import messagebox

# Ventana principal
top = tkinter.Tk()
top.title("Ventana principal")
top.geometry("500x500")
top.resizable(0, 0)
top.config(bg="DodgerBlue4")
label0 = Label(top, text="Registrate o Inicia sesion", font=(
    "Helvetica"), bg="Orange", fg="White", width="500", height="2")
imagen1 = PhotoImage(file="C:\Imagenes_gif\Escudo_UdeG.gif")
label = Label(top, image=imagen1)
label.place(x=150, y=90)
label0.pack()


# Funcion para la ventana de registro
def win_registro():
    top.withdraw()  # Desaparecer ventana sin destruir
    top1 = tkinter.Toplevel()   # Abrir ventana nueva
    top1.title("Registro de Usuario")
    top1.geometry("500x500")
    top1.resizable(0, 0)
    top1.config(bg="blue violet")
    label1 = Label(top1, text="Registrate como Administrador o Usuario", font=(
        "Helvetica"), bg="Orange", fg="White", width="500", height="2")
    label1.pack()

    # Boton para registrar como administrador
    registro2 = tkinter.Button(top1, text="Administrador",
                               bg="white smoke", width="20", height="2", bd="10", command=win_administrador)
    registro2.place(x=175, y=200)

    # Boton para registrar como usuario
    adm0 = tkinter.Button(top1, text="Usuario",
                          bg="white smoke", width="20", height="2", bd="10", command=win_usuario)
    adm0.place(x=175, y=300)

    top1.mainloop()


# Funcion para la ventana de ingreso
def win_ingreso():
    top.withdraw()
    top2 = tkinter.Toplevel()
    top2.title("Inicio de sesion")
    top2.geometry("500x500")
    top2.resizable(0, 0)
    top2.config(bg="blue violet")
    label2 = Label(top2, text="Ingresa tu nombre de usuario", font=(
        "Helvetica"), bg="Orange", fg="White", width="500", height="2")
    label2.pack()

    username_label = Label(top2, text="Nombre de usuario : ", bg="white smoke")
    username_label.place(x=22, y=150)
    password_label = Label(top2, text="Contrasenia : ", bg="white smoke")
    password_label.place(x=22, y=220)

    username_in = Entry(top2, textvariable=username, width="20")
    username_in.place(x=22, y=180)
    password_in = Entry(top2, textvariable=password, width="20", show="*")
    password_in.place(x=22, y=250)

    # Boton para ingresar a un usuario
    ingreso = tkinter.Button(top2, text="Ingresar",
                             bg="white smoke", width="20", height="2", bd="10")
    ingreso.place(x=175, y=350)

    top2.mainloop()


# Ventana para registrar como administrador
def win_administrador():
    # top1.withdraw()
    top3 = tkinter.Toplevel()
    top3.title("Administrador")
    top3.geometry("500x500")
    top3.resizable(0, 0)
    top3.config(bg="blue violet")
    label3 = Label(top3, text="Registrarte como administrador", font=(
        "Helvetica"), bg="Orange", fg="White", width="500", height="2")
    label3.pack()

    username_label = Label(top3, text="Nombre de usuario : ", bg="white smoke")
    username_label.place(x=22, y=150)
    password_label = Label(top3, text="Contrasenia : ", bg="white smoke")
    password_label.place(x=22, y=220)

    username_in = Entry(top3, textvariable=username, width="20")
    username_in.place(x=22, y=180)
    password_in = Entry(top3, textvariable=password, width="20", show="*")
    password_in.place(x=22, y=250)

    # Boton para registrar como administrador
    reg_adm = tkinter.Button(top3, text="Registrar",
                             bg="white smoke", width="20", height="2", bd="10", command=registrar)
    reg_adm.place(x=175, y=350)

    top3.mainloop()


# Ventana para registrar como usuario
def win_usuario():
    # top1.withdraw()
    top4 = tkinter.Toplevel()
    top4.title("Usuario")
    top4.geometry("500x500")
    top4.resizable(0, 0)
    top4.config(bg="blue violet")
    label4 = Label(top4, text="Registrarte como Usuario", font=(
        "Helvetica"), bg="Orange", fg="White", width="500", height="2")
    label4.pack()

    username_label = Label(top4, text="Nombre de usuario : ", bg="white smoke")
    username_label.place(x=22, y=150)
    password_label = Label(top4, text="Contrasenia : ", bg="white smoke")
    password_label.place(x=22, y=220)

    username_in = Entry(top4, textvariable=username, width="20")
    username_in.place(x=22, y=180)
    password_in = Entry(top4, textvariable=password, width="20", show="*")
    password_in.place(x=22, y=250)

    # Boton para registrar como usuarior
    reg_us = tkinter.Button(top4, text="Registrar",
                            bg="white smoke", width="20", height="2", bd="10", command=registrar)
    reg_us.place(x=175, y=350)

    top4.mainloop()


def registrar():

    space = False
    digit = False

    lista = {}

    username_data = username.get()
    password_data = str(password.get())

    l = len(password_data)
    t = password_data.isalnum()

    if t == False:
        messagebox.showwarning("Aviso", "Solo se aceptan letras y numeros")
        #password_in.delete(0, END)
    if l < 6:
        messagebox.showwarning(
            "Aviso", "La contraseña debe tener minimo 6 letras")
        #password_in.delete(0, END)
    for ver in password_data:
        if ver.isspace() == True:
            space = True
        if ver.isdigit() == True:
            digit = True
    if digit == False:
        messagebox.showwarning(
            "Aviso", "La contrasenia debe tener al menos un numero o una letra")
    if space == False and digit == True and t == True:
        lista[username_data] = password_data
        messagebox.showinfo(
            "Bien", "Usuario aceptado\n" "Bienvenido " + username_data)
        print(lista)

    #username_in.delete(0, END)
    #password_in.delete(0, END)


# Entradas
username = StringVar()
password = StringVar()

# Boton entrada a registro
registro0 = tkinter.Button(top, text="Registrar",
                           bg="DeepSkyBlue1", width="20", height="2", bd="10", command=win_registro)
registro0.place(x=50, y=400)

# Boton entrada a ingreso
ingresar = tkinter.Button(top, text="Ingresar",
                          bg="DeepSkyBlue1", width="20", height="2", bd="10", command=win_ingreso)
ingresar.place(x=300, y=400)

top.mainloop()
