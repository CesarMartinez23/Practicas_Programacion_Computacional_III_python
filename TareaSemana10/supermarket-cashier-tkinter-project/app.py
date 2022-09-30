# Importamos la libreria tkinter y sus utilidades necesarias.
import tkinter
from tkinter import messagebox
from tkinter import font

# * Main App Settings
app = tkinter.Tk()
# Centramos la ventana en la pantalla.
app.eval('tk::PlaceWindow . center')
# Configuramos el tamaño de la ventana.
app.geometry("375x450")
# Establecemos el titulo de la ventana.
app.title("Supermarket Chasier")
variableInt = tkinter.IntVar()
# Establecemos el fondo de la ventana.
app.configure(bg="#c5e2f6")

# * Labels Title App
# Establecemos el titulo de el label dentro de la ventana.
labelTile = tkinter.Label(app, text="Chasier Register",
                          font=60, pady=20, bg="#c5e2f6")
labelTile.pack()

# * Labels
# Crear un label para la cantidad del producto.
labelQuantity = tkinter.Label(app, text="Quantity", font=25, bg="#80aaff")
# Crear un label para el precio del producto.
labelPrice = tkinter.Label(app, text="Price", font=25, bg="#80aaff")

# * Entry
# Crear un entry para la cantidad del producto.
entryQuantityProduct = tkinter.Entry(app, font=25, bg="#ffffb3")
# Crear un entry para el precio del producto.
entryPriceProduct = tkinter.Entry(app, font=25, bg="#ffffb3")

# * Functions
# Creamos una funcion para calcular el descuento, mediante la cual recibimos la opcion de pago seleccionda por el usuario y asi mismo el total de la compra del producto, para posteriomente validad y aplicar descuento si este lo requiere.
def discount(optionSelected, total):
    if optionSelected == 1:
        totalBuy = total - (total * 0.20)
        message = f"Su total es: $ {total} y se le aplicara un descuento de $ {total - totalBuy} , su total a pagar es de $ {totalBuy}"
    elif optionSelected == 2:
        totalBuy = total
        message = f"No aplica descuento. Su total a pagar es de $ {total}"
    else:
        message = "Seleccione una opción de pago."
    return message

# Creamos una funcion para obtener los datos del producto y procesarlos para calcular el total de la compra.
def getProduct():
    try:
        price = float(entryPriceProduct.get())
        quantity = int(entryQuantityProduct.get())
        total = float(price * quantity)
        messagebox.showinfo(
            title="Total", message=f"{discount(variableInt.get(), total)}")
    except:
        if entryPriceProduct.get() == "":
            messagebox.showerror(
                title="Error", message="Ingrese los datos del producto.")
        else:
            messagebox.showwarning(
                title="Error", message="Por favor ingrese solo datos numericos.")


# * Radio Buttons Options
# Creamos un radio button para la opcion de pago con tarjeta.
payWithCards = tkinter.Radiobutton(
    app, text="Pay with Credit/Debit Card", value=1, variable=variableInt, font=25, bg="#b3ccff")

# Creamos un radio button para la opcion de pago en efectivo.
payWithCahs = tkinter.Radiobutton(
    app, text="Pay with Cash", value=2, variable=variableInt, font=25, bg="#b3ccff")

# * Buttons
# Creamos un boton para calcular el total de la compra o proceder a pagar.
buttonPay = tkinter.Button(app, text="Pay", width=10,
                           height=2, command=getProduct, font=30, bg="yellow", fg="black")

# * Positioning
# Posicionamos los labels.
labelQuantity.pack(pady=3)
# Posicionamos los entry.
entryQuantityProduct.pack(pady=10)

# Posicionamos los labels.
labelPrice.pack(pady=3)
# Posicionamos los entry.
entryPriceProduct.pack(pady=10)

# Posicionamos los radio buttons.
payWithCards.pack(pady=5)
payWithCahs.pack(pady=5)

# Posicionamos el boton.
buttonPay.pack(pady=10)

# * Main Loop
app.mainloop()
