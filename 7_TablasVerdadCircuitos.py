#LVFF

print("\n          .*+° ¡Bienvenido al programa de Tablas de Verdad! °+*.")
print("\n|| Las tablas de verdad permiten revisar todas las posibilidades       ||")
print("|| de una expresión lógica. En electrónica digital, estas expresiones  ||")
print("|| se interpretan como circuitos.                                      ||")
print("|| - Se evaluarán las 3 expresiones siguientes:                        ||")
print("||   1. (A ∧ B) ∨ (¬C)                                                 ||")
print("||   2. (A XOR B) ∧ C                                                  ||")
print("||   3. (A ∨ B) ∧ (¬A ∨ C)                                             ||")

while True:
    # Menú de opciones para el usuario
    print("\n" + "=" * 74)
    print("  Por favor elija lo que desea hacer:")
    print("  1. Ver tabla de verdad de una expresión")
    print("  2. Evaluar una expresión con valores concretos")
    print("  3. Salir del programa")
    print("=" * 74)
    
    opcion = input("\nIngrese el número de la opción (1, 2 o 3): ")

    # Definición de las funciones
    def AND(a, b):
        return a and b
    
    def OR(a, b):
        return a or b
    
    def NOT(a):
        return not a
    
    def XOR(a, b):
        return a != b
    
    # Mostrar tabla de verdad
    def mostrar_tabla(variables, expresion, nombre):
        print("\n" + "-" * 74)
        print(f"Expresión: {nombre}")
        print("-" * 74)
        
        print(" A | B | C | Resultado")
        print("-" * 74)
        
        # Generar todas las combinaciones
        n = len(variables)
        for i in range(2 ** n):
            # Crear los valores de las variables
            valores = {}
            for j, var in enumerate(variables):
                valores[var] = bool((i >> (n - 1 - j)) & 1)
            
            # Evaluar la expresión
            resultado = eval(expresion, {}, valores)
            
            # Mostrar la fila
            fila = ""
            for var in variables:
                fila += f" {int(valores[var])} |"
            print(fila + f" {int(resultado)}")
    
    # Función para evaluar una expresión con valores concretos
    def evaluar_expresion(expresion, variables, nombre):
        print("\n" + "-" * 74)
        print(f"Evaluando: {nombre}")
        print("-" * 74)
        
        # Pedir valores para cada variable
        valores = {}
        for var in variables:
            while True:
                try:
                    valor = int(input(f"Ingrese el valor de {var} (0 o 1): "))
                    if valor in [0, 1]:
                        valores[var] = bool(valor)
                        break
                    else:
                        print("Por favor ingrese 0 o 1.")
                except ValueError:
                    print("Por favor ingrese un número entero.")
        
        # Evaluar la expresión
        resultado = eval(expresion, {}, valores)
        
        print("\n" + "-" * 74)
        print(f"Resultado: {int(resultado)}")
        print("-" * 74)

    # Opción 1: Ver tabla de verdad de una expresión
    if opcion == "1":
        print("\n.*+° Tabla de Verdad °+*.")
        
        print("\nExpresiones disponibles:")
        print("1. (A ∧ B) ∨ (¬C)")
        print("2. (A XOR B) ∧ C")
        print("3. (A ∨ B) ∧ (¬A ∨ C)")
        
        subopcion = input("\nElija una expresión (1, 2 o 3): ")
        
        if subopcion == "1":
            expresion = "(A and B) or (not C)"
            variables = ["A", "B", "C"]
            nombre = "(A ∧ B) ∨ (¬C)"
            mostrar_tabla(variables, expresion, nombre)
        
        elif subopcion == "2":
            expresion = "(A != B) and C"
            variables = ["A", "B", "C"]
            nombre = "(A XOR B) ∧ C"
            mostrar_tabla(variables, expresion, nombre)
        
        elif subopcion == "3":
            expresion = "(A or B) and (not A or C)"
            variables = ["A", "B", "C"]
            nombre = "(A ∨ B) ∧ (¬A ∨ C)"
            mostrar_tabla(variables, expresion, nombre)
        
        else:
            print("\nOpción no válida.")

    # Opción 2: Evaluar una expresión con valores concretos
    elif opcion == "2":
        print("\n.*+° Evaluación de Expresión °+*.")
        
        print("\nExpresiones disponibles:")
        print("1. (A ∧ B) ∨ (¬C)")
        print("2. (A XOR B) ∧ C")
        print("3. (A ∨ B) ∧ (¬A ∨ C)")
        
        subopcion = input("\nElija una expresión (1, 2 o 3): ")
        
        if subopcion == "1":
            expresion = "(A and B) or (not C)"
            variables = ["A", "B", "C"]
            nombre = "(A ∧ B) ∨ (¬C)"
            evaluar_expresion(expresion, variables, nombre)
        
        elif subopcion == "2":
            expresion = "(A != B) and C"
            variables = ["A", "B", "C"]
            nombre = "(A XOR B) ∧ C"
            evaluar_expresion(expresion, variables, nombre)
        
        elif subopcion == "3":
            expresion = "(A or B) and (not A or C)"
            variables = ["A", "B", "C"]
            nombre = "(A ∨ B) ∧ (¬A ∨ C)"
            evaluar_expresion(expresion, variables, nombre)
        
        else:
            print("\nOpción no válida.")

    # Opción 3: Salir
    elif opcion == "3":
        print("\n¡Gracias por usar el programa!")
        break

    # Opción Inválida
    else:
        print("\nOpción no válida. Debe ser 1, 2 o 3.")