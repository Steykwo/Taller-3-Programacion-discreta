#LVFF

print("\n      .*+° ¡Bienvenido al programa de Entropía de Shannon! °+*.")
print("\n|| La entropía de Shannon mide cuánta información contiene una fuente. ||")
print("|| - Un texto muy repetitivo tiene menos incertidumbre.                ||")
print("|| - Se usa la frecuencia y probabilidad de cada símbolo               ||")

while True:
    # Menú de opciones para el usuario
    print("\n" + "=" * 75)
    print("  Por favor elija lo que desea hacer:")
    print("  1. Calcular entropía de un texto")
    print("  2. Comparar la entropía entre dos textos")
    print("  3. Salir del programa")
    print("=" * 75)
    
    opcion = input("\nIngrese el número de la opción (1, 2 o 3): ")

    # Opción 1: Calcular entropía de un texto
    if opcion == "1":
        print("\n.*+° Cálculo de Entropía °+*.")
        
        import math
        
        # Pedir el texto al usuario
        texto = input("\nPor favor ingrese el texto: ")
        
        # Contar frecuencia de cada símbolo
        frecuencia = {}
        for caracter in texto:
            if caracter in frecuencia:
                frecuencia[caracter] += 1
            else:
                frecuencia[caracter] = 1
        
        # Calcular probabilidad de cada símbolo
        total = len(texto)
        entropia = 0
        
        print("\n" + "-" * 75)
        print("Símbolo | Frecuencia | Probabilidad")
        print("-" * 75)
        
        for simbolo, count in frecuencia.items():
            probabilidad = count / total
            entropia -= probabilidad * math.log2(probabilidad)
            porcentaje = probabilidad * 100
            
            print(f"  {simbolo}    |    {count}     |    {porcentaje:.4f}%")
        
        print("-" * 75)
        print(f"\nLongitud del texto: {total} caracteres")
        print(f"Cantidad de símbolos distintos: {len(frecuencia)}")
        print(f"Entropía de Shannon: {entropia:.4f} bits")

        # Entropía máxima

        num_simbolos = len(frecuencia)
        entropia_maxima = math.log2(num_simbolos)
        porcentaje_entropia = (entropia / entropia_maxima) * 100 if entropia_maxima > 0 else 0
        
        # Interpretación de la entropía
        print("\n" + "-" * 75)
        if entropia == 0:
            print("El texto no tiene entropía -> Sin información nueva.")
        elif porcentaje_entropia <= 30:
            print("El texto tiene baja entropía -> Predecible y repetitivo.")
        elif porcentaje_entropia <= 70:
            print("El texto tiene entropía media -> Patrones mixtos.")
        elif porcentaje_entropia < 100:
            print("El texto tiene alta entropía -> Muy variado y e impredecible.")
        else: 
            print("El texto tiene una entropía máxima -> Totalmente aleatorio.")
        print("-" * 75)

    # Opción 2: Comparar dos textos
    elif opcion == "2":
        print("\n.*+° Comparación de Entropía °+*.")
        
        import math
        
        # Función para calcular entropía de un texto
        def calcular_entropia(texto):
            frecuencia = {}
            for caracter in texto:
                if caracter in frecuencia:
                    frecuencia[caracter] += 1
                else:
                    frecuencia[caracter] = 1
            
            total = len(texto)
            entropia = 0
            
            for count in frecuencia.values():
                probabilidad = count / total
                entropia -= probabilidad * math.log2(probabilidad)
            
            return entropia, len(frecuencia)
        
        # Pedir los dos textos
        print("\ntexto 1:")
        texto1 = input("Ingrese el primer texto: ")
        
        print("\ntexto 2:")
        texto2 = input("Ingrese el segundo texto: ")
        
        # Calcular entropía de cada texto
        entropia1, distintos1 = calcular_entropia(texto1)
        entropia2, distintos2 = calcular_entropia(texto2)
        
        # Mostrar resultados
        print("\n" + "-" * 75)
        print("Comparación de textos:")
        print("-" * 75)
        
        print(f"\ntexto 1: '{texto1}'")
        print(f"  - Longitud: {len(texto1)} caracteres")
        print(f"  - Símbolos distintos: {distintos1}")
        print(f"  - Entropía: {entropia1:.4f} bits")
        
        print(f"\ntexto 2: '{texto2}'")
        print(f"  - Longitud: {len(texto2)} caracteres")
        print(f"  - Símbolos distintos: {distintos2}")
        print(f"  - Entropía: {entropia2:.4f} bits")
        
        # Comparar
        print("\n" + "-" * 75)
        if entropia1 > entropia2:
            print(f"El texto 1 tiene mayor entropía ({entropia1:.4f} > {entropia2:.4f})")
            print("-> El texto 1 es más variado y contiene más información.")
        elif entropia2 > entropia1:
            print(f"El texto 2 tiene mayor entropía ({entropia2:.4f} > {entropia1:.4f})")
            print("-> El texto 2 es más variado y contiene más información.")
        else:
            print(f"Ambos textos tienen la misma entropía ({entropia1:.4f})")
            print("-> Contienen la misma cantidad de información.")
        print("-" * 75)

    # Opción 3: Salir
    elif opcion == "3":
        print("\n¡Gracias por usar el programa!")
        break

    # Opción Inválida
    else:
        print("\nOpción no válida. Debe ser 1, 2 o 3.")
