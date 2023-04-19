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