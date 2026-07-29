#LVFF

print("\n             .*+° ¡Bienvenido al programa de RSA de Juguete! °+*.")
print("\n|| RSA es un sistema criptográfico basado en aritmética modular.                ||")
print("|| Se usa una versión pequeña para entender la idea matemática.                 ||")
print("|| - Se reciben dos números primos p, q y un exponente público e.               ||")
print("|| - Se calcula n = p*q y φ(n) = (p-1)*(q-1).                                   ||")
print("|| - Se calcula d, el inverso modular de e módulo φ(n).                         ||")
print("|| - Con esto se puede cifrar y descifrar mensajes.                             ||")

while True:
    # Menú de opciones para el usuario
    print("\n" + "=" * 82)
    print("  Por favor elija lo que desea hacer:")
    print("  1. Generar llaves y cifrar/descifrar un mensaje")
    print("  2. Salir del programa")
    print("=" * 82)
    
    opcion = input("\nIngrese el número de la opción (1 o 2): ")

    # Opción 1: RSA completo
    if opcion == "1":
        print("\n.*+° Generación de llaves RSA °+*.")
        
        # Función para verificar si un número es primo
        def es_primo(numero):
            if numero < 2:
                return False
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    return False
            return True
        
        # Función para calcular el MCD (Euclides)
        def mcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        # Función para el algoritmo de Euclides extendido
        def mcd_extendido(a, b):
            if b == 0:
                return (a, 1, 0)
            mcd, x1, y1 = mcd_extendido(b, a % b)
            return (mcd, y1, x1 - (a // b) * y1)
        
        # Función para calcular el inverso modular
        def inverso_modular(e, phi):
            mcd, x, _ = mcd_extendido(e, phi)
            if mcd != 1:
                return None  # No existe inverso
            return x % phi
        
        # Pedir el número primo p con validación
        while True:
            try:
                p = int(input("\nIngrese el número primo p: "))
                if p < 2:
                    print("El número debe ser mayor o igual a 2.")
                elif not es_primo(p):
                    print(f"{p} no es un número primo. Por favor ingrese un número primo.")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Pedir el número primo q con validación
        while True:
            try:
                q = int(input("Ingrese el número primo q: "))
                if q < 2:
                    print("El número debe ser mayor o igual a 2.")
                elif not es_primo(q):
                    print(f"{q} no es un número primo. Por favor ingrese un número primo.")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Pedir el exponente público e
        while True:
            try:
                e = int(input("Ingrese el exponente público e: "))
                if e < 1:
                    print("e debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Calcular n y φ(n)
        n = p * q
        phi = (p - 1) * (q - 1)
        
        print("\n" + "-" * 82)
        print(f"n = p * q = {p} * {q} = {n}")
        print("\n" + f"φ(n) = (p-1)*(q-1) = {p-1} * {q-1} = {phi}")
        
        # Verificar que e sea válido (coprimo con φ(n))
        if mcd(e, phi) != 1:
            print(f"\n e = {e} NO es válido porque no es coprimo con φ(n) = {phi}")
            print("   El MCD(e, φ(n)) debe ser 1. Intente con otro valor de e.")
            print("-" * 82)
            continue  # Vuelve al menú
        
        # Calcular el inverso modular d
        d = inverso_modular(e, phi)
        print(f"\nd = inverso de {e} módulo {phi} = {d}")
        print("-" * 82)
        
        # Pedir el mensaje a cifrar
        while True:
            try:
                M = int(input("\nIngrese el mensaje a cifrar (número entero): "))
                if M < 0:
                    print("Por favor ingrese un número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un número entero válido.")
        
        # Cifrar el mensaje
        C = pow(M, e, n)
        print(f"\nCifrado: C = {M}^{e} mod {n} = {C}")
        
        # Descifrar el mensaje
        M_descifrado = pow(C, d, n)
        print(f"Descifrado: M = {C}^{d} mod {n} = {M_descifrado}")
        
        # Verificar que funciona
        print("\n" + "-" * 82)
        if M == M_descifrado:
            print("¡El cifrado y descifrado funcionaron correctamente!")
        else:
            print("El mensaje descifrado no coincide con el original.")
        print("-" * 82)

    # Opción 2: Salir
    elif opcion == "2":
        print("\n¡Gracias por usar el programa!")
        break

    # Opción Inválida
    else:
        print("\nOpción no válida. Debe ser 1 o 2.")
