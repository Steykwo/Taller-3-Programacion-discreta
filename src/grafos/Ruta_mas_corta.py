#JSGV

#Introduccion al programa
print("\n                                   Algoritmo de dijkstra                                               ")
print("\n|| En el algoritmo de dijkstra de busca encontrar la ruta mas corta o que cueste menos de un vertice hacia otro   ||")
print("|| en un grafo, por lo que se debe entrgar primero un grafo, el vertice de inicio y el vertice de final para que  ||")
print("|| el algoritmo pueda realizar su trabajo, en este caso, se tendrá un grafo base, y luego se ingresará el vertice ||")
print("|| de entrada y de salida que el usuario elija para que el algoritmo calcule la ruta mas corta y la muestre       ||")
print("\n" + "=" * 116 + "\n")

# Grafo de prueba hecho con diccionarios, de la forma:
# "Vertice": [("Vertice vecino",peso), ("Vertice vecino",peso), ...],

grafo = {
    "Portal": [("Calle26", 4), ("Terminal", 3)],
    "Calle26": [("Portal", 4), ("Museo", 5), ("Centro", 7)],
    "Terminal": [("Portal", 3), ("Universidad", 6)],
    "Museo": [("Calle26", 5), ("Centro", 2), ("Parque", 6)],
    "Centro": [("Calle26", 7), ("Museo", 2), ("Hospital", 4)],
    "Universidad": [("Terminal", 6), ("Hospital", 3)],
    "Parque": [("Museo", 6), ("Estadio", 5)],
    "Hospital": [("Centro", 4), ("Universidad", 3), ("Estadio", 2)],
    "Estadio": [("Parque", 5), ("Hospital", 2)]
}

#Función encargada de imprimir el grafo de prueba

def imprimir_grafo(grafo):
    print("\nEste es el grafo que se usara para el algoritmo de Dijkstra:\n")

    for vertice in grafo:
        print(vertice, end=" -> ")

        for vecino, peso in grafo[vertice]:
            print(f"{vecino}({peso})", end=", ")
        print()

imprimir_grafo(grafo)

#Funcion encargada de realizar el algoritmo de Dijkstra, con parametros de:
#El grafo a ingresar, el vertice de inicio y el vertice destino para calcular la ruta mas corta

def dijkstra(grafo, inicio, destino):

    #Verificar que los vértices existan
    if inicio not in grafo:
        print(f"\nError: el vértice '{inicio}' no existe en el grafo, vuelva a intentarlo con un nombre válido")
        return None, None

    if destino not in grafo:
        print(f"\nError: el vértice '{destino}' no existe en el grafo, vuelva a intentarlo con un nombre válido")
        return None, None

    #Inicializar distancias
    distancias = {}

    for vertice in grafo:
        distancias[vertice] = float("inf") #Se pone en infinito para que siempre calcula que la distancia es mayor

    distancias[inicio] = 0 #Excepto en el de inicio, ya que para diferenciarlo e iniciar desde ahi se le pone distancia 0

    #Diccionario para reconstruir la ruta, guarda como valor el vertice de donde viene y como clave el vertice actual
    anterior = {}

    #Lista de vértices no visitados, se van eliminando los vertices ya visitados, asegura que se revisen todos los vertices
    no_visitados = []

    for vertice in grafo:
        no_visitados.append(vertice)

    #Base para el algoritmo de Dijkstra
    while len(no_visitados) > 0:

        #Tomo un vertice cualquiera de los no visitados, por ejemplo el primero
        actual = no_visitados[0]

        #Busca el vertine con menor distancia y lo guarda en "actual"
        #Si el programa apenas empieza entonces elige el vertice de inicio seleccionado
        for vertice in no_visitados:
            if distancias[vertice] < distancias[actual]:
                actual = vertice

        #Si no hay más vértices alcanzables, terminar
        if distancias[actual] == float("inf"):
            break

        #Marcar como visitado
        no_visitados.remove(actual)

        #Revisar vecinos, encuentra su peso, los suma y encuentra el menor para ir a ese vertice
        for vecino, peso in grafo[actual]:

            nueva_distancia = distancias[actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anterior[vecino] = actual #Aqui guardo el vertice anterior, parandome en el del vecino

    #Si no existe un camino del inicio hasta el destino
    if distancias[destino] == float("inf"):
        print("No existe un camino entre los dos vértices.")
        return None, None

    #Reconstruir la ruta
    ruta = []

    actual = destino

    while actual != inicio:
        ruta.append(actual)
        actual = anterior[actual]

    ruta.append(inicio)
    ruta.reverse() #Se agregan los valores de los vertices obtenidos al calcular los pesos, gracias a que este guardaba el vertice anterior siempre

    return ruta, distancias[destino]

#Se piden los valores de los vertices de inicio y del destino para implementar el algoritmo sobre el grafo dado
print("\nPor favor, teniendo en cuenta el grafo mostrado, ingrese el nombre del vertice de inicio y de destino a continuacion:")
inicio = input("Vertice de inicio: ")
destino = input("Vertice de destino: ")

ruta, peso = dijkstra(grafo, inicio, destino)

if ruta is not None:

    print("\nSegún los datos obtenidos y la implementación del algoritmo de Dijkstra se tiene que la ruta mas corta, junto con su peso designado es:\n")

    print("Ruta:", " -> ".join(ruta))
    print("Distancia total:", peso)