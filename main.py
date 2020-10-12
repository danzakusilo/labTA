import time
import matplotlib.pyplot as plt


def heapify(arr, heap_size, root_index):
    # Let largest largest element be the root element of the tree
    largest = root_index
    left_descendent = (2 * root_index) + 1
    right_descendent =(2 * root_index) + 2

    # Set descendent as the lartgest element is it's bigger than the current largest element
    if left_descendent < heap_size and arr[left_descendent] > arr[largest]:
        largest = left_descendent
    if right_descendent < heap_size and arr[right_descendent] > arr[largest]:
        largest = right_descendent
    # If root element is no longer largest, swap them and call heapify() to check if it's in right place
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)


def heap_sort(arr):
    length = len(arr)

    # building a max_heap
    for i in range(length, -1, -1):
        heapify(arr, length, i)
    print("max_heap: {}".format(arr))

    # Move root of max_heap to the end of the list,
    # then heapify the remaining array and repeat fot each element
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print("{} to go to the end of the list: {}".format(arr[i], arr))
        heapify(arr, i, 0)


array = [61, 32, 27, 45, 75, 58, 5, 50, 99]
print("Initial array: {}".format(array))

start_time = time.perf_counter()

heap_sort(array)

finish_time = time.perf_counter() - start_time

print("\n Sorted array : {}".format(array))

plt.figure(figsize=(5, 5))
plt.subplot()
plt.ylabel("Time, sec")
plt.plot(range(2), [0, finish_time], label='heap_sort')
plt.legend(loc='lower right')
plt.title('Sort speed comparison')
plt.show()


"""
heapify visualization:
    initial array: 61, 32, 27, 45, 75, 58, 5, 50, 99
                61(0)
                /    \
            32(1)    27(2)
            /   \    /   \
        45(3) 75(4) 58(5) 5(6)
        /  \
    50(7)   99(8)
    
    applying heapify() to index 4:
                61(0)
                /    \
            32(1)    27(2)
            /   \    /   \
        45(3) 75(4) 58(5) 5(6)
        /  \
    50(7)   99(8)
    
    applying heapify to index 8:
                99(0)
                /    \
            75(1)    58(2)
            /   \    /   \      }<- max_heap, that which we can apply heap_sort to
        61(3) 50(4) 32(5) 27(6)  
        /  \
    45(7)   5(8)
    
    heap_ort visualization can be observed in console
"""