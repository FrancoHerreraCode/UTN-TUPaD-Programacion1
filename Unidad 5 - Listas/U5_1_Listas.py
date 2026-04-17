from random import randint

# FUNCIONES UTILIZADAS
def intro_ejercicio(i):
    print(f"Ejercicio {i}".center(100,"."))

def lista_valores_aleatorios(inicio, fin, n):
    lista_base = []
    for i in range(n):
        lista_base.append(randint(inicio, fin))

    return lista_base

def mostrar_lista_horizontal(lista_mostrar:list, intro:str):
    # DESCRICPION DE LA FUNCIÓN
    # Permite mostrar una lista de manera horizontal
    # Los valores se separaon con una coma y una "y" final
    print(intro, end=" ")
    for i, n in enumerate(lista_mostrar):
        if i == len(lista_mostrar)-1:
            print("y", n)
        else:
            print(n, end=", ")

def mostrar_lista_vertical(lista_mostrar:list, intro:str, con_sp:bool, sp:str):
    # DESCRICPION DE LA FUNCIÓN
    # Permite mostrar una lista de manera vertical, un item en cada linea.
    # sp significa "separador". Por ejemplo: ") " de forma que quedaria "1) "
    print(intro)
    if con_sp:
        for i, n in enumerate(lista_mostrar):
            print(str(i+1) + sp + str(n))
    else:
        for n in lista_mostrar:
            print(n)

def solicitar_numero(min:int, max:int, mensaje:str):
    while True:
        try:
            respuesta = int(input(mensaje))
        except ValueError:
            print(f"ERROR: ¡El valor ingresado no es un número!")
        else:
            if respuesta < min or respuesta > max:
                print("ERROR: ¡Usted ha ingresado un número fuera del rango permitido!")
                print(f"Debe ingresar un valor entre {min} y {max}")
            else:
                break
    return respuesta


def menu_principal():
    print()
    print("MENÚ PRINCIPAL".center(100, "_"))
    introduccion = "Ejercicios: "
    lista_opciones = [
        "Notas de alumnos",
        "Lista de 5 productos",
        "Pares e impares",
        "Valores repetidos",
        "Nombre de alumnos",
        "Uno a la derecha",
        "Temperaturas de la semana",
        "Tabla de notas y promedios",
        "Ta Te Ti",
        "Registro de ventas semanales",
        "Buscador de nombres",
        "Lista de números",
        "Puntajes de juego",
        "Salir"
    ]

    mostrar_lista_vertical(lista_opciones, introduccion, True, ") ")
    opcion = solicitar_numero(1, len(lista_opciones), "\nOpcion elegida: ")
    return opcion


# CODIGO PRINCIPAL
ejecucción = True

