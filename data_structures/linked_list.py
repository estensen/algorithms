from node import Node

class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, item):
        current_node = self.head
        found_node = False
        while current_node and not found_node:
            if current_node.get_data() == item:
                found_node = True
            else:
                current_node = current_node.get_next()
        return found_node

    def remove(self, item):
        current_node = self.head
        previous_node = None
        found_node = False
        while not found_node:
            if current_node.get_data() == item:
                found_node = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        if not previous_node:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

    # TODO: Add append
    # TODO: Add insert
    # TODO: Add index
    # TODO: Add pop

    def __repr__(self):
        return (self.data, self.next, self.head)
