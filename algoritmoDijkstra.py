import heapq

def dijkstra(graph, start):
    # Inicialização das estruturas de dados
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph}
    unvisited = [(0, start)]  # Fila de prioridade para escolher o próximo vértice a visitar

    while unvisited:
        
        current_distance, current_vertex = heapq.heappop(unvisited) #Permite remover e retornar o menor elemento de um heap(fila)

        # Verifica se a distância atual é maior do que a armazenada (já foi visitado)
        if current_distance > distances[current_vertex]:
            continue

        # Exploração dos vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Atualiza a distância mínima se encontrar um caminho mais curto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(unvisited, (distance, neighbor))

    return distances, predecessors

# Grafo dado pelo professor
graph = {
    1: {6: 71, 2: 33},
    2: {1: 45, 7: 42, 3: 65},
    3: {2: 100, 8: 80, 4: 17},
    4: {3: 91, 5: 22},
    5: {4: 90, 10: 24},
    6: {1: 50, 11: 89, 7: 23},
    7: {2: 71, 6: 81, 8: 58},
    8: {3: 43, 7: 28},
    10: {5: 29, 15: 48},
    11: {6: 13, 16: 52},
    15: {10: 20, 20: 52},
    16: {11: 75, 21: 50},
    18: {23: 46, 19: 35},
    19: {18: 73, 24: 16, 20: 2},
    20: {15: 0, 19: 17, 25: 13},
    21: {16: 16, 22: 24},
    22: {21: 4, 23: 19},
    23: {18: 21, 22: 43, 24: 78},
    24: {19: 4, 23: 58, 25: 36},
    25: {20: 63, 24: 39}
}

start_vertex = 1
distances, predecessors = dijkstra(graph, start_vertex)

# Imprime as distâncias mínimas e os predecessores para cada vértice
for vertex in graph:
    print(f"Vértice {vertex}: distância mínima = {distances[vertex]}, predecessor = {predecessors[vertex]}")
