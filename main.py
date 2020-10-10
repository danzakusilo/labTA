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


a = [61, 32, 27, 45, 75, 58, 5, 50, 99]
print("Given array is")
print(*a)

a = merge_sort(a)

print("Sorted array is : ")
print(*a)

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
