import tkinter
import time



ventana = tkinter.Tk()
ventana.title("Python Tkinter: Calculadora")

ancho_ventana = 500
alto_ventana = 300

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

X = int(ancho_pantalla / 2 - ancho_ventana / 2)
Y = int(alto_pantalla / 2 - alto_ventana / 2)


ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{X}+{Y}")

#FUNCIONES

def BorrarNumero():
    global Etiqueta_operaciones
    Etiqueta_operaciones.config(text= "")

Secuencia_operacion = 1
valor = 0

def ImprimirNumero(numero):
    global Etiqueta_operaciones
    global Secuencia_operacion
    
    valor= Etiqueta_operaciones.cget("text")
    Etiqueta_operaciones.config(text= str(valor) + str(numero))



primer_numero = ""
operacion = ""
def Suma():
    global primer_numero
    global operacion
    global Etiqueta_operaciones

    primer_numero = Etiqueta_operaciones.cget("text")
    operacion = "+"

    BorrarNumero()

def Resta():
    global primer_numero
    global operacion
    global Etiqueta_operaciones

    primer_numero = Etiqueta_operaciones.cget("text")
    operacion = "-"

    BorrarNumero()

def Multiplicacion():
    global primer_numero
    global operacion
    global Etiqueta_operaciones

    primer_numero = Etiqueta_operaciones.cget("text")
    operacion = "x"

    BorrarNumero()

def Division():
    global primer_numero
    global operacion
    global Etiqueta_operaciones

    primer_numero = Etiqueta_operaciones.cget("text")
    operacion = "/"

    BorrarNumero()


def Calculo():
    global primer_numero
    global operacion

    segundo_numero = Etiqueta_operaciones.cget("text")

    if operacion == "+":
        resultado = int(primer_numero) + int(segundo_numero)
    elif operacion == "-":
        resultado = int(primer_numero) - int(segundo_numero)
    elif operacion == "x":
        resultado = int(primer_numero) * int(segundo_numero)
    elif operacion == "/":
        resultado = int(primer_numero) / int(segundo_numero)
    else: 
        Etiqueta_operaciones.config(text="Error, pulse [Borrar]")

    Etiqueta_operaciones.config(text= str(resultado))
    primer_numero = ""
    operacion = ""








#BOTONES Y ETIQUETAS


Boton_1 = tkinter.Button(text= "1", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(1))
Boton_2 = tkinter.Button(text= "2", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(2))
Boton_3 = tkinter.Button(text= "3", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(3))
Boton_4 = tkinter.Button(text= "4", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(4))
Boton_5 = tkinter.Button(text= "5", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(5))
Boton_6 = tkinter.Button(text= "6", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(6))
Boton_7 = tkinter.Button(text= "7", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(7))
Boton_8 = tkinter.Button(text= "8", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(8))
Boton_9 = tkinter.Button(text= "9", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(9))
Boton_0 = tkinter.Button(text= "0", bg= "pale green", border=5, relief= "flat", command=lambda: ImprimirNumero(0))

Boton_Borrar = tkinter.Button(text= "Borrar", bg= "forest green", command= BorrarNumero)

Etiqueta_operaciones = tkinter.Label(text="", bg="lightgray", relief="sunken", width=20)

Boton_suma = tkinter.Button(text= "+", bg="lime", relief= "flat", command= Suma)
Boton_resta = tkinter.Button(text= "-", bg="lime", relief= "flat", command= Resta)
Boton_multiplicacion = tkinter.Button(text= "x", bg="lime", relief= "flat", command= Multiplicacion)
Boton_division = tkinter.Button(text= "/", bg="lime", relief= "flat", command= Division)
Boton_Calculo = tkinter.Button(text= "=", bg= "lime", relief= "ridge", command= Calculo)


etiqueta = tkinter.Label(text= " ").grid(row=0, column=0)
etiqueta = tkinter.Label(text= " ").grid(row=8, column=8)
etiqueta = tkinter.Label(text= " ").grid(row=7, column=7)
etiqueta = tkinter.Label(text= " ").grid(row=6, column=6)
etiqueta = tkinter.Label(text= " ").grid(row=5, column=5)
etiqueta = tkinter.Label(text= " ").grid(row=4, column=4)
etiqueta = tkinter.Label(text= " ").grid(row=3, column=3)
etiqueta = tkinter.Label(text= " ").grid(row=2, column=2)
etiqueta = tkinter.Label(text= " ").grid(row=1, column=1)


Boton_1.grid(row=6, column=9, padx=2, pady= 2)
Boton_2.grid(row=6, column=10, padx=2, pady= 2)
Boton_3.grid(row=6, column=11, padx=2, pady= 2)
Boton_4.grid(row=7, column=9, pady= 2, padx=2 )
Boton_5.grid(row=7, column=10, pady= 2, padx=2 )
Boton_6.grid(row=7, column=11, pady= 2, padx=2 )
Boton_7.grid(row=8, column=9, pady= 2, padx=2 )
Boton_8.grid(row=8, column=10, pady= 2, padx=2 )
Boton_9.grid(row=8, column=11, pady= 2, padx=2 )
Boton_0.grid(row=9, column=10, pady= 2, padx=2 )

Boton_Borrar.grid(row=6, column=12, padx=2, pady=2)

Etiqueta_operaciones.grid(row=4, column=9, columnspan=4, padx=2, pady=5, sticky="ew")

Boton_suma.grid(row=7, column=12, padx=2, pady=2)
Boton_resta.grid(row=8, column=12, padx=2, pady=2)
Boton_multiplicacion.grid(row=9, column=12, padx=2, pady=2)
Boton_division.grid(row=9, column=11, padx=2, pady=2)
Boton_Calculo.grid(row=9, column=9, padx=2, pady=2)


    













# Bucle pricipal de la ventana
ventana.mainloop()
