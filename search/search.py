class Search:
    def __init__(self, search_space, item):
        self.search_space = search_space
        self.item = item

    def sequential_search(self):
        pos = 0
        found = False

        while pos < len(self.search_space) and not found:
            if self.search_space[pos] == self.item:
                found = True
            else:
                pos += 1

        return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(Search(test_list, 3).sequential_search())
print(Search(test_list, 13).sequential_search())
