def bubble_sort(data):
    """The generic bad algorithm"""
    data_length = len(data)
    for pass_num in range(data_length - 1, 0, -1):
        for i in range(pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

def short_bubble_short(data):
    """Skips elements when they are already sorted"""
    data_length = len(data)
    while True:
        swapped = False
        for i in range(data_length - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        if not swapped:
            break

def quicksort(data):
    """Not in place implementation of quicksort"""
    less = []
    equal = []
    greater = []

    if len(data) > 1
        pivot = data[0]
        for x in data:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return data


unsorted_list = [54,26,93,17,77,31,44,55,20]
bubble_sort(unsorted_list)
print(unsorted_list)

almost_sorted_list = [20,30,40,90,50,60,70,80,100,110]
short_bubble_short(almost_sorted_list)
print(almost_sorted_list)

print('Quicksort')
print(quicksort(unsorted_list))

