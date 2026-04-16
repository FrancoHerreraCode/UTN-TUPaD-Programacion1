#CREDENCIALES POR DEFECTO
user = "alumno"
password = "python123"
intentos = 0
acceso = False
bucle_principal = True

while bucle_principal:
    print("ACCESO AL CAMPUS".center(50,"."))

    for i in range(3):
        print(f"intento {i+1}/3")
        intento_user = input("Usuario: ")
        intento_password = input("Contraseña: ")
        
        if intento_user == user and intento_password == password:
            print("Acceso concedido...\n")
            intentos = 0
            acceso = True
            break
        elif i == 2:
            print("Error: credenciales inválidas.\nCuenta bloqueada.\n")
            bucle_principal = False
        else:
            print("Error: credenciales inválidas.\n")

    while acceso:
        print("MENU PRINCIPAL".center(40,"."))
        print("Opciones: ")
        print("1) Estado de inscripción.\n2) Cambiar clave.\n3) Mensaje motivacional.\n4) Salir.\n")

        opcion = input("Ingrese la opcion elegida (1 a 4): ")
        opciones_validas = ["1","2","3","4"]

        while not(opcion.isdigit() and opcion in opciones_validas):
            if opcion.isdigit():
                print("Error: opción fuera de rango.")
            else:
                print("Error: ingrese un número válido.")
            opcion = input("Ingrese la opcion elegida (1 a 4): ")

        opcion = int(opcion)
        print("")
        
        if opcion == 1:
            print("Estado de inscripción: Inscripto!")
            input("Presione cualquier tecla para continuar\n")
        elif opcion == 2:
            nueva_clave_1 = input("Ingrese su nueva clave: ")
            nueva_clave_2 = input("Repita su nueva clave: ")

            while not(len(nueva_clave_1) >= 6 and nueva_clave_1 == nueva_clave_2):
                if nueva_clave_1 != nueva_clave_2:
                    print("Las contraseñas ingresadas no coinciden.")
                else:
                    print("La nueva contraseña debe tener 6 caracteres como minimo.")

                nueva_clave_1 = input("Ingrese su nueva clave: ")
                nueva_clave_2 = input("Repita su nueva clave: ")
            password = nueva_clave_1
            acceso = False
            print("Cambio de clave exitoso!")
            print("Debe volver a ingresar...\n")
            input("Presione cualquier tecla para continuar")
            break
        elif opcion == 3:
            print("Aqui va el mensaje motivacional xD")
            input("Presione cualquier tecla para continuar\n")
        else:
            input("Cerrando sesión... Presione cualquier tecla para continuar")
            bucle_principal = False
