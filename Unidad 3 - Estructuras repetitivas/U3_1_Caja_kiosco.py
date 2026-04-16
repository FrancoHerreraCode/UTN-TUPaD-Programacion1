
# INTRODUCCIÓN
print("\n")
print(" LISTA DE COMPRAS ".center(50,"-"))

# ALGUNAS VARIABLES
precio_producto = ""
descuento = "n"
total_sin_desc = 0
total_con_desc = 0
lista_producto = []


# NOMBRE DEL CLIENTE
nombre_cliente = input("Ingrese el nombre del cliente: ")

while not(nombre_cliente.isalpha()):
    nombre_cliente = input("El valor ingresado no es valido.\nIngrese el nombre del cliente: ")

nombre_cliente = nombre_cliente.title()
cantidad_producto = input("Ingrese la cantidad de productos a comprar: ")


# CANTIDAD DE PRODUCTOS
while not(cantidad_producto.isdigit() and cantidad_producto[0] != "0"):
    cantidad_producto = input("El valor ingresado no es valido.\nIngrese la cantidad de productos a comprar: ")

cantidad_producto = int(cantidad_producto)
print("")


#BUCLE PRINCIPAL - SOLICITA LOS DATOS DE LOS PRODUCTOS
for p in range(cantidad_producto):
    precio_producto = input(f"Ingrese el precio del producto N° {p+1} (Numero entero): ")

    while not(precio_producto.isdigit() and precio_producto[0] != "0"):
        precio_producto = input(f"El valor ingresado no es valido.\nIngrese el precio del producto N° {p+1} (Numero entero): ")

    precio_producto = int(precio_producto)

    descuento = input("Si el producto tiene descuento, presione 's'. De lo contrario presione 'n': ").upper()
    valores_validos = ["S", "N"]
    while not(descuento in valores_validos):
        descuento = input("El valor ingresado no es valido.\nSi el producto tiene descuento, presione 's'. De lo contrario presione 'n':").upper()

    print("")
    if descuento == "S":
        precio_producto_desc = 0.9*precio_producto
    else:
        precio_producto_desc = precio_producto

    datos = (p+1, precio_producto, descuento, precio_producto_desc)
    lista_producto.append(datos)


#IMPRIME EN PANTALLA LA INFO
print("\n")
print("-".center(50,"-"))
print(" RESUMEN DE LA COMPRA ".center(50,"-"))
print("-".center(50,"-"))
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_producto}")

for h, i, j, k in lista_producto:
    print(f"Producto {h} - Precio: {i} - Descuento: (S/N) {j}")

    total_sin_desc += i
    total_con_desc += k

print(f"\nTotal sin descuento: ${total_sin_desc:.2f}")
print(f"Total con descuento: ${total_con_desc:.2f}")
print(f"Ahorro: ${(total_sin_desc - total_con_desc):.2f}")
print(f"Promedio por producto: ${total_con_desc/cantidad_producto:.2f}")