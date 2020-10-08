# Python program for implementation of  
# MergeSort (Alternative) 

def merge_sort(values):
    if len(values) > 1:
        m = len(values) // 2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)


        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)

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
    ...
    
    
    
    initial array = [61, 32, 27, 45, 75, 58, 5, 50, 99] n = 9
    
    
    1: initial array is split until we have sequences with the length of one 
        [61, 32, 27, 45, 75, 58, 5, 50, 99] ->
        [61, 32, 27, 45] [75, 58, 5, 50, 99] ->
        [61, 32] [27, 45] [75, 58] [5, 50, 99] ->
        [61] [32] [27] [45] [75] [58] [5] [50, 99] ->
        [61] [32] [27] [45] [75] [58] [5] [50] [99]
    2: sequences are merged back into array:
        [61] [32] [27] [45] [75] [58] [5] [50] [99] ->
            
        


"""
