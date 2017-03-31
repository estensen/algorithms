def bubble_sort(data):
    data_length = len(data)
    while True:
        swapped = False
        for i in range(data_length - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        if not swapped:
            break

unsorted_list = [54,26,93,17,77,31,44,55,20]
bubble_sort(unsorted_list)
print(unsorted_list)

almost_sorted_list = [20,30,40,90,50,60,70,80,100,110]
#short_bubble_short(almost_sorted_list)
#print(almost_sorted_list)
