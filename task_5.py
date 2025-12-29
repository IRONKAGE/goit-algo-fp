import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import multiprocessing
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_with_colors(tree_root, node_colors_map, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node_colors_map.get(node_id, 'skyblue') for node_id in tree.nodes]
    labels = {node_id: tree.nodes[node_id]['label'] for node_id in tree.nodes}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def get_color_gradient(start_hex, end_hex, steps):
    if steps <= 1: return [start_hex]

    def hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return f'#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}'

    s_rgb = hex_to_rgb(start_hex)
    e_rgb = hex_to_rgb(end_hex)

    colors = []
    for i in range(steps):
        factor = i / (steps - 1)
        curr_rgb = tuple(s_rgb[j] + factor * (e_rgb[j] - s_rgb[j]) for j in range(3))
        colors.append(rgb_to_hex(curr_rgb))
    return colors

def list_to_tree(heap_list, index=0):
    if index < len(heap_list):
        node = Node(heap_list[index])
        node.left = list_to_tree(heap_list, 2 * index + 1)
        node.right = list_to_tree(heap_list, 2 * index + 2)
        return node
    return None

def run_dfs(root):
    visited_order_ids = []
    stack = [root]
    visited_ids = set()

    while stack:
        current = stack.pop()
        if current.id not in visited_ids:
            visited_ids.add(current.id)
            visited_order_ids.append(current.id)
            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)

    colors = get_color_gradient('#00008B', '#ADD8E6', len(visited_order_ids))
    node_colors_map = {n_id: color for n_id, color in zip(visited_order_ids, colors)}
    draw_tree_with_colors(root, node_colors_map, "Обхід у глибину (DFS) ☯︎ Синій градієнт\n")

def run_bfs(root):
    visited_order_ids = []
    queue = deque([root])
    visited_ids = {root.id}

    while queue:
        current = queue.popleft()
        visited_order_ids.append(current.id)
        for child in [current.left, current.right]:
            if child and child.id not in visited_ids:
                visited_ids.add(child.id)
                queue.append(child)

    colors = get_color_gradient('#8B0000', '#FFB6C1', len(visited_order_ids))
    node_colors_map = {n_id: color for n_id, color in zip(visited_order_ids, colors)}
    draw_tree_with_colors(root, node_colors_map, "Обхід у ширину (BFS) ☯︎ Червоний градієнт\n")

# Приклад використання:
def benchmark():
    data = [0, 4, 5, 10, 1, 3, 2, 8, 7, 9, 6, 100, 50, 25, 333]
    heapq.heapify(data)
    root_node = list_to_tree(data)

    if root_node:
        p1 = multiprocessing.Process(target=run_dfs, args=(root_node,))
        p2 = multiprocessing.Process(target=run_bfs, args=(root_node,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()
        print("\nПрограму завершено. Усі вікна закриті.\n")
    else:
        print("Купа порожня.")

if __name__ == '__main__':
    benchmark()
