#LVFF

print("\n                         .*+° ¡Bienvenido al programa de Cifrado César! °+*.")
print("\n|| En el cifrado César se desplaza cada letra de un texto cifrado un cierto número de posiciones 'k': ||")
print("|| - Si se quiere cifrar un texto, el cifrado mueve la posición de cada letra k veces hacia adelante. ||")
print("|| - Si se conoce k, el descifrado mueve la posición de cada letra k veces hacia atrás.               ||")
print("|| - También se puede realizar un descrifrado con fuerza bruta si se desconoce k:                     ||")
print("||   Es decir, el texto se mueve un total de 25 posibles k, y se revisa cuál de ellos tiene sentido.  ||")
print("|| El programa conserva espacios, mayúsculas, signos de puntuación y números.                         ||")

while True:
    # Menú de opciones para el usuario
    print("\n" + "=" * 104)
    print("  Por favor elija lo que desea hacer:")
    print("  1. Cifrar un texto con desplazamiento k")
    print("  2. Descifrar un texto (conociendo k)")
    print("  3. Descrifrar probando todos los desplazamientos k (si no se conoce k)")
    print("  4. Salir del programa")
    print("=" * 104)
    
    opcion = input("\nIngrese el número de la opción (1, 2, 3 o 4): ")

    # Definición del alfabeto sin la ñ.

    ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Opción 1: Cifrar Texto

    if opcion == "1":
        print("\n.*+° Cifrado de texto °+*.")

        texto = input("\n Ingrese el texto a cifrar: ")
        
        # Pedir desplazamiento k
        while True:
            try:
                k = int(input("Ingrese el desplazamiento (k) deseado: "))
                break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Cifrar el texto
        resultado = ""
        for caracter in texto:
            if caracter.isalpha():
                mayus = caracter.isupper()
                letra = caracter.upper()
                posicion = ALFABETO.index(letra)
                N_posicion = (posicion + k) % 26 # Sumamos la posición para cifrar
                N_letra = ALFABETO[N_posicion]
                
                if mayus:
                    resultado += N_letra
                else:
                    resultado += N_letra.lower()
            else:
                resultado += caracter
        
        print("\n" + "-" * 104)
        print(f"Texto original:   {texto}")
        print(f"Desplazamiento k:   {k}")
        print(f"Texto cifrado:    {resultado}")
        print("-" * 104)

    # Opción 2: Descifrar con k

    elif opcion == "2":
        print("\n.*+° Descrifrado de texto °+*.")
        texto = input("Ingrese el texto cifrado: ")
        
        # Pedir desplazamiento k con validación
        while True:
            try:
                k = int(input("Ingrese el desplazamiento usado para cifrar (k): "))
                break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Descifrar usando el desplazamiento contrario (-k)
        resultado = ""
        for caracter in texto:
            if caracter.isalpha():
                mayus = caracter.isupper()
                letra = caracter.upper()
                posicion = ALFABETO.index(letra)
                N_posicion = (posicion - k) % 26  # Restamos en lugar de sumar para descifrar
                N_letra = ALFABETO[N_posicion]
                
                if mayus:
                    resultado += N_letra
                else:
                    resultado += N_letra.lower()
            else:
                resultado += caracter
        
        print("\n" + "-" * 104)
        print(f"Texto cifrado:    {texto}")
        print(f"Desplazamiento:   {k}")
        print(f"Texto descifrado: {resultado}")
        print("-" * 104)

    # Opción 3: Descifrar sin k

    elif opcion == "3":
        print("\n.*+° Descifrado con fuerza bruta °+*.")
        texto = input("Ingrese el texto cifrado: ")
        
        print("\n" + "=" * 104)
        print("Probando todos los desplazamientos (0 a 25):")
        print("=" * 104)
        
        # Probar todos los desplazamientos
        for k in range(26):
            resultado = ""
            for caracter in texto:
                if caracter.isalpha():
                    mayus = caracter.isupper()
                    letra = caracter.upper()
                    posicion = ALFABETO.index(letra)
                    N_posicion = (posicion - k) % 26  # Restamos para descifrar
                    N_letra = ALFABETO[N_posicion]
                    
                    if mayus:
                        resultado += N_letra
                    else:
                        resultado += N_letra.lower()
                else:
                    resultado += caracter
            
            print(f"{k:2} | {resultado}")
        
        print("-" *104)
        print(" -> Busca entre los resultados el que parezca un mensaje con sentido:")
        print("    Ese será el mensaje descifrado.")
        print("-" *104)

    # Opción 4: Salir
    elif opcion == "4":
        print("\n¡Gracias por usar el programa!")
        break

    # Opción Inválida
    else:
        print("\nOpción no válida. Debe ser 1, 2, 3 o 4.")
