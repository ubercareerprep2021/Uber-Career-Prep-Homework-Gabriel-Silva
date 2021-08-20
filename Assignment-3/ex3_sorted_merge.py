def sorted_merge(array_a: list, array_b: list):
    index_a = index_b = 0
    
    while (index_b < len(array_b)):
        if index_a < len(array_a):
            if array_b[index_b] > array_a[index_a]:
                index_a += 1
            elif array_b[index_b] <= array_a[index_a]:
                array_a = array_a[:index_a] + [array_b[index_b]] + array_a[index_a:]
                index_a += 1
                index_b += 1
        else:
            array_a = array_a + array_b[index_b:]
            break

    return array_a

if __name__ == '__main__':
    sorted_merge([1,3,5,7], [2,4,6,8])