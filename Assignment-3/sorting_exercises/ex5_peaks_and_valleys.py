def sort_peaks_and_valleys(array: list):
    aux_array = [array[0]]
    index_aux = 0
    array_to_delete = array[1:]

    # while there are elements to compare
    while len(array_to_delete) > 0:
        max_difference = 0
        # search for element with the biggest diference from the last ordered element
        for element in array_to_delete:
            absolute_diference = abs(aux_array[index_aux] - element)
            if absolute_diference > max_difference:
                max_difference = absolute_diference
                element_to_append = element

        aux_array.append(element_to_append)
        index_aux += 1
        array_to_delete.remove(element_to_append)

    return aux_array

if __name__ == '__main__':
    print(sort_peaks_and_valleys([5, 3, 1, 2, 3])) # answer [5, 1, 3, 2, 3]
    print(sort_peaks_and_valleys([5, 4, 3, 2, 1, 0])) # answer [5, 0, 4, 1, 3, 2]
    print(sort_peaks_and_valleys([-500, -200, -100, 100, 200, 0, 500])) # answer [-500, 500, -200, 200, -100, 100, 0]