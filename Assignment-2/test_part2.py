import Part2_binary_tree as t, unittest

class TestPart1(unittest.TestCase):

    def test_binarytree_insert_ex1(self):
        tree = t.Node(16)
        t.insert(tree, 10)
        t.insert(tree, 21)
        t.insert(tree, 7)
        t.insert(tree, 18)
        t.insert(tree, 29)
        t.insert(tree, 99)
        t.insert(tree, 13)
        print("\nTest 1")
        tree.print()

    def test_binarytree_find_ex2(self):
        print("\nTest 2")
        tree = t.Node(16)
        t.insert(tree, 10)
        t.insert(tree, 21)
        t.insert(tree, 7)
        t.insert(tree, 18)
        t.insert(tree, 29)
        t.insert(tree, 99)
        t.insert(tree, 13)
        #tree.print()
        for i in range(9, 100):
            result = t.find(tree, i)
            if result:
                print(i, result)

if __name__ == '__main__':
    unittest.main()