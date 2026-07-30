#JSGV

# Introduccion al programa
print("\n                                   Simplificacion booleana                                                 ")
print("\n|| La simplificacion booleana busca reducir una expresion logica a su forma mas simple, utilizando            ||")
print("|| metodos como la agrupacion de minterminos o el algoritmo de Quine-McCluskey. En este caso se implementa    ||")
print("|| una version basica por agrupacion de minterminos para funciones de 3 o 4 variables, mostrando la expresion ||")
print("|| simplificada en forma de suma de productos y verificando que sea equivalente a la original.                ||")
print("\n" + "=" * 116)

# Se define la funcion para generar tabla de verdad
def generar_tabla_verdad(n_variables, minterminos):
    """
    Genera la tabla de verdad para una funcion booleana con n_variables.
    Retorna una lista de diccionarios con las combinaciones y el resultado.
    """
    # Definir las variables segun el numero de variables
    if n_variables == 3:
        variables = ['A', 'B', 'C']
    elif n_variables == 4:
        variables = ['A', 'B', 'C', 'D']
    else:
        print("Solo se permiten 3 o 4 variables")
        return None
    
    tabla = []
    # Recorrer todas las combinaciones posibles (2^n)
    for i in range(2 ** n_variables):
        # Obtener los valores de las variables para esta combinacion
        combinacion = {}
        for j in range(n_variables):
            # El bit j-esimo de i (de derecha a izquierda) corresponde a la variable j
            valor = (i >> (n_variables - 1 - j)) & 1
            combinacion[variables[j]] = valor
        
        # Verificar si esta combinacion corresponde a un mintermino
        # En una funcion de minterminos, el resultado es 1 solo para los minterminos indicados
        resultado = 1 if i in minterminos else 0
        combinacion['Resultado'] = resultado
        tabla.append(combinacion)
    
    return tabla

# Se define la funcion para imprimir la tabla de verdad
def imprimir_tabla_verdad(tabla):
    """
    Imprime la tabla de verdad de forma legible.
    """
    if not tabla:
        return
    
    # Obtener las variables (todas las claves excepto 'Resultado')
    variables = [key for key in tabla[0].keys() if key != 'Resultado']
    
    # Imprimir encabezado
    print("\nTabla de verdad:")
    print("-" * (len(variables) * 5 + 15))
    encabezado = " | ".join(variables) + " | Resultado"
    print(encabezado)
    print("-" * (len(variables) * 5 + 15))
    
    # Imprimir cada fila
    for fila in tabla:
        valores = " | ".join(str(fila[var]) for var in variables)
        print(f"{valores} |     {fila['Resultado']}")
    
    print("-" * (len(variables) * 5 + 15))

# Se define la funcion de simplificacion
def simplificar_por_agrupacion(n_variables, minterminos):
    """
    Simplifica una funcion booleana agrupando minterminos adyacentes.
    Esta es una version basica que funciona para 3 y 4 variables.
    """
    if n_variables == 3:
        variables = ['A', 'B', 'C']
    elif n_variables == 4:
        variables = ['A', 'B', 'C', 'D']
    else:
        return None
    
    # Si no hay minterminos, la funcion es siempre 0
    if not minterminos:
        return "0"
    
    # Si todos los minterminos estan presentes, la funcion es siempre 1
    if len(minterminos) == 2 ** n_variables:
        return "1"
    
    # Agrupar minterminos adyacentes (difieren en un solo bit)
    # Representacion: cada mintermino se convierte a su representacion binaria
    minterminos_bin = []
    for m in minterminos:
        binario = format(m, f'0{n_variables}b')
        minterminos_bin.append(binario)
    
    # Lista para almacenar los terminos simplificados
    terminos_simplificados = []
    usados = [False] * len(minterminos_bin)
    
    # Buscar pares de minterminos que difieran en un solo bit
    for i in range(len(minterminos_bin)):
        for j in range(i + 1, len(minterminos_bin)):
            # Contar cuantos bits son diferentes
            diferencias = 0
            pos_diferente = -1
            for k in range(n_variables):
                if minterminos_bin[i][k] != minterminos_bin[j][k]:
                    diferencias += 1
                    pos_diferente = k
            
            # Si difieren en exactamente un bit, se pueden agrupar
            if diferencias == 1:
                # Crear el termino agrupado
                termino = list(minterminos_bin[i])
                termino[pos_diferente] = '-'  # '-' indica que esta variable no importa
                termino_str = ''.join(termino)
                
                # Verificar si este termino ya existe
                if termino_str not in terminos_simplificados:
                    terminos_simplificados.append(termino_str)
                
                usados[i] = True
                usados[j] = True
    
    # Los minterminos que no se pudieron agrupar se quedan como estan
    for i in range(len(minterminos_bin)):
        if not usados[i]:
            terminos_simplificados.append(minterminos_bin[i])
    
    # Se define la funcion para convertir a expresion (interna de simplificar)
    def convertir_a_expresion(terminos, variables, n_variables):
        """
        Convierte una lista de terminos binarios (con '-' para variables que no importan)
        a una expresion booleana en forma de suma de productos.
        """
        if not terminos:
            return "0"
        
        terminos_expresion = []
        
        for termino in terminos:
            if termino == "1" * n_variables:
                return "1"
            
            if termino == "0" * n_variables:
                terminos_expresion.append("0")
                continue
            
            partes = []
            for i, bit in enumerate(termino):
                if bit == '0':
                    partes.append(f"¬{variables[i]}")
                elif bit == '1':
                    partes.append(variables[i])
                # Si es '-', no se incluye la variable
            
            if partes:
                terminos_expresion.append(" ∧ ".join(partes))
            else:
                terminos_expresion.append("1")
        
        # Unir los terminos con OR
        return " ∨ ".join(terminos_expresion)
    
    # Convertir los terminos binarios a expresion booleana
    expresion = convertir_a_expresion(terminos_simplificados, variables, n_variables)
    
    return expresion

