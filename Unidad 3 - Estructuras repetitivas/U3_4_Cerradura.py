
# VARIABLES POR DEFECTO
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
bloque_alarma = False
regla_antispam = 0

print("ESCAPE ROOM: LA BÓVEDA".center(100,"."))
print("""Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.""")
print("."*100)
nombre_agente = input("Ingrese el nombre del agente: ")
while not(nombre_agente.isalpha()):
    print("El valor ingresado no es valido!")
    nombre_agente = input("Ingrese el nombre del agente: ")
input("\nIniciando el juego. Presione cualquier tecla para continuar...")


#DESARROLLO DEL JUEGO
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not(bloque_alarma):
    print("")
    print("MENU PRINCIPAL".center(70 ,"."))
    print(f"Bienvenido agente {nombre_agente.title()}")
    print("\nEstado:")
    print(f"Energia: {energia} - Tiempo: {tiempo} - Cerraduras abiertas: {cerraduras_abiertas} - Alarma: ", "Encendida" if alarma else "Apagada")
    print("\nAcciones:")
    print("1) Forzar cerradura.\n2) Hackear panel.\n3) Descansar\n")
    opcion = input("Opcion elegida: ")
    while not(opcion.isdigit() and opcion in ("1","2","3")):
        print("El valor ingresado no es valido!")
        opcion = input("Opcion elegida: ")
    opcion = int(opcion)

    if alarma and tiempo <= 3:
        bloque_alarma = True
        print("Oh no! Se ha bloqueado la boveda por alarma!")
        input("Presione cualquier tecla para continuar")
        continue

    if opcion == 1:
        regla_antispam += 1
        energia -= 20
        tiempo -= 2
        print("\nSe ha consumido: -20 Energia y -2 Tiempo")

        if regla_antispam == 3:
            regla_antispam = 0
            alarma = True
            print("Oh no! Se ha activado la alarma porque se ha trabado la cerradura!")
        elif energia < 40:
            print("Hay riesgo de alarma! Deberas elegir una numero del 1 al 3 para continuar")
            numero = input("Número elegido: ")
            while not(numero.isdigit() and numero in ("1","2","3")):
                print("El valor ingresado no es valido!")
                numero = input("Opcion elegida: ")
            numero = int(numero)

            if numero == 3:
                alarma = True
                print("Oh no! Se ha activado la alarma!")
            else:
                cerraduras_abiertas += 1
                print("Buena elección! Todo normal por aqui")
        else:
            cerraduras_abiertas += 1
            print("Bien! Has logrado abrir una cerradura")
        
        input("Presione cualquier tecla para continuar")
    elif opcion == 2:
        regla_antispam = 0
        energia -= 10
        tiempo -= 3
        print("\nSe ha consumido: -10 Energia y -3 Tiempo")

        for i in range (4):
            print("Hackeando el sistema...")
            codigo_parcial += "A"
        print("")
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("Lograste hackear el sitema! Se ha abierto una cerradura")
        else:
            print("No se ha logrado hackear el sistema")
        
        input("Presione cualquier tecla para continuar")
    
    elif opcion == 3:
        regla_antispam = 0
        variacion_energia = 0
        if alarma:
            variacion_energia += (5 if energia <= 95 else (100-energia))
        else:
            variacion_energia += (15 if energia <= 85 else (100-energia))
        energia += variacion_energia
        tiempo -= 1
        print(f"Resultado del descando: + {variacion_energia} Energia y -1 Tiempo")
        input("Presione cualquier tecla para continuar")

# DESENLACE DEL JUEGO

if cerraduras_abiertas == 3:
    print("Felicitaciones! Has ganado el juego!!")
elif energia <= 0:
    print("Ya no te quedan energias... Has perdido el juego!!")
elif tiempo <= 0:
    print("Se te agoto el tiempo... Has perdido el juego!!")
elif bloque_alarma:
    print("Se ha producido el bloque por alarma... Has perdido el juego!!")