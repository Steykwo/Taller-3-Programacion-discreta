#JSGV
import math

# Introduccion al programa
print("\n                                   Simulador cuantico basico                                            ")
print("\n|| Un qubit se representa como una combinacion α|0⟩ + β|1⟩, donde |α|^2 y |β|^2 son probabilidades.    ||")
print("|| Este simulador permite aplicar las compuertas cuanticas X, Z y H a un qubit, y luego simular          ||")
print("|| mediciones para observar las probabilidades de obtener 0 o 1.                                        ||")
print("\n" + "=" * 116)

# Se define la funcion para mostrar el estado del qubit
def mostrar_estado(estado, mensaje=""):
    """
    Muestra el estado actual del qubit en formato α|0⟩ + β|1⟩
    """
    if mensaje:
        print(f"\n{mensaje}")
    
    alpha, beta = estado
    print(f"Estado: ({alpha:.4f})|0⟩ + ({beta:.4f})|1⟩")
    
    # Calcular probabilidades
    prob_0 = abs(alpha) ** 2
    prob_1 = abs(beta) ** 2
    print(f"Probabilidad de medir 0: {prob_0:.4f} ({prob_0*100:.2f}%)")
    print(f"Probabilidad de medir 1: {prob_1:.4f} ({prob_1*100:.2f}%)")

# Se define la funcion para aplicar compuerta X (NOT cuantica)
def compuerta_X(estado):
    """
    Aplica la compuerta X al estado del qubit.
    X = [[0, 1], [1, 0]]
    X|0⟩ = |1⟩, X|1⟩ = |0⟩
    """
    alpha, beta = estado
    # X * [alpha, beta]^T = [beta, alpha]^T
    return (beta, alpha)

# Se define la funcion para aplicar compuerta Z (fase)
def compuerta_Z(estado):
    """
    Aplica la compuerta Z al estado del qubit.
    Z = [[1, 0], [0, -1]]
    Z|0⟩ = |0⟩, Z|1⟩ = -|1⟩
    """
    alpha, beta = estado
    # Z * [alpha, beta]^T = [alpha, -beta]^T
    return (alpha, -beta)

# Se define la funcion para aplicar compuerta H (Hadamard)
def compuerta_H(estado):
    """
    Aplica la compuerta H (Hadamard) al estado del qubit.
    H = 1/√2 * [[1, 1], [1, -1]]
    H|0⟩ = (|0⟩ + |1⟩)/√2, H|1⟩ = (|0⟩ - |1⟩)/√2
    """
    import math
    alpha, beta = estado
    # H * [alpha, beta]^T = 1/√2 * [alpha + beta, alpha - beta]^T
    factor = 1 / math.sqrt(2)
    nuevo_alpha = factor * (alpha + beta)
    nuevo_beta = factor * (alpha - beta)
    return (nuevo_alpha, nuevo_beta)

# Se define la funcion para simular mediciones
def simular_mediciones(estado, num_mediciones=1000):
    """
    Simula num_mediciones mediciones del qubit y retorna las frecuencias observadas.
    """
    import random
    
    alpha, beta = estado
    prob_0 = abs(alpha) ** 2
    prob_1 = abs(beta) ** 2
    
    # Normalizar las probabilidades por si hay errores numericos
    total = prob_0 + prob_1
    if total > 0:
        prob_0 = prob_0 / total
        prob_1 = prob_1 / total
    
    # Simular mediciones
    conteo_0 = 0
    conteo_1 = 0
    
    for _ in range(num_mediciones):
        if random.random() < prob_0:
            conteo_0 += 1
        else:
            conteo_1 += 1
    
    return conteo_0, conteo_1

# Se define la funcion para mostrar resultados de mediciones
def mostrar_mediciones(conteo_0, conteo_1, num_mediciones):
    """
    Muestra los resultados de las mediciones simuladas.
    """
    print(f"\nResultados de {num_mediciones} mediciones simuladas:")
    print(f"Mediciones con resultado 0: {conteo_0} ({conteo_0/num_mediciones*100:.2f}%)")
    print(f"Mediciones con resultado 1: {conteo_1} ({conteo_1/num_mediciones*100:.2f}%)")

# Funcion principal para ejecutar el simulador
def ejecutar_simulador():
    """
    Funcion principal que ejecuta el simulador cuantico basico.
    """
    print("\n" + "=" * 116)
    print("\nSIMULADOR CUANTICO BASICO")
    print("=" * 116)
    
    # Solicitar el estado inicial del qubit
    print("\nIngrese el estado inicial del qubit:")
    print("El estado se representa como α|0⟩ + β|1⟩, donde |α|^2 + |β|^2 = 1")
    
    try:
        # Solicitar la parte real de alpha
        alpha_real = float(input("Ingrese la parte real de α (coeficiente de |0⟩): "))
        alpha_imag = float(input("Ingrese la parte imaginaria de α (coeficiente de |0⟩): "))
        alpha = complex(alpha_real, alpha_imag)
        
        # Solicitar la parte real de beta
        beta_real = float(input("Ingrese la parte real de β (coeficiente de |1⟩): "))
        beta_imag = float(input("Ingrese la parte imaginaria de β (coeficiente de |1⟩): "))
        beta = complex(beta_real, beta_imag)
        
        estado = (alpha, beta)
        
        # Verificar que el estado este normalizado
        norma = abs(alpha) ** 2 + abs(beta) ** 2
        if abs(norma - 1.0) > 0.01:
            print(f"\nAdvertencia: El estado no esta normalizado (|α|^2 + |β|^2 = {norma:.4f})")
            print("Se normalizara automaticamente.")
            # Normalizar el estado
            factor = 1 / math.sqrt(norma)
            estado = (alpha * factor, beta * factor)
        
        # Mostrar el estado inicial
        mostrar_estado(estado, "Estado inicial del qubit:")
        
        # Menu de compuertas
        continuar = True
        while continuar:
            print("\n" + "-" * 50)
            print("Compuertas disponibles:")
            print("1. X (NOT cuantica)")
            print("2. Z (Fase)")
            print("3. H (Hadamard)")
            print("4. Mostrar estado actual")
            print("5. Simular mediciones")
            print("6. Salir y terminar programa")
            
            opcion = input("\nSeleccione una opcion (1-6): ")
            
            if opcion == "1":
                estado = compuerta_X(estado)
                mostrar_estado(estado, "Despues de aplicar compuerta X:")
                
            elif opcion == "2":
                estado = compuerta_Z(estado)
                mostrar_estado(estado, "Despues de aplicar compuerta Z:")
                
            elif opcion == "3":
                estado = compuerta_H(estado)
                mostrar_estado(estado, "Despues de aplicar compuerta H:")
                
            elif opcion == "4":
                mostrar_estado(estado, "Estado actual del qubit:")
                
            elif opcion == "5":
                # Solicitar numero de mediciones
                num_med = input("Ingrese el numero de mediciones a simular (default 1000): ")
                if num_med.strip() == "":
                    num_med = 1000
                else:
                    num_med = int(num_med)
                
                conteo_0, conteo_1 = simular_mediciones(estado, num_med)
                mostrar_mediciones(conteo_0, conteo_1, num_med)
                
            elif opcion == "6":
                continuar = False
                print("\nSaliendo del simulador...")
                
            else:
                print("Opcion no valida. Intente de nuevo.")
    
    except ValueError:
        print("Error: Ingrese valores numericos validos.")
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")

# Ejecutar el simulador
ejecutar_simulador()

print("\n" + "=" * 116)
print("FIN DEL PROGRAMA")
print("=" * 116)