class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        if val <= self.data:
            if not self.left:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def contains(self, val):
        if val == self.data:
            return True
        elif val < self.data:
            if not self.left:
                return False
            else:
                return self.left.contains(val)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(val)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)
