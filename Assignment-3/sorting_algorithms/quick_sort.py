def quick_sort(array: list, low: int, high: int):
    if len(array) == 1:
        return array
    if low < high:
        # index of smaller element
        partition_index = (low-1)
        # pivot element as the highest index
        pivot = array[high]

        # places smaller than pivot elements to the left and 
        # greater elements to the right
        for index in range(low, high):    
            # If current element is smaller or equal to pivot
            if array[index] <= pivot:
                # increment index of smaller element
                partition_index = partition_index+1
                temp = array[partition_index] 
                array[partition_index] = array[index] 
                array[index] = temp
    
        temp = array[partition_index+1]
        array[partition_index+1] = array[high] 
        array[high] = temp

        partition_index += 1
  
        # sort elements before and after partition
        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)
    
    return array
  