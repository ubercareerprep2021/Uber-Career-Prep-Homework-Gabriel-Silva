def insertion_sort(array: list):
    """values in the unsorted part are placed in the sorted part"""
    # traverse through 1 to len(array)
    for i in range(1, len(array)):
        # get array value in position i 
        key = array[i]
        # get index before i
        j = i-1
        # while it's not in the 0 index and key value is 
        # less than lower index values
        while j >= 0 and key < array[j] :
            # shift right the value on index j
            array[j + 1] = array[j]
            # go to the previous position in the array
            j -= 1
        # store the value in it's ordered position
        array[j + 1] = key
    
    return array
