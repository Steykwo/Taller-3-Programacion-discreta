#LVFF

print("\n             .*+° ¡Bienvenido al programa de MPC Básico! °+*.")
print("\n|| MPC (Computación Multipartita Segura) permite calcular un promedio     ||")
print("|| sin revelar los datos individuales de cada estudiante.                 ||")
print("|| - Cada nota se divide en 3 partes aleatorias módulo M.                 ||")
print("|| - Cada servidor recibe una parte de cada nota.                         ||")
print("|| - Al final se reconstruye únicamente la suma total y el promedio.      ||")
print("|| - Ningún servidor por sí solo puede conocer las notas originales.      ||")

while True:
    # Menú de opciones para el usuario
    print("\n" + "=" * 76)
    print("  Por favor elija lo que desea hacer:")
    print("  1. Calcular promedio de notas de forma segura")
    print("  2. Salir del programa")
    print("=" * 76)
    
    opcion = input("\nIngrese el número de la opción (1 o 2): ")

    # Opción 1: Calcular promedio seguro
    if opcion == "1":
        print("\n.*+° Cálculo de promedio seguro °+*.")
        
        import random
        
        # Módulo grande para las operaciones
        M = 1000007
        
        # Pedir las notas al usuario
        while True:
            try:
                num_notas = int(input("\n¿Cuántas notas desea ingresar? "))
                if num_notas <= 0:
                    print("Debe ingresar al menos una nota.")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Lista para almacenar las notas
        notas = []
        
        # Pedir cada nota
        for i in range(num_notas):
            while True:
                try:
                    nota = int(input(f"Ingrese la nota {i+1} (0-50): "))
                    if nota < 0 or nota > 50:
                        print("La nota debe estar entre 0 y 50.")
                    else:
                        notas.append(nota)
                        break
                except ValueError:
                    print("Por favor ingrese un número entero válido.")
        
        # Inicializar los 3 servidores
        servidor1 = 0
        servidor2 = 0
        servidor3 = 0
        
        # Dividir cada nota y distribuir entre servidores
        for nota in notas:
            # Generar dos partes aleatorias
            s1 = random.randint(0, M - 1)
            s2 = random.randint(0, M - 1)
            # La tercera parte se calcula para que la suma sea la nota
            s3 = (nota - s1 - s2) % M
            
            # Cada servidor recibe una parte
            servidor1 = (servidor1 + s1) % M
            servidor2 = (servidor2 + s2) % M
            servidor3 = (servidor3 + s3) % M
        
        # Reconstruir la suma total
        suma_total = (servidor1 + servidor2 + servidor3) % M
        
        # Calcular el promedio
        promedio = suma_total / len(notas)
        
        # Salida principal: suma y promedio
        print("\n" + "-" * 76)
        print(f"Suma total: {suma_total}")
        print(f"Promedio: {promedio:.2f}")
        print("-" * 76)

    # Opción 2: Salir
    elif opcion == "2":
        print("\n¡Gracias por usar el programa!")
        break

    # Opción Inválida
    else:
        print("\nOpción no válida. Debe ser 1 o 2.")
