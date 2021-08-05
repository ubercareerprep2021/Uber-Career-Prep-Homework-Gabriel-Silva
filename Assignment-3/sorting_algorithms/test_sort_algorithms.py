import insertion_sort, bubble_sort, selection_sort, merge_sort, quick_sort, unittest

class Insertion_sort(unittest.TestCase):
    list_sorted_1 = [1,2,3,4,5]
    list_unsorted_1 = [2,1,5,4,3]    
    list_sorted_2 = [-535,-44,13,21,123,1000]
    list_unsorted_2 = [21,1000,13,123,-44,-535]
    list_sorted_3 = [-12,40,50,60,70,80,900]
    list_unsorted_3 = [40,80,-12,50,900,70,60]

    def test_insertion_sort(self):
        self.assertEqual(self.list_sorted_1, insertion_sort.insertion_sort(self.list_unsorted_1))
        self.assertEqual(self.list_sorted_2, insertion_sort.insertion_sort(self.list_unsorted_2))
        self.assertEqual(self.list_sorted_3, insertion_sort.insertion_sort(self.list_unsorted_3))

    def test_bubble_sort(self):
        self.assertEqual(self.list_sorted_1, bubble_sort.bubble_sort(self.list_unsorted_1))
        self.assertEqual(self.list_sorted_2, bubble_sort.bubble_sort(self.list_unsorted_2))
        self.assertEqual(self.list_sorted_3, bubble_sort.bubble_sort(self.list_unsorted_3))

    def test_selection_sort(self):
        self.assertEqual(self.list_sorted_1, selection_sort.selection_sort(self.list_unsorted_1))
        self.assertEqual(self.list_sorted_2, selection_sort.selection_sort(self.list_unsorted_2))
        self.assertEqual(self.list_sorted_3, selection_sort.selection_sort(self.list_unsorted_3))

    def test_merge_sort(self):
        self.assertEqual(self.list_sorted_1, merge_sort.merge_sort(self.list_unsorted_1))
        self.assertEqual(self.list_sorted_2, merge_sort.merge_sort(self.list_unsorted_2))
        self.assertEqual(self.list_sorted_3, merge_sort.merge_sort(self.list_unsorted_3))

    def test_quick_sort(self):
        self.assertEqual(self.list_sorted_1, quick_sort.quick_sort(self.list_unsorted_1, 0, len(self.list_unsorted_1) - 1))
        self.assertEqual(self.list_sorted_2, quick_sort.quick_sort(self.list_unsorted_2, 0, len(self.list_unsorted_2) - 1))
        self.assertEqual(self.list_sorted_3, quick_sort.quick_sort(self.list_unsorted_3, 0, len(self.list_unsorted_3) - 1))


if __name__ == '__main__':
    unittest.main()