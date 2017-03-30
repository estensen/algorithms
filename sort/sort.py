def bubble_sort(data):
    data_length = len(data)
    for i in range(data_length):
        swapped = False
        for j in range(data_length - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]



unsorted_list = [54,26,93,17,77,31,44,55,20]
bubble_sort(unsorted_list)
print(unsorted_list)
