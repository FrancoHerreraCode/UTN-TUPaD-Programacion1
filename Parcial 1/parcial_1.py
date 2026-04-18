
ejecuccion = True
primera_pasada = True
herramientas = []
existencias = []
movimientos = []
menu_principal = [
    "Cargar una nueva herramienta",
    "Cargar movimiento de invetario",
    "Ver inventario completo",
    "Consulta invididual",
    "Reportes de productos sin stock",
    "Salir"
]

# BUCLE PRINCIPAL
while ejecuccion:
    if primera_pasada:
        # Carga inicial de herramientas como pide la consigna
        print("SISTEMA DE CONTROL DE INVENTARIO".center(120, "."))
        print("CARGA INICIAL DE STOCK")
        print("  Antes de comenzar con el sistema, deberá realizar una carga inicial del inventario de herramientas.")
        print("  Posteriormente podra cargar nuevas herramientas, o bien modificar el stock de aquellas cargas en este punto.")
        numero_inicial = input("\n> Indique la cantidad de herramientas a cargar (0 para omitir): ")

        while not(numero_inicial.isdigit()):
            print("\nERROR: El valor ingresado no es valido!")
            numero_inicial = input(" > Indique la cantidad de herramientas a cargar: ")
        print()
        numero_inicial = int(numero_inicial)

        for n in range(numero_inicial):
            nombre_herramienta = input(f">> Ahora ingrese el nombre de la herramienta N° {n+1} que desea cargar: ")
            while (nombre_herramienta.title() in herramientas) or (nombre_herramienta.isdigit()) or (nombre_herramienta == "") or (nombre_herramienta.isspace()):
                if nombre_herramienta.title() in herramientas:
                    print("ERROR! La herramienta ingresada ya se encuentra cargada!")
                elif nombre_herramienta.isdigit():
                    print("ERROR! Ingreso números. Debe ingresar el nombre de la herramienta")
                else:
                    print("ERROR! No puede ingresar espacios en blanco")
                print()
                nombre_herramienta = input(f">> Ingrese el nombre de la herramienta N° {n+1} que desea cargar: ")

            nombre_herramienta = nombre_herramienta.title()

            cantidad_herramienta = input(f">> Ahora ingrese la cantidad inicial de la herramienta {nombre_herramienta}: ")
            while not(cantidad_herramienta.isdigit()):
                print("ERROR: El valor ingresado no es valido!")
                cantidad_herramienta = input(f" > Indique la cantidad inicial de la herramienta {nombre_herramienta}: ")
            print()
            cantidad_herramienta = int(cantidad_herramienta)
            herramientas.append(nombre_herramienta)
            existencias.append(cantidad_herramienta)
            movimientos.append([cantidad_herramienta])

        primera_pasada = False
        input("La carga inicial ha finalizado con éxito! Presione una tecla para continuar...")
        print()
    
    # Se muestra el menu
    print("SITEMA DE INVENTARIO".center(120, "-"))
    print("Menu principal".center(120, "."))
    print("Opciones:")
    for i, p in enumerate(menu_principal):
        print(f" {i+1}) {p}.")
    
    opcion_elegida = input("\n>> Indique la copción elegida: ")

    while True:
        while not(opcion_elegida.isdigit()):
            print("ERROR: El valor ingresado no es valido!")
            opcion_elegida = input(">> Indique la copción elegida: ")
        
        if int(opcion_elegida) in range(1, len(menu_principal)+1):
            opcion_elegida = int(opcion_elegida)
            break
        else:
            opcion_elegida = " "

    # Estructura condicional principal
    if opcion_elegida == 1:
        print("Carga de una nueva herramienta".center(120, "."))
        nombre_herramienta = input(f">> Ahora ingrese el nombre de la herramienta que desea cargar: ")
        while (nombre_herramienta.title() in herramientas) or (nombre_herramienta.isdigit()) or (nombre_herramienta == "") or (nombre_herramienta.isspace()):
            if nombre_herramienta.title() in herramientas:
                print("ERROR! La herramienta ingresada ya se encuentra cargada!")
            elif nombre_herramienta.isdigit():
                print("ERROR! Ingreso números. Debe ingresar el nombre de la herramienta")
            else:
                print("ERROR! No puede ingresar espacios en blanco")
            print()
            nombre_herramienta = input(f">> Ingrese el nombre de la herramienta que desea cargar: ")

        nombre_herramienta = nombre_herramienta.title()
        
        cantidad_herramienta = input(f">> Ahora ingrese la cantidad inicial de la herramienta {nombre_herramienta}: ")
        while not(cantidad_herramienta.isdigit()):
            print("ERROR: El valor ingresado no es valido!")
            cantidad_herramienta = input(f" > Indique la cantidad inicial de la herramienta {nombre_herramienta}: ")
        print()
        cantidad_herramienta = int(cantidad_herramienta)
        herramientas.append(nombre_herramienta)
        existencias.append(cantidad_herramienta)
        movimientos.append([0, cantidad_herramienta])
        input(f"Se cargo {cantidad_herramienta} unidades de {nombre_herramienta} con éxito! \nPresione una tecla para continuar...")
        print()

    elif opcion_elegida == 2:
        print("Carga movimientos de inventario".center(120, "."))

        print("Movimientos de stock:")
        print(" 1) Venta (Salida de mercadería)")
        print(" 2) Compra (Ingreso de mercadería)")

        opcion_movstock = input("\n>> Opción elegida (1 o 2): ")
        while True:
            while not(opcion_movstock.isdigit()):
                print("ERROR: El valor ingresado no es valido!")
                opcion_movstock = input("\n>> Opción elegida (1 o 2): ")

            if int(opcion_movstock) in [1, 2]:
                opcion_movstock = int(opcion_movstock)
                break
            else:
                opcion_movstock = " "

        herramienta_buscada = input("\n> Ahora ingrese el nombre de la herramienta: ")
        salir = False
        while not(herramienta_buscada.title() in herramientas):
            print(f"ERROR: No se ha encontrado {herramienta_buscada} en el inventario")
            herramienta_buscada = input("> Ingrese el nombre de la herramienta (Salir para volver al menu): ")

            if herramienta_buscada.title() == "Salir":
                salir = True
                break
        if salir:
            continue
        herramienta_buscada = herramienta_buscada.title()
        indice_ext = herramientas.index(herramienta_buscada)

        print(f"Recordatorio: hay {existencias[indice_ext]} unidades de {herramienta_buscada}\n")

        if opcion_movstock == 1 and existencias[indice_ext] == 0:
            print(f"No hay stock disponible de {herramienta_buscada}!")
            input("Presione una tecla para continuar...")
            continue
        
        cantidad_herramienta_add = input(f">> Ingrese la cantidad de {herramienta_buscada}: ")
        while not(cantidad_herramienta_add.isdigit()):
            print("ERROR: El valor ingresado no es valido!")
            cantidad_herramienta_add = input(f" > Indique la cantidad de {herramienta_buscada}: ")
        cantidad_herramienta_add = int(cantidad_herramienta_add)

        if opcion_movstock == 1 and existencias[indice_ext] < cantidad_herramienta_add:
            print(f"Usted quiere resta {cantidad_herramienta_add} unidades de {herramienta_buscada}, pero solo hay {existencias[indice_ext]}!")
            print(f"Si continua con esta accion, se restan solo {existencias[indice_ext]} unidades a las existencias de {herramienta_buscada}")
            respuesta = input("¿Desea continuar con esta acción? (Si / No) : ")
            
            while not(respuesta.lower() in ["si", "no"]):
                print("ERROR: El valor ingresado no es valido!")
                respuesta = input("¿Desea continuar con esta acción? (Si / No) : ")
                
            if respuesta.lower() == "si":
                cantidad_herramienta_add = existencias[indice_ext]
            else:
                input("Modificación cancelada! Presione una tecla para volver al menu...")
                continue
        
        if opcion_movstock == 1:
            existencias[indice_ext] -= cantidad_herramienta_add
            movimientos[indice_ext].append(-1*cantidad_herramienta_add)
            print(f"Se han dismunido {cantidad_herramienta_add} unidades a {herramienta_buscada}. Su stock ahora es {existencias[indice_ext]}")
        else:
            existencias[indice_ext] += cantidad_herramienta_add
            movimientos[indice_ext].append(cantidad_herramienta_add)
            print(f"Se han agregado {cantidad_herramienta_add} unidades a {herramienta_buscada}. Su stock ahora es {existencias[indice_ext]}")
        input("Presione una tecla para continuar...")

    elif opcion_elegida == 3:
        print("Detalle del inventario actual".center(120, "."))
        aj = 20
        print("Nombre".center(aj, " ") , end= " ")
        print("Cantidad".center(aj, " "))
        print("-------------".center(aj, " ") , end= " ")
        print("-------------".center(aj, " "))
        for i, h in enumerate(herramientas):
            print(str(h).center(aj, " "), end= " ")
            print(str(existencias[i]).center(aj, " "))
        print()
        input("Presione una tecla para continuar...")

    elif opcion_elegida == 4:
        print("Consulta indivudla de stock".center(120, "."))
        aj = 20
        saldo = 0
        herramienta_buscada = input("> Ingrese el nombre de la herramienta: ")

        salir = False
        while not(herramienta_buscada.title() in herramientas):
            print(f"ERROR: No se ha encontrado {herramienta_buscada} en el inventario")
            herramienta_buscada = input("> Ingrese el nombre de la herramienta (Salir para volver al menu): ")
            if herramienta_buscada.title() == "Salir":
                salir = True
                break
        if salir:
            continue

        herramienta_buscada = herramienta_buscada.title()
        indice_ext = herramientas.index(herramienta_buscada)

        print("\nResultados de busqueda:")
        print(f"  Item: {herramienta_buscada}")
        print(f"  Unidades en stock: {existencias[indice_ext]}")
        print()

        print("\nDetalle de los movimientos:")

        print("Nombre".center(aj, " "), end= " ")
        print("Cantidad".center(aj, " "), end= " ")
        print("Saldo".center(aj, " "))
        print("-------------".center(aj, " ") , end= " ")
        print("-------------".center(aj, " ") , end= " ")
        print("-------------".center(aj, " "))
        for i, m in enumerate(movimientos[indice_ext]):
            saldo += m
            if i == 0:
                print("Stock inicial".center(aj, " "), end=" ")
                print(str(m).center(aj, " "), end=" ")
                print(str(saldo).center(aj, " "))
            elif m > 0:
                print("Compra".center(aj, " "), end=" ")
                print(str(m).center(aj, " "), end=" ")
                print(str(saldo).center(aj, " "))
            else:
                print("Venta".center(aj, " "), end=" ")
                print(str(m).center(aj, " "), end=" ")
                print(str(saldo).center(aj, " "))
        print()
        input("Presione una tecla para continuar...")


    elif opcion_elegida == 5:
        print("Detalle del herramientas SIN stock".center(120, "."))
        aj = 20
        print("Nombre".center(aj, " ") , end= " ")
        print("Cantidad".center(aj, " "))
        print("-------------".center(aj, " ") , end= " ")
        print("-------------".center(aj, " "))
        for i, h in enumerate(herramientas):
            if existencias[i] == 0:
                print(str(h).center(aj, " "), end= " ")
                print(str(existencias[i]).center(aj, " "))
        print()

    else:
        print("\nMuchas gracias por usar mi app!")
        input("Presione una tecla para continuar...")
        ejecuccion = False