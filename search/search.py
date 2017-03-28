class Search:
    def sequential_search(self, search_space, item):
        pos = 0
        found = False

        while pos < len(search_space) and not found:
            if search_space[pos] == item:
                found = True
            else:
                pos += 1

        return found

    def binary_search(self, sorted_search_space, item):
        if len(sorted_search_space) == 0:
            return False
        else:
            midpoint = len(sorted_search_space) // 2
            if sorted_search_space[midpoint] == item:
                return True
            else:
                if item < sorted_search_space[midpoint]:
                    return self.binary_search(sorted_search_space[:midpoint], item)
                else:
                    return self.binary_search(sorted_search_space[midpoint+1:], item)

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# Sequential search
s = Search()
print(s.sequential_search(test_list, 3))
print(s.sequential_search(test_list, 13))
test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# Binary search
print(s.binary_search(test_list2, 2))
print(s.binary_search(test_list2, 18))
