import unittest, Part5

class TestPart5(unittest.TestCase):
    def test_reverse_list_node(self):
        node = Part5.Node(1)
        node.push(Part5.Node(5))
        node.push(Part5.Node(-10))
        node.push(Part5.Node(12))
        node.push(Part5.Node(20))
        list_reversed = node.reverse_list()
        self.assertEqual(list_reversed.value, 20)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, 12)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, -10)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, 5)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, 1)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed, None)

    def test_stack_reverse_list_node(self):
        node = Part5.Node(1)
        node.push(Part5.Node(5))
        node.push(Part5.Node(-10))
        node.push(Part5.Node(12))
        node.push(Part5.Node(20))
        list_reversed = node.stack_reverse_list()
        self.assertEqual(list_reversed.value, 20)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, 12)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, -10)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, 5)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed.value, 1)
        list_reversed = list_reversed.next
        self.assertEqual(list_reversed, None)
 
if __name__ == '__main__':
    unittest.main()