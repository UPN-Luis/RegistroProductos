from utils import (
    bienvenida,
    registrar_producto,
    calcular_total,
    mostrar_producto
)

# Mostrar bienvenida
bienvenida()

while True:

    # Registrar producto
    nombre, precio, cantidad = registrar_producto()

    # Validar datos
    if precio <= 0 or cantidad < 0:
        print("\nError: El precio debe ser mayor que cero y la cantidad no puede ser negativa.")
    else:
        total = calcular_total(precio, cantidad)
        mostrar_producto(nombre, precio, cantidad, total)

    opcion = input("\n¿Desea registrar otro producto? (S/N): ").upper()

    if opcion != "S":
        break

print("\nGracias por utilizar el sistema.")