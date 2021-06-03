import Binary_tree as t, unittest

class TestPart1(unittest.TestCase):

    def test_binarytree_find_ex2(self):
        tree = t.BinaryTree(16)
        tree.insert(10)
        tree.insert(21)
        tree.insert(7)
        tree.insert(18)
        tree.insert(29)
        tree.insert(99)
        tree.insert(13)
        for i in range(9, 100):
            result = tree.find(i)
            if result:
                self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()