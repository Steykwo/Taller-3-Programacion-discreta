#JSGV

#Introduccion al programa
print("\n                                          Coloreo de grafos                                                         ")
print("\n|| El coloreo de grafos se basa en que cada vertice de un grafo tenga un color, pero que a su vez los vertices  ||")
print("|| vecinos no tengan el mismo color, de forma que al aplicarlo a un caso real, como en el caso de este ejercicio, ||")
print("|| la conexión entre los vertices que representan las asignaturas se refiere a que estas tienen estudiantes en    ||")
print("|| comun, por lo que no pueden tener el mismo horario para examenes, y este horario se verá representado con los  ||")
print("|| colores, cada color representando una distinta franja horaria                                                  ||")
print("\n" + "=" * 116)

#Grafo de prueba hecho con diccionarios, de la forma:
# "Vertice": ["Vertice vecino", "Vertice vecino", ...]

grafo = {
    "Matematicas": ["Fisica", "Programacion", "Algebra", "Quimica"],
    "Fisica": ["Matematicas", "Programacion", "BasesDatos"],
    "Programacion": ["Matematicas", "Fisica", "Redes"],
    "Algebra": ["Matematicas", "Estadistica", "Electronica"],
    "Quimica": ["Matematicas", "Biologia", "BasesDatos"],
    "BasesDatos": ["Fisica", "Quimica", "Redes"],
    "Redes": ["Programacion", "BasesDatos", "Electronica"],
    "Biologia": ["Quimica", "Estadistica"],
    "Electronica": ["Algebra", "Redes", "Estadistica"],
    "Estadistica": ["Algebra", "Biologia", "Electronica"]
}

#Función encargada de imprimir el grafo de prueba
def imprimir_grafo(grafo):
    print("\nEste es el grafo que se usara para el coloreo de grafos:\n")

    for vertice in grafo:
        print(vertice, end=" -> ")

        for vecino in grafo[vertice]:
            print(f"{vecino}", end=", ")
        print()

imprimir_grafo(grafo)

#Algoritmo voraz usado para el coloreo de los vertices

#Diccionario donde se guardará el color de cada vértice como valor
colores = {}

for vertice in grafo:

    # Colores usados por los vecinos
    colores_vecinos = set() # Se usa una tupla para que no existan valores repetidos

    # Busca los colores que ya tienen los vecinos y los almacena en la tupla
    for vecino in grafo[vertice]:
        if vecino in colores:
            colores_vecinos.add(colores[vecino])

    # Buscar el primer color disponible (que no este ocupado por los vecinos) y lo añade al vertice
    color = 1
    while color in colores_vecinos:
        color += 1

    colores[vertice] = color


#Muestro los colores que obtuvo cada materia (vertice)
print("Color asignado a cada materia\n")
for materia, color in colores.items():
    print(f"{materia:15} -> Color {color}")


#Cantidad de colores usados en el grafo
cantidad_colores = len(set(colores.values()))
print(f"\nCantidad de colores utilizados: {cantidad_colores}")


#Muestro todos los colores que se usaron
print("\nMaterias en cada color:\n")
for color in range(1, cantidad_colores + 1):
    print(f"Color {color}:")
    for materia in colores:
        if colores[materia] == color:
            print(" -", materia)
    print()