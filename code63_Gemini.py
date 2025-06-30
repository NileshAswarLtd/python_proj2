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
    Includes methods to append nodes, detect loops, and remove duplicates.
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

    def remove_duplicates(self):
        """
        Removes all duplicate integer values from the linked list in-place.
        The relative order of the remaining unique nodes is preserved.

        This method uses a hash set (Python's set) to keep track of values
        that have already been encountered.

        Algorithm:
        1. Initialize an empty set called 'seen_values'.
        2. Initialize two pointers: 'current' starting at the head, and
           'previous' starting at None.
        3. Iterate through the list with 'current':
           a. If 'current.value' is already in 'seen_values':
              This means it's a duplicate. Remove it by linking 'previous.next'
              to 'current.next'.
           b. If 'current.value' is NOT in 'seen_values':
              Add 'current.value' to 'seen_values'.
              Update 'previous' to 'current' (since 'current' is now a unique node).
           c. Move 'current' to 'current.next' for the next iteration.
        4. After the loop, update the tail pointer if necessary.
        """
        if not self.head:
            return # Empty list, nothing to do

        seen_values = set()
        current = self.head
        previous = None

        while current:
            if current.value in seen_values:
                # Duplicate found: skip the current node
                if previous:
                    previous.next = current.next
                else:
                    # This case should not happen if previous is correctly managed
                    # unless the head itself is a duplicate, which is handled below.
                    pass
            else:
                # Not a duplicate: add to seen and advance previous
                seen_values.add(current.value)
                previous = current

            current = current.next

        # After removing duplicates, the tail might have changed.
        # Re-set the tail by traversing to the end if previous exists,
        # or if the list became empty.
        if previous:
            self.tail = previous
        else:
            # If previous is None, it means the list became empty (e.g., all duplicates)
            self.head = None
            self.tail = None


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

# --- New Test Cases for remove_duplicates ---

# Test Case 6: Remove duplicates from a list with duplicates
print("--- Test Case 6: Remove duplicates from a list with duplicates ---")
ll_duplicates = LinkedList()
ll_duplicates.append(1)
ll_duplicates.append(2)
ll_duplicates.append(3)
ll_duplicates.append(2) # Duplicate
ll_duplicates.append(4)
ll_duplicates.append(1) # Duplicate
ll_duplicates.append(5)
print("Original list:")
ll_duplicates.print_list()
ll_duplicates.remove_duplicates()
print("List after removing duplicates:")
ll_duplicates.print_list() # Expected: 1 -> 2 -> 3 -> 4 -> 5
print("-" * 40)

# Test Case 7: Remove duplicates from a list with all duplicates
print("--- Test Case 7: Remove duplicates from a list with all duplicates ---")
ll_all_duplicates = LinkedList()
ll_all_duplicates.append(7)
ll_all_duplicates.append(7)
ll_all_duplicates.append(7)
print("Original list:")
ll_all_duplicates.print_list()
ll_all_duplicates.remove_duplicates()
print("List after removing duplicates:")
ll_all_duplicates.print_list() # Expected: 7
print("-" * 40)

# Test Case 8: Remove duplicates from an empty list
print("--- Test Case 8: Remove duplicates from an empty list ---")
ll_empty_dup = LinkedList()
print("Original list:")
ll_empty_dup.print_list()
ll_empty_dup.remove_duplicates()
print("List after removing duplicates:")
ll_empty_dup.print_list() # Expected: (empty)
print("-" * 40)

# Test Case 9: Remove duplicates from a list with no duplicates
print("--- Test Case 9: Remove duplicates from a list with no duplicates ---")
ll_no_dup = LinkedList()
ll_no_dup.append(10)
ll_no_dup.append(20)
ll_no_dup.append(30)
print("Original list:")
ll_no_dup.print_list()
ll_no_dup.remove_duplicates()
print("List after removing duplicates:")
ll_no_dup.print_list() # Expected: 10 -> 20 -> 30
print("-" * 40)

# Test Case 10: Remove duplicates with head as duplicate
print("--- Test Case 10: Remove duplicates with head as duplicate ---")
ll_head_dup = LinkedList()
ll_head_dup.append(1)
ll_head_dup.append(1)
ll_head_dup.append(2)
ll_head_dup.append(3)
print("Original list:")
ll_head_dup.print_list()
ll_head_dup.remove_duplicates()
print("List after removing duplicates:")
ll_head_dup.print_list() # Expected: 1 -> 2 -> 3
print("-" * 40)
