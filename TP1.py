""" import random

# Función a minimizar
def f(x, y):
    return 3 * x**2 * y**2

# Parámetros iniciales aleatorios entre 0 y 1
x = random.uniform(0, 1)
y = random.uniform(0, 1)

# Proceso iterativo
for i in range(1, 101):
    # Calcular el valor de la función en la posición actual
    funActual = f(x, y)
    
    # Calcular el gradiente de la función en la posición actual
    derivadaX = 6 * x * y**2
    derivadaY = 6 * x**2 * y
    
    # Actualizar las coordenadas en la dirección del gradiente
    x -= 0.05 * derivadaX
    y -= 0.05 * derivadaY
    
    # Imprimir los valores de la función en cada iteración
    print("Iteración:", i, "par(",x, " , ",y,"), Valor funcion f(x, y):", funActual)
    print()
"""
graph = {
    'A': {'A': 4.1, 'C': 3.1 },
    'B': {'D': 5.1},
    'C': {'B': 2.1, 'D': 3.2, 'E': 6.1},
    'E': {'D': 5},
} 

def dijkstra(graph, source):
    dist = {}  # Diccionario para almacenar las distancias mínimas desde el origen
    prev = {}  # Diccionario para almacenar los nodos previos en el camino más corto
    Q = []  # Lista para almacenar los nodos no visitados

    for v in graph.keys():
        dist[v] = float('inf')  # Inicializar todas las distancias como infinito
        prev[v] = None  # Inicializar todos los nodos previos como no definidos
        Q.append(v)  # Agregar todos los nodos a la lista Q

    dist[source] = 0  # La distancia desde el origen al origen es 0

    while Q:
        # Obtener el nodo con la distancia mínima en Q
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)  # Remover u de la lista Q

        for v in graph[u]:  # Iterar sobre los vecinos de u
            alt = dist[u] + graph[u][v]  # Calcular la nueva distancia tentativa desde el origen hasta v a través de u
            if alt < dist[v]:  # Si la nueva distancia es menor que la distancia actual
                dist[v] = alt  # Actualizar la distancia mínima
                prev[v] = u  # Actualizar el nodo previo en el camino más corto

    return dist, prev  # Devolver los diccionarios de distancias mínimas y nodos previos

def shortest_path(source, destination, prev):
    # Recorremos los predecesores para obtener el camino desde la fuente hasta el destino
    path = []
    while destination is not None:
        path.append(destination)
        destination = prev[destination]
    # Invertimos el camino obtenido, ya que se agregaron los nodos desde el destino hasta la fuente
    path.reverse()
    return path

# Luego de ejecutar la función dijkstra y obtener los diccionarios dist y prev
# Supongamos que "A" es el nodo fuente y "E" es el nodo final
source = "A"
destination = "E"
dijkstra(graph, 'A')
path = shortest_path('A', 'D', prev)
print("Camino más corto desde", source, "hasta", destination, ":", path)