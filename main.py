# Вариант 8


def selection_sort(arr):
    amount = 0
    length = len(arr)
    # set i as amount of elements in the array
    for i in range(length):
        # set lowest_value_index as current i
        lowest_value_index = i
        # for remaining unsorted elements
        for j in range(i+1, length):
            # if elements value is lower that previous lowest elements, swap them
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
            arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]
            amount += 1
    return amount


def insertion_sort(arr):
    length = len(arr)
    amount = 0
    # assume first elem is already sorted
    for i in range(1, length):
        item_to_insert = arr[i]
        # link to previous elem
        j = i - 1
        # move elems up front if elem > item_to_insert
        while j >= 0 and arr[j] < item_to_insert:
            amount += 1
            arr[j + 1] = arr[j]
            j -= 1
        # inserting elem
        arr[j + 1] = item_to_insert
    return amount


if __name__ == '__main__':
    array = [61, 32, 27, 45, 75, 58, 5, 50, 99]
    # 36 exchanges. This algorithm has complexity of n^2 so it will complete 9^2=81 exchanges in the worst case
    print("Overall %d exchanges" % selection_sort(array))
    print("Sorted array", array) # [5, 27, 32, 45, 50, 58, 61, 75, 99]

    # shuffling array
    array = [61, 32, 27, 45, 75, 58, 5, 50, 99]
    # 21 exchanges. This algorithm has complexity of n^2 so it will complete 9^2=81 exchanges in the worst case
    print("Overall %d exchanges" % insertion_sort(array))
    print("Sorted array", array)   # [5, 27, 32, 45, 50, 58, 61, 75, 99]

    # In this case, sorting with insertions was proven to be  more efficient  for this array
    # Insertion sorting cost us 21 iteration, whereas selection sorting cost us 36 iterations


