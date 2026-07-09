def bienvenida():
    """
    Muestra un mensaje de bienvenida al usuario.
    """
    print("=" * 40)
    print(" SISTEMA DE REGISTRO ABARROTES DON ANTONIO")
    print("=" * 40)


def registrar_producto():
    """
    Solicita los datos del producto y los devuelve.
    """
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: S/ "))
    cantidad = int(input("Ingrese la cantidad: "))

    return nombre, precio, cantidad


def calcular_total(precio, cantidad):
    """
    Calcula el valor total del inventario.
    """
    return precio * cantidad


def mostrar_producto(nombre, precio, cantidad, total):
    """
    Muestra la informacion del producto registrado.
    """
    print("\n===== PRODUCTO REGISTRADO =====")
    print(f"Nombre   : {nombre}")
    print(f"Precio   : S/ {precio:.2f}")
    print(f"Cantidad : {cantidad}")
    print(f"Total    : S/ {total:.2f}")