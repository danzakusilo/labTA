# Python program for implementation of  
# MergeSort (Alternative) 

def merge_sort(values):
    # recursively splitting array until we have sequences with the size of 1 element
    if len(values) > 1:
        m = len(values) // 2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)
        # array for sorted and temporary values
        values = []
        # comparing the values and appending them to respective temporary arrays
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)
        # after all the comparisons are done, the left and right array are merged back together
        for i in left:
            values.append(i)
        for i in right:
            values.append(i)

    return values


""" 
    algorithm visualisation
    initial array is split in two
    left = [61,32,27,45] right = [75,58,5,50,99]
    left and right are both spilt in two like this
    leftleft = [61,32] leftright = [27,45], rightleft = [75,58], rightright = [5,50,99]
    this continues recursively until all elements are individual. 

    then, the a simple sorting algorithm is used to merge values back into a single array, whilst sorting them in pairs,
    fours and so on

    initial array = [61, 32, 27, 45, 75, 58, 5, 50, 99] n = 9

    1: initial array is split until we have sequences with the length of one 
        [61, 32, 27, 45, 75, 58, 5, 50, 99] ->
        [61, 32, 27, 45] [75, 58, 5, 50, 99] ->
        [61, 32] [27, 45] [75, 58] [5, 50, 99] ->
        [61] [32] [27] [45] [75] [58] [5] [50, 99] ->
        [61] [32] [27] [45] [75] [58] [5] [50] [99]
    2: adjacent sequences are merged back into array:
        [61] [32] [27] [45] [75] [58] [5] [50] [99] ->
            32 < 61, 27 < 45, 58 < 75, 5 < 50, so
            [32,61] [27,45] [58, 75] [5,50] [99] ->
            27<32<45<61, 5<50<58<75<99, so
            [27, 32, 45, 61] [5,50,58,75,99] ->
            5<27<32<45<50<58<61<75<99, so
            [5,27,32,45,50,58,61,75,99]
    3: sorted array look like this :
        [5,27,32,45,50,58,61,75,99]

"""


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        # if current element is smaller than pivot,
        # increment the index of the smallest element
        # and swap them
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    # the smallest elements is swapped with the highest
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # this index determines how will the array be split
        index = partition(arr, low, high)
        quick_sort(arr, low, index-1)
        quick_sort(arr, index+1, high)
    return arr


"""
initial array : [61, 32, 27, 45, 75, 58, 5, 50, 99] 

quicksort :
    [61, 32, 27, 45, 75, 58, 5, 50, 99] -> 
    let the second last value (50) be the pivot, so 
    if values bigger then pivot go the right sublist and 
    values lower than pivot will go to the left sublist 
    like this :
    [61, 32, 27, 45, 75, 58, 5, 50, 99] ->
    [61, 32, 27, 45, 5, 58, 50, 75, 99] ->
    [58, 32, 27, 45, 5, 50, 61, 75, 99] ->
    [5, 32, 27, 45, 50, 58, 61, 75, 99] ->
    
    now, the same procedure is applied to 
    [5,32,27,45] and [58,61,75,99]
          
    sorted array look like :
    5 27 32 45 50 58 61 75 99

"""

a = [61, 32, 27, 45, 75, 58, 5, 50, 99]
print("Given array is")
print(*a)

a = merge_sort(a)

print("Sorted array is : ")
print(*a)

a = [61, 32, 27, 45, 75, 58, 5, 50, 99]
print("Given array is")
print(*a)

a = quick_sort(a, 0, len(a)-1)

print("Sorted array is : ")
print(*a)






