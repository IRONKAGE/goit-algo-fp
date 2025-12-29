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
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    # 1. Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Сортування вставками (Insertion Sort)
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
        else:
            current = head_ref
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            return head_ref

# 3. Функція об'єднання двох відсортованих списків
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy
    
    l1 = list1.head
    l2 = list2.head
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 or l2
    
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Приклад використання:
llist = LinkedList()
llist.insert_at_end(4)
llist.insert_at_end(2)
llist.insert_at_end(1)
llist.insert_at_end(3)

print("\nОригінальний список:")
llist.print_list()

llist.reverse()
print("Реверсований список:")
llist.print_list()

llist.insertion_sort()
print("Відсортований список:")
llist.print_list()

list_a = LinkedList()
for i in [1, 5, 10]: list_a.insert_at_end(i)

list_b = LinkedList()
for i in [2, 3, 8]: list_b.insert_at_end(i)

merged = merge_sorted_lists(list_a, list_b)
print("Об'єднаний відсортований список:")
merged.print_list()
