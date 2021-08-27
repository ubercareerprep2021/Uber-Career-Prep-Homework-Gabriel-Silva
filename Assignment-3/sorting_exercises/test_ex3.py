import ex3_sorted_merge, unittest

class Insertion_sort(unittest.TestCase):
    list_sorted_1 = [1,2,3,4,5]
    list_sorted_2 = [-535,-44,13,21,123,1000]
    list_sorted_3 = [-12,40,50,60,70,80,900]
    list_sorted_4 = [-9,-7,-5,-3,-1,0,1,3,5,7,9]
    list_sorted_5 = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
    list_sorted_6 = []
    
    merge_sorted_1_2 = [-535,-44,1,2,3,4,5,13,21,123,1000]
    merge_sorted_2_3 = [-535,-44,-12,13,21,40,50,60,70,80,123,900,1000]
    merge_sorted_3_3 = [-12,-12,40,40,50,50,60,60,70,70,80,80,900,900]
    merge_sorted_4_5 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,0,1,2,3,4,5,6,7,8,9,10]
    merge_sorted_1_5 = [-10,-8,-6,-4,-2,0,1,2,2,3,4,4,5,6,8,10]
    merge_sorted_1_4 = [-9,-7,-5,-3,-1,0,1,1,2,3,3,4,5,5,7,9]

    def test_sorted_merge(self):
        self.assertEqual(self.merge_sorted_1_2, ex3_sorted_merge.sorted_merge(self.list_sorted_1, self.list_sorted_2))
        self.assertEqual(self.merge_sorted_1_2, ex3_sorted_merge.sorted_merge(self.list_sorted_2, self.list_sorted_1))
        self.assertEqual(self.merge_sorted_2_3, ex3_sorted_merge.sorted_merge(self.list_sorted_2, self.list_sorted_3))
        self.assertEqual(self.merge_sorted_2_3, ex3_sorted_merge.sorted_merge(self.list_sorted_3, self.list_sorted_2))
        self.assertEqual(self.merge_sorted_3_3, ex3_sorted_merge.sorted_merge(self.list_sorted_3, self.list_sorted_3))
        self.assertEqual(self.merge_sorted_4_5, ex3_sorted_merge.sorted_merge(self.list_sorted_4, self.list_sorted_5))
        self.assertEqual(self.merge_sorted_4_5, ex3_sorted_merge.sorted_merge(self.list_sorted_5, self.list_sorted_4))
        self.assertEqual(self.merge_sorted_1_5, ex3_sorted_merge.sorted_merge(self.list_sorted_1, self.list_sorted_5))
        self.assertEqual(self.merge_sorted_1_5, ex3_sorted_merge.sorted_merge(self.list_sorted_5, self.list_sorted_1))
        self.assertEqual(self.merge_sorted_1_4, ex3_sorted_merge.sorted_merge(self.list_sorted_1, self.list_sorted_4))
        self.assertEqual(self.merge_sorted_1_4, ex3_sorted_merge.sorted_merge(self.list_sorted_4, self.list_sorted_1))
        self.assertEqual(self.list_sorted_1, ex3_sorted_merge.sorted_merge(self.list_sorted_6, self.list_sorted_1))
        self.assertEqual(self.list_sorted_1, ex3_sorted_merge.sorted_merge(self.list_sorted_1, self.list_sorted_6))
        self.assertEqual(self.list_sorted_6, ex3_sorted_merge.sorted_merge(self.list_sorted_6, self.list_sorted_6))

    
if __name__ == '__main__':
    unittest.main()