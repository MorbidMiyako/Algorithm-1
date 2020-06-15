def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] is target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lowest = 0
    highest = len(arr) - 1
    middle = len(arr)//2
    while lowest <= highest:
        middle = (lowest + highest)//2
        if arr[middle] is target:
            return middle
        if arr[middle] > target:
            highest = middle - 1
        if arr[middle] < target:
            lowest = middle + 1

    return -1  # not found
