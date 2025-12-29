import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def visualize_graph(graph, shortest_paths, start_node):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=7)
    node_colors = ['skyblue' if node != start_node else 'lightgreen' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    dist_labels = {node: f"{node}:{dist:.0f}" if dist != float('infinity') else f"{node}:inf" for node, dist in shortest_paths.items()}
    nx.draw_networkx_labels(G, pos, labels=dist_labels, font_size=10, font_family='sans-serif')

    plt.axis('off')
    plt.title(f"Граф та найкоротші шляхи від вузла '{start_node}'\n")
    plt.show()

# Приклад використання:
def visualize_shortest_paths():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3}
    }
    start_node = 'A'

    shortest_paths = dijkstra(graph, start_node)

    print(f"Найкоротші шляхи від початкової вершини '{start_node}':")
    for node, distance in shortest_paths.items():
        print(f"До вершини {node}: {distance}")

    visualize_graph(graph, shortest_paths, start_node)

if __name__ == '__main__':
    visualize_shortest_paths()
