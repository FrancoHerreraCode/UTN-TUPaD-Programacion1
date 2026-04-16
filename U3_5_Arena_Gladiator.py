
# VARIABLES PREDEFINIDAS
vida_gladiador = 100  
vida_enemigo = 100  
pociones_vida = 3    
dano_base_personaje = 15 #ATAQUE PESADO 
dano_base_enemigo = 12  
turno_gladiador = True  


# PIDE NOMBRE AL JUGADOR
print("ESCAPE ROOM: LA ARENA DEL GLADIADOR".center(100,"."))
print("."*100)
nombre_gladiador = input("Ingrese el nombre del gladiador: ")
while not(nombre_gladiador.isalpha()):
    print("Error: Solo se permiten letras")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")
input("\nIniciando el juego. Presione cualquier tecla para continuar...")


# BUCLE PRINCIPAL
while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador == True:
        print("")
        print("TU TURNO GLADIADOR".center(70 ,"-"))
        print("\nEstado:")
        print(f"Gladiador {nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
        print("\nAcciones:")
        print("1) Ataque pesado.\n2) Ráfaga veloz.\n3) Curar\n")
        opcion = input("Opcion elegida: ")
        while not(opcion.isdigit() and opcion in ("1","2","3")):
            print("El valor ingresado no es valido!")
            opcion = input("Opcion elegida: ")
        opcion = int(opcion)
        print("")

        if opcion == 1:
            print(">> ¡Inicias ataque pesado!")
            if vida_enemigo < 20:
                dano_turno = 1.5*dano_base_personaje
            else:
                dano_turno = dano_base_personaje
            vida_enemigo -= dano_turno
            print(f"> ¡Atacaste al enemigo por {float(dano_turno):.2f} puntos de daño!")
            input("\nPresione cualquier tecla para continuar...")

        elif opcion == 2:
            dano_turno = 5
            print(">> ¡Inicias una ráfaga de golpes!")
            for a in range(3):
                vida_enemigo -= dano_turno
                print(f"> Golpe conectado por {float(dano_turno):.2f} puntos de daño")
            
            input("\nPresione cualquier tecla para continuar...")
        
        elif opcion == 3:
            if pociones_vida > 0:
                print(">> Estas tomando una poción")
                pociones_vida -= 1
                recupero_vida = 30 if vida_gladiador <= 70 else (100-vida_gladiador)
                vida_gladiador += recupero_vida
                print(f"> Recuperaste {recupero_vida} puntos de vida")
                input("\nPresione cualquier tecla para continuar...")
            else:
                print(">> ¡No quedan pociones!")
        turno_gladiador = False
    else:
        print("")
        print("EL TURNO DE TU OPONENTE".center(70 ,"-"))
        vida_gladiador -= dano_base_enemigo
        print(f"\n>> ¡El enemigo te atacó por {dano_base_enemigo} puntos de daño!")
        turno_gladiador = True
    
# DESENLACE
print("\n\n")
print("-" * 70)
if vida_gladiador > 0:
    print(f">>> ¡VICTORIA! {nombre_gladiador} ha ganado la batalla. <<<".center(70, " "))

else:
    print(">>> DERROTA. Has caído en combate<<<".center(70, " "))
    
    

print("FIN DEL JUEGO".center(70,"."))