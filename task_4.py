import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

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
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph

def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

def list_to_tree(heap_list, index=0):
    if index < len(heap_list):
        node = Node(heap_list[index])
        node.left = list_to_tree(heap_list, 2 * index + 1)
        node.right = list_to_tree(heap_list, 2 * index + 2)
        return node
    return None

def draw_heap(data_list):
    heapq.heapify(data_list)

    root_node = list_to_tree(data_list)

    if root_node:
        draw_tree(root_node)
    else:
        print("Список купи порожній.")

# Приклад використання:
def display_binary_heap():
    print("\nВізуалізація впорядкованої бінарної купи:")
    unordered_data = [0, 4, 5, 10, 1, 3, 2, 8, 7, 9, 6]
    draw_heap(unordered_data)

if __name__ == '__main__':
    display_binary_heap()
