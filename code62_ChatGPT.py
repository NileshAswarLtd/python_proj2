class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next         # Move slow by 1 step
            fast = fast.next.next    # Move fast by 2 steps

            if slow == fast:
                return True          # Loop detected

        return False                 # No loop

    # Helper method to add a node to the list
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
