# tried binary search but couldn't think in a O(log n) solution
def find_element(rotated_sorted_list: list, element: int):
    for elem in rotated_sorted_list:
        if element == elem:
            return elem
    return -1


if __name__ == '__main__':
    array = [4, 5, 1, 2, 3]
    element = 10

    print(find_element(array, element))