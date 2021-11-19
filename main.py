# Collection of sorting algorithms
# TODO: Get a .csv containing unsorted integers to read in to test sorting
# TODO: Make a GUI for this

### THE QUICKSORT ALGORITHM -- O(nlogn) -> O(n^2) ###

# partition - Defines a pivot element then rearranges list so that elements less than or equal to the pivot
# are to the left of it while elements greater than or equal to it are on the right
# The start and end arguments specify which part of the list to partition
def partition(list, start, end):
    # define pivot element as the first element in the list
    pivot = list[start]
    # the low value is set as the value of the element immediately after the pivot
    low = start + 1
    # the high value is set to end
    high = end

    while(True):

        # Look for an element before the low pointer that is less than the pivot
        while low <= high and list[high] >= pivot:
            high -= 1

        # Look for an element that is greater than the pivot
        while low <= high and list[low] <= pivot:
            low += 1

        # Swap the two elements if we have not gone through the list yet
        if low <= high:
            temp = list[low]
            list[low] = list[high]
            list[high] = temp

        # Otherwise exit the loop
        else:
            break

    # Now move the pivot into the correct position
    temp = list[start]
    list[start] = list[high]
    list[high] = temp

    # return the high index
    return high

# Quicksort recursively calls itself, repeatedly breaking the list into left and right sublists
# until it reaches lists of 0 or 1 elements
# At that point the list is sorted
def quickSort(list, start, end):
    if start >= end:
        return

    p = partition(list, start, end)
    quickSort(list, start, p-1)
    quickSort(list, p+1, end)

### THE MERGESORT ALGORITHM -- O(nlogn)###

def merge(list, left, right, middle):
    # First make copies of each array to be merged
    left_copy = list[left:middle+1]
    right_copy = list[middle+1:right+1]

    # Pointers to keep track of position in each array
    left_copy_pos = 0
    right_copy_pos = 0
    sorted_index = left

    # Now go through both list copies until we run out of elements in one of them
    while left_copy_pos < len(left_copy) and right_copy_pos < len(right_copy):

        # If the left copy element is smaller, position it in the sorted array
        if left_copy[left_copy_pos] <= right_copy[right_copy_pos]:
            list[sorted_index] = left_copy[left_copy_pos]
            left_copy_pos += 1

        # If the right copy element is smaller, position it in the sorted array
        else:
            list[sorted_index] = right_copy[right_copy_pos]
            right_copy_pos += 1

        # Move the pointer for the sorted list forward
        sorted_index += 1

    # We have now run out of elements in one of the arrays
    # At this point we can add all remaining elements of the leftover array in the order they are currently in
    while left_copy_pos < len(left_copy):
        list[sorted_index] = left_copy[left_copy_pos]
        left_copy_pos += 1
        sorted_index += 1

    while right_copy_pos < len(right_copy):
        list[sorted_index] = right_copy[right_copy_pos]
        right_copy_pos += 1
        sorted_index += 1

# Merge sort recursively breaks the list in half until we have subarrays of one element each
# Merge is then called on pairs of these arrays, and the elements are 'merged' into their sorted positions
def mergeSort(list, left, right):
    # Base case
    if left >= right:
        return

    # Recursive steps
    middle = (left + right) // 2
    mergeSort(list, left, middle)
    mergeSort(list, middle+1, right)
    merge(list, left, right, middle)

# Try out your own list here!
testList = [31, 45, 2, 35, 7, 50, 100, 1, 28, 47, 30, 3, 49, 15, 21, 24, 45]
print(testList)
mergeSort(testList, 0, len(testList)-1)
print(testList)


