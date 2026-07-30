#JSGV

#Introduccion al programa
print("\n                                   Algoritmo de dijkstra                                               ")
print("\n|| En el algoritmo de dijkstra de busca encontrar la ruta mas corta o que cueste menos de un vertice hacia otro   ||")
print("|| en un grafo, por lo que se debe entrgar primero un grafo, el vertice de inicio y el vertice de final para que  ||")
print("|| el algoritmo pueda realizar su trabajo, en este caso, se tendrá un grafo base, y luego se ingresará el vertice ||")
print("|| de entrada y de salida que el usuario elija para que el algoritmo calcule la ruta mas corta y la muestre       ||")
print("\n" + "=" * 116)
print("\n|| En este caso se tomarán 5 pares de vertices a analizar, dando el antes y el despues de sus pesos para ir de    ||")
print("|| uno al otro al cortar la conexión de un vertice en específico, mostrando el cómo la desconexión de ese vertice ||")
print("|| crea ruido en los vertices de alrededor, volviendo unas rutas mas largas y otras imposibles                    ||")
print("\n" + "=" * 116)

#Declaracion del grafo (es el mismo grafo utilizado en el punto 5 de
#este mismo taller, al igual que el correspondiente al algoritmo de Dajkstra)

grafo_inicial = {
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
pares = [
    ("Portal","Hospital"),
    ("Portal","Estadio"),
    ("Calle26","Universidad"),
    ("Museo","Terminal"),
    ("Parque","Centro")
]

#Función encargada de imprimir el grafo de prueba
def imprimir_grafo(grafo):
    print("\nEste es el grafo que se usara para el algoritmo de Dijkstra:\n")

    for vertice in grafo:
        print(vertice, end=" -> ")

        for vecino, peso in grafo[vertice]:
            print(f"{vecino}({peso})", end=", ")
        print()

imprimir_grafo(grafo_inicial)

#Codigo del algoritmo de Dijkstra utilizado en el punto 5 de este mismo taller
#Al ya haberlo explicado en ese punto simplemente se saltará la explicación de su funcionamiento y se utilizará como función

def dijkstra(grafo, inicio, destino):

    #Verificar que los vértices existan
    if inicio not in grafo:
        print(f"\nError: el vértice '{inicio}' no existe en el grafo")
        return None, None

    if destino not in grafo:
        print(f"\nError: el vértice '{destino}' no existe en el grafo")
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

#Funcion que elimina un vertice y las aristas que llegan hasta el
def eliminar_vertice(grafo, vertice_a_eliminar):

    # Verificar que el vertice exista
    if vertice_a_eliminar not in grafo:
        print(f"El vértice '{vertice_a_eliminar}' no existe.")
        return

    # Si existe de elimina el vertice
    del grafo[vertice_a_eliminar]

    #Eliminar todas las aristas que apuntan al vértice eliminado
    for vertice in grafo:
        nueva_lista = []
        for vecino, peso in grafo[vertice]:
            if vecino != vertice_a_eliminar:
                nueva_lista.append((vecino, peso))
        grafo[vertice] = nueva_lista

    
    print(f"Se eliminó el vértice '{vertice_a_eliminar}' junto con todas sus conexiones.")

# Muestro los pares de vertices en los que se basara el programa
print("\nEl algoritmo de Dajkstra se ejecutará en los siguientes pares de vertices:\n")
for origen, destino in pares:
    print(f"{origen} -> {destino}")

#Separación decorativa
print("\n" + "=" * 116)

#Inicio del calculo para almacenar las variables con al algoritmo de Dajkstra

#Creo un diccionario donde guardo la distancia antes de borrar el vertice
antes = {}
for origen, destino in pares:
    ruta, distancia = dijkstra(grafo_inicial, origen, destino)
    antes[(origen,destino)] = distancia

#Se elimina un vertice
vertice_a_eliminar = input("Ingrese el nombre del vertice que desea eliminar, que haga parte del grafo dado: ")
if vertice_a_eliminar not in grafo_inicial:
    print(f"\nError: el vértice '{vertice_a_eliminar}' no existe en el grafo")
else:
    eliminar_vertice(grafo_inicial, vertice_a_eliminar)

#Creo un diccionario donde guardo la distancia despues de borrar el vertice Hospital
despues = {}
for origen, destino in pares:
    ruta, distancia = dijkstra(grafo_inicial, origen, destino)
    despues[(origen, destino)] = distancia

#Muestro los resultados en formato de tabla
print("\nAplicando el algoritmo de Dijkstra para calcular la menor distancia de dos vertices antes y despues")
print("de eliminar un vertice (en este caso el vertice Hospital) se obtiene los siguientes resultados\n")

#Titulo de la tabla
print("{:<15}{:<15}{:<12}{}".format(
    "Origen",
    "Destino",
    "Antes",
    "Después"
))

print("-" * 55)

#Impresión de todos los valores de los pares de vertices
for origen, destino in pares:

    distancia_antes = antes[(origen, destino)]
    distancia_despues = despues[(origen, destino)]

    if distancia_despues is None:
        distancia_despues = "No existe"

    print("{:<15}{:<15}{:<12}{}".format(
        origen,
        destino,
        str(distancia_antes),
        str(distancia_despues)
    ))

