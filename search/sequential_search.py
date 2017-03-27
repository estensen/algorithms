class SequentialSearch:
    def __init__(self, search_space, item):
        self.search_space = search_space
        self.item = item

    def search(self):
        pos = 0
        found = False

        while pos < len(self.search_space) and not found:
            if self.search_space[pos] == self.item:
                found = True
            else:
                pos += 1

        return found
