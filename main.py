# Collection of sorting algorithms
# TODO: Get a .csv containing unsorted integers to read in to test sorting
# TODO: Make a GUI for this

### THE QUICKSORT ALGORITHM ###

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


# Try out your own list here!
testList = [5, 20, 3, -1, 32, 50, 1010, 331]
print(testList)
quickSort(testList, 0, len(testList)-1)
print(testList)


