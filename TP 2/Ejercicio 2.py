#ejercicio 1
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
#Ejercicio 2
"""
def dijkstra(Grafo, salida, final):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    nodos = [vertice for vertice in Grafo]
    
    while nodos:
        print(nodos)
        nodoVisitado = min(nodos, key=dist.get)
        nodos.remove(nodoVisitado)
        result.append(nodoVisitado)

        for vecino in Grafo[nodoVisitado]:
            if vecino in nodos and dist[vecino] > dist[nodoVisitado] + Grafo[nodoVisitado][vecino]:
                dist[vecino] = dist[nodoVisitado] + Grafo[nodoVisitado][vecino]
                prev[vecino] = nodoVisitado

    return result, dist[final], prev


grafo = {
    'A': {'A': 4.1, 'C': 3.1 },
    'B': {'D': 5.1},
    'C': {'B': 2.1, 'D': 3.2},
    'D': {},
}

s, distancia, previos = dijkstra(grafo, 'A', 'D')
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")
"""
#ejercicio 3
import numpy as np
import time
import matplotlib.pyplot as plt

def calcular_valor_en_anillo(k):
    valor_en_anillo = k % 3
    return valor_en_anillo

# Prueba del código con n = 73 y k = 3
n = 73
k = 3
resultado = calcular_valor_en_anillo(k, n)
print("Resultado para n = 73 y k = 3:", resultado)

# Creación de un array aleatorio de 10,000 elementos
tamano_array = 10000
array_aleatorio = np.random.randint(1, 1000, size=tamano_array)

# Medición del tiempo acumulado en cada iteración
tiempo_acumulado = []
tiempo_total = 0
for i in range(tamano_array):
    tiempo_inicio = time.time()
    calcular_valor_en_anillo(k, n)
    tiempo_fin = time.time()
    tiempo_total += (tiempo_fin - tiempo_inicio)
    tiempo_acumulado.append(tiempo_total)

# Graficación del tiempo acumulado en cada iteración
x = np.arange(tamano_array)
y = np.array(tiempo_acumulado)
plt.plot(x, y)
plt.xlabel('n de iteración')
plt.ylabel('Tiempo acumulado')
plt.title('Costo de Computación en función de n')
plt.grid(True)
plt.show()

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
    nodos = []  # Lista para almacenar los nodos no visitados

    for v in graph.keys():
        dist[v] = float('inf')  # Inicializar todas las distancias como infinito
        prev[v] = None  # Inicializar todos los nodos previos como no definidos
        nodos.append(v)  # Agregar todos los nodos a la lista nodos

    dist[source] = 0  # La distancia desde el origen al origen es 0

    while nodos:
        # Obtener el nodo con la distancia mínima en nodos
        nodoVisitado = min(nodos, key=lambda x: dist[x])
        nodos.remove(nodoVisitado)  # Remover nodoVisitado de la lista nodos

        for v in graph[nodoVisitado]:  # Iterar sobre los vecinos de nodoVisitado
            alt = dist[nodoVisitado] + graph[nodoVisitado][v]  # Calcular la nueva distancia tentativa desde el origen hasta v a través de nodoVisitado
            if alt < dist[v]:  # Si la nueva distancia es menor Nodosue la distancia actual
                dist[v] = alt  # Actualizar la distancia mínima
                prev[v] = nodoVisitado  # Actualizar el nodo previo en el camino más corto

    return dist, prev  # Devolver los diccionarios de distancias mínimas y nodos previos

def shortest_path(source, destination, prev):
    # Recorremos los predecesores para obtener el camino desde la fuente hasta el destino
    path = []
    while destination is not None:
        path.append(destination)
        destination = prev[destination]
    # Invertimos el camino obtenido, ya Nodosue se agregaron los nodos desde el destino hasta la fuente
    path.reverse()
    return path

# Luego de ejecutar la función dijkstra y obtener los diccionarios dist y prev
# Supongamos Nodosue "A" es el nodo fuente y "E" es el nodo final
source = "A"
destination = "E"
dijkstra(graph, 'A')
path = shortest_path('A', 'D', prev)
print("Camino más corto desde", source, "hasta", destination, ":", path)

"""