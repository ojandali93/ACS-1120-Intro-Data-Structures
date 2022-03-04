#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail
        new_node = Node(item)
        if self.is_empty == True:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.tail.next = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.is_empty == True:
            self.head = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.next = self.head

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        current_node = self.head
        next_node = self.next
        if current_node.data == item:
            return True
        if self.tail.data == item:
            return True
        while current_node is not None:
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False
            

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty == True:
            raise ValueError("The current linked list is empty.")
        if self.find(item) == False:
            raise ValueError('Item not found: {}'.format(item))

        if self.head.data == item and self.tail.data == item:
            self.tail = None
            self.tail = None

        if self.head.data == item:
            self.head = self.head.next
        
        if self.tail.data == item:
            current_node = self.head
            new_tail = current_node
            while current_node.next is not self.tail:
                current_node = current_node.next
                new_tail = current_node 
            self.tail = new_tail
            self.tail.next = None
        else:
            current_node = self.head
            selected_node = current_node
            while current_node is not None and current_node.data is not item:
                selected_node = current_node
                current_node = current_node.next
                reroute_to = current_node.next
            selected_node.next = reroute_to

        


if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)

    