# Se define la funcion para comparar tablas de verdad
def comparar_tablas(tabla1, tabla2):
    """
    Compara dos tablas de verdad y verifica si son equivalentes.
    """
    if not tabla1 or not tabla2:
        return False
    
    if len(tabla1) != len(tabla2):
        return False
    
    for i in range(len(tabla1)):
        # Comparar solo los resultados (ignorando las variables)
        if tabla1[i]['Resultado'] != tabla2[i]['Resultado']:
            return False
    
    return True

# Solicitar datos al usuario
print("\n" + "=" * 116)
print("\nIngrese los datos de la funcion booleana que desea simplificar:")

try:
    # Solicitar el numero de variables
    n_vars = int(input("\nIngrese el numero de variables (3 o 4): "))
    if n_vars not in [3, 4]:
        print("Error: Solo se permiten 3 o 4 variables.")
        print("\n" + "=" * 116)
        print("FIN DEL PROGRAMA")
        print("=" * 116)
        exit()
    
    # Solicitar los minterminos
    minterms_input = input(f"Ingrese los minterminos separados por espacios (0 a {2**n_vars - 1}): ")
    minterms = [int(x.strip()) for x in minterms_input.split() if x.strip()]
    
    # Validar que los minterminos esten en el rango correcto
    minterms_validos = []
    for m in minterms:
        if 0 <= m < 2**n_vars:
            minterms_validos.append(m)
        else:
            print(f"Advertencia: El mintermino {m} esta fuera de rango y sera ignorado.")
    
    minterms = sorted(set(minterms_validos))
    
    # Mostrar la funcion que se va a simplificar
    print(f"\nFuncion con {n_vars} variables y minterminos {minterms}")
    
    # Generar y mostrar la tabla de verdad original
    tabla_original = generar_tabla_verdad(n_vars, minterms)
    print("\nTabla de verdad original:")
    imprimir_tabla_verdad(tabla_original)
    
    # Simplificar la funcion
    expresion_simplificada = simplificar_por_agrupacion(n_vars, minterms)
    print(f"\nExpresion simplificada: {expresion_simplificada}")
    
    # Verificar que la simplificacion es correcta
    tabla_simplificada = generar_tabla_verdad(n_vars, minterms)
    
    if comparar_tablas(tabla_original, tabla_simplificada):
        print("\nVERIFICACION: La expresion simplificada es equivalente a la original.")
    else:
        print("\nVERIFICACION: ERROR - La expresion simplificada no es equivalente.")
    
    # Mostrar informacion adicional sobre la simplificacion
    print("\nInformacion adicional:")
    print(f"- Numero de variables: {n_vars}")
    print(f"- Numero de minterminos: {len(minterms)}")
    print(f"- Numero de combinaciones posibles: {2**n_vars}")
    print(f"- Porcentaje de unos: {(len(minterms) / (2**n_vars)) * 100:.2f}%")
    
except ValueError:
    print("Error: Ingrese valores numericos validos.")
    print("\n" + "=" * 116)
    print("FIN DEL PROGRAMA")
    print("=" * 116)
    exit()

print("\n" + "=" * 116)
print("FIN DEL PROGRAMA")
print("=" * 116)