import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def print_list(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        out = " -> ".join(elements) + " -> None"
        print(out)
        return out

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head_ref, new_node):
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head_ref

def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy
    l1, l2 = list1.head, list2.head
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    merged = LinkedList()
    merged.head = dummy.next
    return merged

def draw_linked_list(llist, ax, title, color="skyblue"):
    G = nx.DiGraph()
    labels = {}
    current = llist.head
    i = 0
    if not current:
        ax.set_title(f"{title} (Порожній)")
        ax.axis('off')
        return
    while current:
        node_id = i
        G.add_node(node_id)
        labels[node_id] = f"[{current.data}]"
        if i > 0: G.add_edge(i - 1, node_id)
        current = current.next
        i += 1
    G.add_node("None")
    labels["None"] = "None"
    G.add_edge(i - 1, "None")
    pos = {n: (idx, 0) for idx, n in enumerate(G.nodes())}
    ax.set_title(title, fontsize=12, fontweight='bold')
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=1200, 
            node_color=color, font_size=9, arrowsize=15, edge_color="gray", ax=ax)
    ax.axis('off')

# Приклад використання:
def process_and_visualize_lists():
    fig, axes = plt.subplots(6, 1, figsize=(8, 14)) 
    plt.subplots_adjust(hspace=0.6, top=0.95, bottom=0.05)

    # 1. Робота з основним списком
    llist = LinkedList()
    for val in input_data: llist.insert_at_end(val)
    print("\nОригінальний список:")
    llist.print_list()
    draw_linked_list(llist, axes[0], "1. Оригінальний список", color="lightgray") # <--- ВИПРАВЛЕНО

    # 2. Реверс
    llist.reverse()
    print("Реверсований список:")
    llist.print_list()
    draw_linked_list(llist, axes[1], "2. Реверсований список", color="salmon") # <--- ВИПРАВЛЕНО

    # 3. Сортування
    llist.insertion_sort()
    print("Відсортований список:")
    llist.print_list()
    draw_linked_list(llist, axes[2], "3. Відсортований список", color="lightgreen") # <--- ВИПРАВЛЕНО

    # 4. Об'єднання двох списків
    list_a = LinkedList()
    for x in list_a_data: list_a.insert_at_end(x)
    
    list_b = LinkedList()
    for x in list_b_data: list_b.insert_at_end(x)

    print("\nСписок A (початковий):")
    list_a.print_list()
    draw_linked_list(list_a, axes[3], "4a. Список A (несортований)", color="gray")

    print("Список B (початковий):")
    list_b.print_list()
    draw_linked_list(list_b, axes[4], "4b. Список B (несортований)", color="gray")

    list_a.insertion_sort()
    list_b.insertion_sort()

    merged = merge_sorted_lists(list_a, list_b)
    print("Об'єднаний A+B відсортований список:")
    merged.print_list()
    draw_linked_list(merged, axes[5], "4c. Об'єднаний список (A+B)", color="lightblue")

    plt.show()

if __name__ == "__main__":
    input_data = [4, 2, 1, 3]
    list_a_data = [23, 54, 1, 5, 10, 4, 67, 34]
    list_b_data = input_data

    process_and_visualize_lists()
