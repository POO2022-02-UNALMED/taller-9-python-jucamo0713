from tkinter import Tk, Button, Entry, StringVar

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                              cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                        cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)


class admin:
    number1 = ""
    number2 = ""
    operator = None
    text = StringVar()

    @classmethod
    def resolveOperator(cls, operator):
        if operator == "+":
            return str(float(cls.number1) + float(cls.number2))
        elif operator == "-":
            return str(float(cls.number1) - float(cls.number2))
        elif operator == "*":
            return str(float(cls.number1) * float(cls.number2))
        elif operator == "/":
            return str(float(cls.number1) / float(cls.number2))

    @classmethod
    def igual(cls):
        if cls.number1 != "" and cls.number2 != "":
            cls.number1 = cls.resolveOperator(cls.operator)
            cls.text.set(str(cls.number1))
            cls.operator = "="
            cls.number2 = ""

    @classmethod
    def operador(cls, operador):
        if cls.number1 != "" and cls.number2 != "":
            cls.operator = operador
            cls.number1 = cls.resolveOperator(cls.operator)
            cls.text.set(str(cls.number1))
            cls.number2 = ""
        elif operador == "-" and (
                (cls.operator is None and cls.number1 == "") or (cls.operator is not None and cls.number2 == "")):
            cls.numero("-")
        elif cls.number1 != "":
            cls.operator = operador
            cls.text.set("")

    @classmethod
    def numero(cls, numero):
        if cls.operator == "=":
            cls.number1 = str(numero)
            cls.operator = None
            cls.text.set(str(cls.number1))
        elif cls.operator is not None:
            cls.number2 += str(numero)
            cls.text.set(str(cls.number2))
        else:
            cls.number1 += str(numero)
            cls.text.set(str(cls.number1))


boton_1.bind("<Button-1>", lambda x: admin.numero(1))
boton_2.bind("<Button-1>", lambda x: admin.numero(2))
boton_3.bind("<Button-1>", lambda x: admin.numero(3))
boton_4.bind("<Button-1>", lambda x: admin.numero(4))
boton_5.bind("<Button-1>", lambda x: admin.numero(5))
boton_6.bind("<Button-1>", lambda x: admin.numero(6))
boton_7.bind("<Button-1>", lambda x: admin.numero(7))
boton_8.bind("<Button-1>", lambda x: admin.numero(8))
boton_9.bind("<Button-1>", lambda x: admin.numero(9))
boton_punto.bind("<Button-1>", lambda x: admin.numero("."))
boton_igual.bind("<Button-1>", lambda x: admin.igual())
boton_mas.bind("<Button-1>", lambda x: admin.operador("+"))
boton_menos.bind("<Button-1>", lambda x: admin.operador("-"))
boton_multiplicacion.bind("<Button-1>", lambda x: admin.operador("*"))
boton_division.bind("<Button-1>", lambda x: admin.operador("/"))
pantalla.config(textvariable=admin.text)
root.mainloop()
