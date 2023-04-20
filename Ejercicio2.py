def dijkstra(Grafo, salida, final):
    dist, prev = {}, {}

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    nodos = [vertice for vertice in Grafo]
    
    while nodos: 
        
        nodoVisitado = min(nodos, key=dist.get)
        nodos.remove(nodoVisitado)

        for vecino in Grafo[nodoVisitado]:
            if vecino in nodos and dist[vecino] > dist[nodoVisitado] + Grafo[nodoVisitado][vecino]:
                dist[vecino] = dist[nodoVisitado] + Grafo[nodoVisitado][vecino]
                prev[vecino] = nodoVisitado

    return dist[final], prev


grafo = {
    'A': {'A': 4.1, 'C': 3.1 },
    'B': {'D': 5.1},
    'C': {'B': 2.1, 'D': 3.2},
    'D': {},
}

distancia, previos = dijkstra(grafo, 'A', 'D')
print(f"{distancia=}")
print(f"{previos=}")