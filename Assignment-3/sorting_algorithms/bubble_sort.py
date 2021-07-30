def bubble_sort(array):
    """swapp adjacent elements if they are in wrong order"""
    array_lenght = len(array) 
    # traverse through all array elements
    for i in range(array_lenght):
        # last i elements will be in place at 
        # the end of the pass
        for j in range(0, array_lenght-i-1):
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array