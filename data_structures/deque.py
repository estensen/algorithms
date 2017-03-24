class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# Test output
d = Deque()
print(d.is_empty())
d.add_rear(4)
d.add_rear("dog")
d.add_front("cat")
d.add_front(True)
print(d.size())
print(d.is_empty())
d.add_rear(8.4)
print(d.items)
print(d.remove_rear())
print(d.remove_front())
