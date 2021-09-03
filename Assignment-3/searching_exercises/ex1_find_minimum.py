# tried binary search but couldn't think in a O(log n) solution
def find_minimum(rotated_sorted_list: list):
    if len(rotated_sorted_list) > 0:
        minimum_element = float('inf')
        for element in rotated_sorted_list:
            if element < minimum_element:
                minimum_element = element
        return minimum_element
    else:
        return -1

        
if __name__ == '__main__':
    array = [4, 5, 1, 2, 3]

    print(find_minimum(array))
