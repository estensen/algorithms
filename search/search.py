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

    def binary_search(self):
        first = 0
        last = len(self.search_space) - 1
        found = False

        while first <= last and not found:
            midpoint = (first + last) // 2
            if self.search_space[midpoint] == self.item:
                found = True
            else:
                if self.item < self.search_space[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# Sequential search
print(Search(test_list, 3).sequential_search())
print(Search(test_list, 13).sequential_search())
test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# Binary search
print(Search(test_list2, 2).binary_search())
print(Search(test_list2, 18).binary_search())
