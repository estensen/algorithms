class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last_element_index = len(self.items) - 1
        return self.items[last_element_index]

    def size(self):
        return len(self.items)
