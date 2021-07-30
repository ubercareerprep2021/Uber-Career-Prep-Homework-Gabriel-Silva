def merge_sort(array: list):
    if len(array) > 1:
         # finding the mid index of the array
        middle = len(array)//2
        # dividing the array in left and right
        left_array = array[:middle]
        right_array = array[middle:]
 
        # sorting the first half recursevely
        merge_sort(left_array)
        # sorting the second half recursevely
        merge_sort(right_array)
 
        i = j = k = 0
        # copy elements in order between left and right 
        # into array
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
 
        # copy the remaining elements into array
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    return array
