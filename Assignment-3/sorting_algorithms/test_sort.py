import insertion_sort, bubble_sort, selection_sort, merge_sort, unittest

class Insertion_sort(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertEqual([1,2,3,4,5], insertion_sort.insertion_sort([2,1,5,4,3]))
        self.assertEqual([-535,-44,13,21,123,1000], insertion_sort.insertion_sort([21,1000,13,123,-44,-535]))
        self.assertEqual([-12,40,50,60,70,80,900], insertion_sort.insertion_sort([40,80,-12,50,900,70,60]))

    def test_bubble_sort(self):
        self.assertEqual([1,2,3,4,5], bubble_sort.bubble_sort([2,1,5,4,3]))
        self.assertEqual([-535,-44,13,21,123,1000], bubble_sort.bubble_sort([21,1000,13,123,-44,-535]))
        self.assertEqual([-12,40,50,60,70,80,900], bubble_sort.bubble_sort([40,80,-12,50,900,70,60]))

    def test_selection_sort(self):
        self.assertEqual([1,2,3,4,5], selection_sort.selection_sort([2,1,5,4,3]))
        self.assertEqual([-535,-44,13,21,123,1000], selection_sort.selection_sort([21,1000,13,123,-44,-535]))
        self.assertEqual([-12,40,50,60,70,80,900], selection_sort.selection_sort([40,80,-12,50,900,70,60]))

    def test_merge_sort(self):
        self.assertEqual([1,2,3,4,5], merge_sort.merge_sort([2,1,5,4,3]))
        self.assertEqual([-535,-44,13,21,123,1000], merge_sort.merge_sort([21,1000,13,123,-44,-535]))
        self.assertEqual([-12,40,50,60,70,80,900], merge_sort.merge_sort([40,80,-12,50,900,70,60]))


if __name__ == '__main__':
    unittest.main()