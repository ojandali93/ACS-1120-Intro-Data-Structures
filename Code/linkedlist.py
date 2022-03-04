#!python


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        self.head = None 
        self.tail = None 
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        items = []  
        node = self.head  
        while node is not None:  
            items.append(node.data)  
            node = node.next  
        return items  

    def is_empty(self):
        return self.head is None

    def length(self):
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter


    def append(self, item):
        new_node = Node(item)
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        new_node = Node(item)
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, item):
        current_node = self.head
        while current_node is not None: 
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False

    def find_if__matches(self, matching_function):
        current_node = self.head
        while current_node:
            if matching_function(current_node.data): 
                return current_node.data
            current_node = current_node.next
        return None

    def update(self, key, new_data):
        current_node = self.head
        while current_node:
            if key == current_node.data[0]:
                current_node.data[1] = new_data
            current_node = current_node.next

    def delete(self, item):
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

    


