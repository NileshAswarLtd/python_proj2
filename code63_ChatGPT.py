class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None

        while current:
            if current.value in seen:
                # Duplicate found: remove current node
                prev.next = current.next
            else:
                seen.add(current.value)
                prev = current
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