while ejecucción:
    
    opcion_elegida = menu_principal()

    match opcion_elegida:
        case 1:
            # EJERCICIO 1
            intro_ejercicio(1)

            notas_estudiantes = [2, 6, 9, 1, 6, 10, 4, 4, 1, 10]

            mostrar_lista_horizontal(notas_estudiantes, "Las notas de los estudiantes son:")

            promedio = sum(notas_estudiantes)/len(notas_estudiantes)
            print(f"El promedio de las notas es: {promedio:.2f}")

            print(f"La nota más alta es: {max(notas_estudiantes)}")
            print(f"La nota más baja es: {min(notas_estudiantes)}")
            print()

        case 2:
            # EJERCICIO 2
            intro_ejercicio(2)

            print("A continuación deberá ingresar 5 productos (uno a la vez)")
            lista_productos = []
            CANTIDAD_PRODUCTOS = 5

            for i in range(CANTIDAD_PRODUCTOS):
                productos = input(f"Ingrese el producto N° {i+1}: ")
                lista_productos.append(productos.title())

            print("\nLista de productos (ordenados alfabeticamente)")
            lista_productos.sort()
            for a, p in enumerate(lista_productos):
                print(f"{a+1}) {p}")

            while True:
                try:
                    respuesta_1 = int(input("¿Que producto desea eliminar? Indiquelo por su número: "))
                except ValueError:
                    print(f"El valor ingresado no es un número!")
                else:
                    if respuesta_1 > CANTIDAD_PRODUCTOS:
                        print("Usted ha ingresado un número fuera del rango permitido!")
                    else:
                        respuesta_1 -= 1
                        break

            lista_productos.pop(respuesta_1)

            print("\nLa nueva lista de productos (ordenados alfabeticamente)")
            for a, p in enumerate(lista_productos):
                print(f"{a+1}) {p}")

        case 3:
            # EJERCICIO 3
            intro_ejercicio(3)

            numeros_aleatorios = lista_valores_aleatorios(1, 100, 15)
            mostrar_lista_horizontal(numeros_aleatorios, "Los 15 números aleatorios generados son:")
            lista_pares = []
            lista_impares = []

            for b in numeros_aleatorios:
                if b % 2 == 0:
                    lista_pares.append(b)
                else:
                    lista_impares.append(b)

            mostrar_lista_horizontal(lista_pares, f"Hay {len(lista_pares)} números que son pares, los cuales son:")
            print()
            mostrar_lista_horizontal(lista_impares, f"Hay {len(lista_impares)} números que son impares, los cuales son:")

        case 4:
            # EJERCICIO 4
            intro_ejercicio(4)

            datos_repetidos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
            lista_sin_duplicar = []
            # Pude haber ocupados sets en esta parte,
            # pero entiendo que no es el objetivo del ejercicio:
            # datos_repetidos_mod = set(datos_repetidos)
            # lista_sin_duplicar = list(datos_repetidos_mod)
            # print(datos_repetidos_mod_2)

            for d in datos_repetidos:
                if not(d in lista_sin_duplicar):
                    lista_sin_duplicar.append(d)
                else:
                    continue
            print("La lista original era: ", datos_repetidos)
            print("La lista sin datos duplicados es: ", lista_sin_duplicar)

        case 5:
            # EJERCICIO 5
            intro_ejercicio(5)
            nombre_estudiantes = ["Maxi", "Rocio", "Gustavo", "Flor",
                                  "Matias", "Romina", "Ignacio", "Melani"]
            
            while True:
                mostrar_lista_vertical(nombre_estudiantes,"Los estudiantes inscriptos son: ", True, ".- ")
                print("\nOpciones: \n1 - Agregar alumno | 2 - Borrar alumno | 3 - Volver al menu principal")
                accion = solicitar_numero(1, 3, "Opcion elegida (1/3): ")
                
                if accion == 1:
                    nombre_alumno_nuevo = input("Ahora ingrese el nombre del nuevo alumno: ").title()
                    nombre_estudiantes.append(nombre_alumno_nuevo)
                    input(f"Se ha agregado a {nombre_alumno_nuevo} a la lista! Presione alguna tecla para continuar...")
                elif accion == 2:
                    alumno_borrar = solicitar_numero(1,len(nombre_estudiantes), "Ahora ingrese el número del alumno que desee borrar: ")
                    borrado = nombre_estudiantes.pop(alumno_borrar-1)
                    input(f"Se ha borrado a {borrado} de la lista! Presione alguna tecla para continuar...")
                else:
                    break

        case 6:
            # EJERCICIO 6
            intro_ejercicio(6)
            valores_iniciales = lista_valores_aleatorios(1, 100, 7)
            print("La lista de valores iniciales es la siguiente: \n", valores_iniciales, "\n")
            ultimo_valor = valores_iniciales.pop(6)
            valores_iniciales.insert(0,ultimo_valor)
            print("Se ha desplazado cada valor una casilla a la derecha...\n")
            print("La nueva lista de valores iniciales es la siguiente: \n", valores_iniciales, "\n")

        case 7:
            # EJERCICIO 7
            intro_ejercicio(7)

            lista_anidada = [["Max", "Min", "Dia"]]
            dias_semana = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
            temp_max = []
            temp_min = []
            mayor_amplitud = 0
            dia_mayor_amplitud = ""

            for dia in dias_semana:
                n_temp_max = randint(25, 45)
                n_temp_min = randint(0, n_temp_max)
                amplitud_actual = n_temp_max - n_temp_min
                if mayor_amplitud < (amplitud_actual):
                    mayor_amplitud = amplitud_actual
                    temp_max_amplitud = n_temp_max
                    temp_min_amplitud = n_temp_min
                    dia_mayor_amplitud = dia

                temp_max.append(n_temp_max)
                temp_min.append(n_temp_min)
                lista_anidada.append([dia, n_temp_max, n_temp_min])

            for i in range(len(lista_anidada)):
                for j in lista_anidada[i]:
                    print(str(j).center(10," "), end=" ")
                print()
            promedio_max = sum(temp_max) / len(temp_max)
            promedio_min = sum(temp_min) / len(temp_min)

            print("\nMas información: ")
            print(f"  El promedio de las temperaturas maximas es de {promedio_max:.2f}°.")
            print(f"  Por otro lado, el promedio de las temperaturas minimas es de {promedio_min:.2f}° ")
            print(f"  El día con mayor amplitud termina es {dia_mayor_amplitud} con un diferencia de {mayor_amplitud}° entre la maxima ({temp_max_amplitud}) y la minima ({temp_min_amplitud})")

        case 8:
            # EJERCICIO 8
            intro_ejercicio(8)
            print()
            print("Notas de los alumnos".center(100, " "))
            print()
            lista_materias = ["Alumnos", "Matematicas", "Historia", "Literatura", "Promedio alumno"]
            estudiantes_octavo = ["Maxi", "Rocio", "Gustavo", "Flor", "Matias", "Promedio materia"]
            lista_parcial = []
            tabla_completa = [lista_materias]
            suma_acumulador = 0
            nota_matematica = 0
            nota_historia = 0
            nota_literatura = 0

            for i, est in enumerate(estudiantes_octavo):
                lista_parcial.append(est)

                if i == len(estudiantes_octavo)-1:
                    p_nota_matematica = round(nota_matematica/5, 2)
                    p_nota_historia = round(nota_historia/5, 2)
                    p_nota_literatura = round(nota_literatura/5, 2)
                    promedio_materia = [p_nota_matematica, p_nota_historia, p_nota_literatura]
                    suma_acumulador = sum(promedio_materia)

                    for p in promedio_materia:
                        lista_parcial.append(p)
                else:
                    for t in range(3):
                        nota_aleatoria = randint(1, 10)
                        lista_parcial.append(nota_aleatoria)
                        suma_acumulador += nota_aleatoria

                        match t:
                            case 0:
                                nota_matematica += nota_aleatoria
                            case 1:
                                nota_historia += nota_aleatoria
                            case 2:
                                nota_literatura += nota_aleatoria

                promedios_alumno = round(suma_acumulador/3, 2)
                lista_parcial.append(promedios_alumno)
                tabla_completa.append(lista_parcial)

                lista_parcial = []
                suma_acumulador = 0
            
            for i in range(len(tabla_completa)):
                for j in tabla_completa[i]:
                    print(str(j).center(17," "), end=" ")
                print()

        case 9:
            # EJERCICIO 9
            intro_ejercicio(9)
            print("TA TE TI")
            turno_x = True
            tateti = [["_","_","_"],
                      ["_","_","_"],
                      ["_","_","_"]]

            while True:
                for i, e in enumerate(tateti):
                    for j, d in enumerate(tateti[i]):
                        print(d, end=" ")
                    print()
                
                print("\nTurno del jugador " + ("1 (X)" if turno_x else "2 (O)"))
                fila = solicitar_numero(1, 3, " > Primero ingrese el número de fila: ")
                col = solicitar_numero(1, 3, " > Ahora ingrese el número de columna: " )

                while tateti[fila-1][col-1] != "_":
                    print("\nERROR! Acaba de seleccionar una celda que ya esta ocupada")
                    fila = solicitar_numero(1, 3, " > Primero ingrese el número de fila: ")
                    col = solicitar_numero(1, 3, " > Ahora ingrese el número de columna: " )

                tateti[fila-1][col-1] = "X" if turno_x else "O"
                
                turno_x = False if turno_x else True
                
                ganador = None
                for i in range(3):
                    if tateti[i][0] == tateti[i][1] == tateti[i][2] != "_":
                        ganador = tateti[i][0]
                    if tateti[0][i] == tateti[1][i] == tateti[2][i] != "_":
                        ganador = tateti[0][i]

                if tateti[0][0] == tateti[1][1] == tateti[2][2] != "_":
                    ganador = tateti[0][0]
                if tateti[0][2] == tateti[1][1] == tateti[2][0] != "_":
                    ganador = tateti[0][2]

                if ganador:
                    for fila_final in tateti:
                        print(" ".join(fila_final))
                    print(f"\n¡EL JUGADOR {ganador} HA GANADO!")
                    input("Presione una tecla para volver al menú...")
                    break

                celdas_vacias = False
                for f in tateti:
                    if "_" in f:
                        celdas_vacias = True
                if not celdas_vacias:
                    print("\n¡ES UN EMPATE!")
                    break


        case 10:
            # EJERCICIO 10
            intro_ejercicio(10)
            dias = ["1. Domingo", "2. Lunes", "3. Martes", "4. Miercoles", "5. Jueves", "6. Viernes", "7. Sabado", "Total producto"]
            ventas_totales = [["Meses", "Producto_1", "Producto_2", "Producto_3", "Producto_4", "Total mensual"]]
            
            for d in dias:
                lista_primaria = []
                lista_primaria.append(d)
                lista_zero = [0]*(len(ventas_totales[0])-1)
                lista_primaria.extend(lista_zero)
                ventas_totales.append(lista_primaria)

                produ_masvendido = 0
                nombre_prod_masvendido = "Ninguno"
                dia_masvendido = 0
                nombre_dia_masvendido = "Ninguno"
            
            while True:
                for i in range(len(ventas_totales)):
                    for j in range(len(ventas_totales[i])):
                        print(str(ventas_totales[i][j]).center(15, " "), end=" ")
                    print()
                
                max_ventas_prod = -1
                idx_prod = -1
                for j in range(1, 5):
                    if ventas_totales[8][j] > max_ventas_prod:
                        max_ventas_prod = ventas_totales[8][j]
                        idx_prod = j

                max_ventas_dia = -1
                idx_dia = -1
                for i in range(1, 8):
                    if ventas_totales[i][5] > max_ventas_dia:
                        max_ventas_dia = ventas_totales[i][5]
                        idx_dia = i

                print(f"\n> Producto más vendido: {ventas_totales[0][idx_prod]} ($ {max_ventas_prod} de ventas totales)")
                print(f"> Día con más ventas: {ventas_totales[idx_dia][0]} ($ {max_ventas_dia} de ventas totales)")

                print("\nCARGA DE VENTAS")
                fila = solicitar_numero(0, 7," > Seleccione el dia (1 a 7 | 0 para salir): ")
                if fila == 0:
                    break
                columna = solicitar_numero(0, 4, " > Ahora selecione el producto (1 a 4 | 0 para salir): ")
                if columna == 0:
                    break
                ventas_cargar = solicitar_numero(0,1000000000000, " >> Ingrese las ventas que desea cargar: ")

                ventas_totales[fila][columna] = ventas_cargar
                ventas_totales[fila][5] += ventas_cargar
                ventas_totales[8][columna] += ventas_cargar

        case 11:
            # EJERCICIO 11
            intro_ejercicio(11)

            base_nomb_estudiantes = ["Maxi", "Rocio", "Gustavo", "Flor", "Javier",
                                     "Matias", "Romina", "Ignacio", "Melani", "Cintia"]
            
            mostrar_lista_vertical(base_nomb_estudiantes, "Lista de estudiantes", True, ") ")
            print()

            buscado = input("Ingrese el nombre que desea buscar: ")

            if buscado in base_nomb_estudiantes:
                print("El nombre se encuentra en la lista!")
                print(f"El mismo figura en el orden {base_nomb_estudiantes.index(buscado)+1}")
            else:
                print("El nombre ingresado NO figura en la lista!")

        case 12:
            # EJERCICIO 12
            intro_ejercicio(12)

            listado_original = []
            for i in range(8):
                num_elegido = solicitar_numero(1,1000000000, "Ingrese un número: ")
                listado_original.append(num_elegido)

            mostrar_lista_horizontal(listado_original, "\nLa lista ingresada es:")

            listado_original.sort()
            mostrar_lista_horizontal(listado_original, "\nAhora, si la lista se ordena de menor a mayor seria: ")

            listado_original.sort(reverse=True)
            mostrar_lista_horizontal(listado_original, "\nFinalmente, si la lista se ordena de mayor a menor seria: ")

        case 13:
            # EJERCICIO 13
            intro_ejercicio(13)

            puntajes = [450, 1200, 875, 990, 300, 1500, 640]
            mostrar_lista_horizontal(puntajes,"Puntajes del juego:")
            
            print("\nMás información")
            print(f"> El puntaje más alto es: {max(puntajes)}")
            print(f"> El puntaje más bajo es: {min(puntajes)}")
            puntajes_ascendente = puntajes
            puntajes_ascendente.sort(reverse=True)
            
            mostrar_lista_vertical(puntajes_ascendente,"\nRanking de puntajes",True,") ")

            print(f"\nEl puntaje 990 se encuentra en el puesto N° {puntajes_ascendente.index(990)+1} del ranking!")

        case 14:
            break


