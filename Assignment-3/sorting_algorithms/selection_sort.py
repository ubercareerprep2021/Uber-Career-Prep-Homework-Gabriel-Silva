def selection_sort(array: list):
    """ repeatedly finds the minimum element from the unsorted part 
        and replaces at the correct order """
    # traverse through all array elements
    for i in range(len(array)): 
        # find the minimum element in remaining
        # unsorted array
        min_index = i
        # find the minimum element in remaining
        # unsorted array
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
                
        # swap the found minimum element with
        # the lower correspondent index in the array       
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    
    return array