
print("AGENDA DE TURNOS".center(50 ,"_"))
ejecuccion = True
turnos_lunes_ocupados = 0
turnos_martes_ocupados = 0

lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""
martes_1 = ""
martes_2 = ""
martes_3 = ""


# PIDE EL NOMBRE DEL OPERADOR.
nombre_operador = input("Ingrese el nombre del operador: ")
while not(nombre_operador.isalpha()):
    print("El valor ingresado no es valido!")
    nombre_operador = input("Ingrese el nombre del operador: ")

#BLOQUE DE CODIGO PRINCIPAL
while ejecuccion:
    print("")
    print("MENU PRINCIPAL".center(50 ,"."))
    print(f"Operador: {nombre_operador.title()}")
    print("Opciones:")
    print("1) Reserva de turno.\n2) Cancelar turno.\n3) Ver agenda del día.\n4) Ver resumen general.\n5) Cerrar sistema.\n")
    opcion = input("Opcion elegida: ")
    while not(opcion.isdigit() and opcion in ",1,2,3,4,5,"):
        print("El valor ingresado no es valido!")
        opcion = input("Opcion elegida: ")
    opcion = int(opcion)

    if opcion == 1:
        print("Reserva de turno".center(50, "."))
        #ELECCION DEL DIA DEL TURNO
        print("Seleccion un dia:\n1) Lunes.\n2) Martes.")
        dia_turno = input("Dia elegido (1/2): ")
        while not(dia_turno.isdigit() and dia_turno in ",1,2,"):
            print("El valor ingresado no es valido!")
            dia_turno = input("Dia elegido (1/2): ")
        dia_turno = int(dia_turno)

        #NOMBRE DEL PACIENTE
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not(nombre_paciente.isalpha()):
            print("El valor ingresado no es valido!")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
        nombre_paciente = nombre_paciente.title()


        #VERIFICACION DE QUE EL PACIENTE NO ESTE REPETIDO
        bandera_no_existe = False
        if lunes_1 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Lunes - 1er turno")
        elif lunes_2 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Lunes - 2do turno")
        elif lunes_3 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Lunes - 3er turno")
        elif lunes_4 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Lunes - 4to turno")
        elif martes_1 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Martes - 1er turno")
        elif martes_2 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Martes - 2do turno")
        elif martes_3 == nombre_paciente:
            print("El paciente ya tiene asignado un turno: Martes - 3er turno")
        else:
            bandera_no_existe = True

        # ASIGNACION DEL TURNO
        bandera_reserva = True
        if (dia_turno == 1 and bandera_no_existe):
            if lunes_1 == "":
                lunes_1 = nombre_paciente
                turnos_lunes_ocupados += 1
            elif lunes_2 == "":
                lunes_2 = nombre_paciente
                turnos_lunes_ocupados += 1
            elif lunes_3 == "":
                lunes_3 = nombre_paciente
                turnos_lunes_ocupados += 1
            elif lunes_4 == "":
                lunes_4 = nombre_paciente
                turnos_lunes_ocupados += 1
            else:
                bandera_reserva = False
                print("No hay turnos disponibles para el lunes!")
        elif (dia_turno == 2 and bandera_no_existe):
            if martes_1 == "":
                martes_1 = nombre_paciente
                turnos_martes_ocupados += 1
            elif martes_2 == "":
                martes_2 = nombre_paciente
                turnos_martes_ocupados += 1
            elif martes_3 == "":
                martes_3 = nombre_paciente
                turnos_martes_ocupados += 1
            else:
                bandera_reserva = False
                print("No hay turnos disponibles para el martes!")
        else:
            bandera_reserva = False

        if bandera_reserva:
            print("Se ha agendado el turno con exito!")
            bandera_reserva = False
        input("\nPresione alguna tecla para continuar...")

    elif opcion == 2:
        print("Cencelación de turno".center(50, "."))

        #ELECCION DEL DIA DEL TURNO A CANCELAR
        print("Seleccion un dia:\n1) Lunes.\n2) Martes.")
        dia_turno = input("Dia elegido (1/2): ")
        while not(dia_turno.isdigit() and dia_turno in ",1,2,"):
            print("El valor ingresado no es valido!")
            dia_turno = input("Dia elegido (1/2): ")
        dia_turno = int(dia_turno)

        #NOMBRE DEL PACIENTE
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not(nombre_paciente.isalpha()):
            print("El valor ingresado no es valido!")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
        nombre_paciente = nombre_paciente.title()
        
        # BUSQUEDA Y REESCRITURA DEL TURNO
        bandera_eliminar = True
        if dia_turno == 1:
            if lunes_1 == nombre_paciente:
                lunes_1 = ""
                turnos_lunes_ocupados -= 1
            elif lunes_2 == nombre_paciente:
                lunes_2 = ""
                turnos_lunes_ocupados -= 1
            elif lunes_3 == nombre_paciente:
                lunes_3 = ""
                turnos_lunes_ocupados -= 1
            elif lunes_4 == nombre_paciente:
                lunes_4 = ""
                turnos_lunes_ocupados -= 1
            else:
                bandera_eliminar = False
                print(f"No hay turnos asignados {nombre_paciente} para el dia lunes")
        else:
            if martes_1 == nombre_paciente:
                martes_1 = ""
                turnos_martes_ocupados -= 1
            elif martes_2 == nombre_paciente:
                martes_2 = ""
                turnos_martes_ocupados -= 1
            elif martes_3 == nombre_paciente:
                martes_3 = ""
                turnos_martes_ocupados -= 1
            else:
                bandera_eliminar = False
                print(f"No hay turnos asignados {nombre_paciente} para el dia martes")
        if bandera_eliminar:
            print("Se ha eliminado el turno con exito!")
            bandera_eliminar = False
        input("\nPresione alguna tecla para continuar...")
    
    elif opcion == 3:
        print("Agenda de turnos diaria".center(50, "."))

        #ELECCION DEL DIA DEL TURNO A CANCELAR
        print("Seleccion un dia:\n1) Lunes.\n2) Martes.")
        dia_turno = input("Dia elegido (1/2): ")
        while not(dia_turno.isdigit() and dia_turno in ",1,2,"):
            print("El valor ingresado no es valido!")
            dia_turno = input("Dia elegido (1/2): ")
        dia_turno = int(dia_turno)

        # BUSQUEDA Y REESCRITURA DEL TURNO
        if dia_turno == 1:
            print("Turnos del día lunes".center(50, "."))
            print("Turno N° 1:", "Libre" if lunes_1 =="" else lunes_1)
            print("Turno N° 2:", "Libre" if lunes_2 =="" else lunes_2)
            print("Turno N° 3:", "Libre" if lunes_3 =="" else lunes_3)
            print("Turno N° 4:", "Libre" if lunes_4 =="" else lunes_4)
        else:
            print("Turnos del día martes".center(50, "."))
            print("Turno N° 1:", "Libre" if martes_1 =="" else martes_1)
            print("Turno N° 2:", "Libre" if martes_2 =="" else martes_2)
            print("Turno N° 3:", "Libre" if martes_3 =="" else martes_3)
        input("Presione alguna tecla para continuar...")

    elif opcion == 4:
        print("Resumen general de turnos".center(50, "."))

        turnos_lunes_disponibles = 4 - turnos_lunes_ocupados
        turnos_martes_disponibles = 3 - turnos_martes_ocupados

        dia_mas_turnos = ""
        if turnos_lunes_ocupados > turnos_martes_ocupados:
            dia_mas_turnos = "Lunes"
        elif turnos_lunes_ocupados < turnos_martes_ocupados:
            dia_mas_turnos = "Martes"
        else:
            dia_mas_turnos = "Ambos (Empate)"

        print("El día con más turnos ocupados es: " + dia_mas_turnos)

        print("\nTurnos del día lunes")
        print(f" - Disponibles: {turnos_lunes_disponibles}")
        print(f" - Ocupados: {turnos_lunes_ocupados}")

        print("\nTurnos del día martes")
        print(f" - Disponibles: {turnos_martes_disponibles}")
        print(f" - Ocupados: {turnos_martes_ocupados}")
        input("\nPresione alguna tecla para continuar...")

    else:
        input("Gracias por ocupar nuestro sistema! Presione una tecla para continuar...")
        ejecuccion = False
    