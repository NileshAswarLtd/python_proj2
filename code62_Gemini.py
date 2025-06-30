class Node:
    """
    Represents a node in a singly linked list.
    Each node has a value and a pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a singly linked list.
    Includes methods to append nodes and detect loops.
    """
    def __init__(self):
        self.head = None
        self.tail = None # Keep track of tail for easy appending

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def has_loop(self):
        """
        Detects if there is a cycle (loop) present in the linked list
        using Floyd's cycle-finding algorithm (Tortoise and Hare).

        Algorithm:
        1. Initialize two pointers, 'slow' and 'fast', both starting at the head.
        2. 'slow' moves one step at a time.
        3. 'fast' moves two steps at a time.
        4. If 'slow' and 'fast' meet at any point, a loop is detected.
        5. If 'fast' or 'fast.next' becomes None, it means the end of the list
           is reached, and there is no loop.

        Returns:
            bool: True if a loop is detected, False otherwise.
        """
        if not self.head or not self.head.next:
            # An empty list or a list with only one node cannot have a loop.
            return False

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next          # Tortoise moves one step
            fast = fast.next.next     # Hare moves two steps

            if slow == fast:
                # If they meet, a loop is present
                return True

        # If fast reaches the end (None), no loop is present
        return False

    def print_list(self):
        """
        Prints the values of the nodes in the linked list.
        Caution: This method might run indefinitely if there's a loop.
        It's primarily for testing non-looped lists.
        """
        current = self.head
        nodes = []
        # Limit printing to avoid infinite loop in case of an undetected cycle
        max_nodes_to_print = 20
        count = 0
        while current and count < max_nodes_to_print:
            nodes.append(str(current.value))
            current = current.next
            count += 1
        if current: # If we stopped because of max_nodes_to_print, indicate a potential loop or very long list
            print(" -> ".join(nodes) + " -> ... (list might be very long or have a loop)")
        else:
            print(" -> ".join(nodes))


# --- Example Usage ---

# Test Case 1: Linked List without a loop
print("--- Test Case 1: Linked List without a loop ---")
ll_no_loop = LinkedList()
ll_no_loop.append(1)
ll_no_loop.append(2)
ll_no_loop.append(3)
ll_no_loop.append(4)
ll_no_loop.print_list()
print(f"Does the list have a loop? {ll_no_loop.has_loop()}") # Expected: False
print("-" * 40)

# Test Case 2: Linked List with a loop
print("--- Test Case 2: Linked List with a loop ---")
ll_with_loop = LinkedList()
ll_with_loop.append(10)
ll_with_loop.append(20)
ll_with_loop.append(30)
ll_with_loop.append(40)
ll_with_loop.append(50)

# Create a loop: Make the last node point to the second node (value 20)
# To do this, we need to manually access the nodes.
# Node 10 -> Node 20 -> Node 30 -> Node 40 -> Node 50
#                     ^----------------------|
if ll_with_loop.head and ll_with_loop.head.next:
    node_20 = ll_with_loop.head.next
    ll_with_loop.tail.next = node_20
    print("Loop created: 50 points back to 20.")
else:
    print("Could not create loop for testing (list too short).")

# We cannot safely print a list with a loop using print_list() as it would run indefinitely.
# print(f"List content (will loop if printed): {ll_with_loop.print_list()}")
print(f"Does the list have a loop? {ll_with_loop.has_loop()}") # Expected: True
print("-" * 40)

# Test Case 3: Empty Linked List
print("--- Test Case 3: Empty Linked List ---")
ll_empty = LinkedList()
ll_empty.print_list()
print(f"Does the list have a loop? {ll_empty.has_loop()}") # Expected: False
print("-" * 40)

# Test Case 4: Single Node Linked List
print("--- Test Case 4: Single Node Linked List ---")
ll_single = LinkedList()
ll_single.append(100)
ll_single.print_list()
print(f"Does the list have a loop? {ll_single.has_loop()}") # Expected: False
print("-" * 40)

# Test Case 5: Loop at head
print("--- Test Case 5: Loop at head ---")
ll_loop_head = LinkedList()
ll_loop_head.append(1)
ll_loop_head.append(2)
ll_loop_head.append(3)
# Create a loop: 3 points back to 1
if ll_loop_head.head:
    ll_loop_head.tail.next = ll_loop_head.head
    print("Loop created: 3 points back to 1 (head).")
print(f"Does the list have a loop? {ll_loop_head.has_loop()}") # Expected: True
print("-" * 40)
