import unittest, Part4

class TestPart4(unittest.TestCase):

    def test_node_instantiation(self):
        node = Part4.Node(0)
        self.assertEqual(type(node.value), int)
        self.assertEqual(node.next, None)

    def test_push_back_adds_one_node(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        self.assertEqual(node.next.value, 456456456)
        self.assertEqual(node.next.next, None)
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        while node.next != None:
             node = node.next 
        self.assertEqual(node.value, 999888777)
        self.assertEqual(node.next, None)

    def test_pop_back_removes_correct_node(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        
        popped_node = node.pop()
        self.assertEqual(popped_node.value, 999888777)
        copy = node
        while copy.next != None:
             copy = copy.next 
        self.assertEqual(copy.value, 99)
        self.assertEqual(copy.next, None)
        
        popped_node = node.pop()
        self.assertEqual(popped_node.value, 99)
        copy = node
        while copy.next != None:
             copy = copy.next 
        self.assertEqual(copy.value, 456456456)
        self.assertEqual(copy.next, None)
        
        popped_node = node.pop()
        self.assertEqual(popped_node.value, 456456456)
        copy = node
        while copy.next != None:
             copy = copy.next 
        self.assertEqual(copy.value, 0)
        self.assertEqual(copy.next, None)

        popped_node = node.pop()
        self.assertEqual(popped_node.value, 0)
        copy = node
        while copy.next != None:
             copy = copy.next
        # don't know if it should remove the first node
        self.assertEqual(copy.value, 0)

    def test_insert_node_index_1(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        node1 = Part4.Node(-123)
        node.insert(2, node1)
        node = node.next
        node = node.next
        self.assertEqual(node.value, -123)
        self.assertEqual(node.next.value, 99)

    def test_insert_node_index_2(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        node1 = Part4.Node(-123)
        node.insert(4, node1)
        node = node.next
        node = node.next
        node = node.next
        self.assertEqual(node.next.value, -123)
        self.assertEqual(node.next.next, None)

    def test_insert_node_index_3(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        node1 = Part4.Node(-123)
        node.insert(10, node1)
        node = node.next
        node = node.next
        node = node.next
        self.assertEqual(node.value, 999888777)
        self.assertEqual(node.next, None)

    def test_remove_node_index(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        node.remove(2)
        node = node.next
        self.assertEqual(node.value, 456456456)
        self.assertEqual(node.next.value, 999888777)

    def test_remove_node_index_1(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        node.remove(3)
        node = node.next
        node = node.next
        self.assertEqual(node.value, 99)
        self.assertEqual(node.next, None)

    def test_element_at(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        element_node = node.element_at(0)
        self.assertEqual(element_node.value, 0)
        element_node = node.element_at(2)
        self.assertEqual(element_node.value, 99)
        element_node = node.element_at(10)
        self.assertEqual(element_node, None)

    def test_size(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        self.assertEqual(node.size(), 4)
        node1 = Part4.Node(10)
        self.assertEqual(node1.size(), 1)
        node2 = Part4.Node(0)
        node2.push(Part4.Node(1))
        node2.push(Part4.Node(2))
        node2.push(Part4.Node(3))
        node2.push(Part4.Node(4))
        node2.push(Part4.Node(5))
        node2.push(Part4.Node(6))
        node2.push(Part4.Node(7))
        node2.push(Part4.Node(8))
        node2.push(Part4.Node(9))
        self.assertEqual(node2.size(), 10)

    def test_string_representation(self):
        node = Part4.Node(0)
        node.push(Part4.Node(456456456))
        node.push(Part4.Node(99))
        node.push(Part4.Node(999888777))
        self.assertEqual(node.print_list(), '045645645699999888777')
        node1 = Part4.Node(10)
        self.assertEqual(node1.print_list(), '10')
        node2 = Part4.Node(0)
        node2.push(Part4.Node(1))
        node2.push(Part4.Node(2))
        node2.push(Part4.Node(3))
        node2.push(Part4.Node(4))
        node2.push(Part4.Node(5))
        node2.push(Part4.Node(6))
        node2.push(Part4.Node(7))
        node2.push(Part4.Node(8))
        node2.push(Part4.Node(9))
        self.assertEqual(node2.print_list(), '0123456789')

    def test_has_cycle(self):
        # node = Part4.Node(0)
        # node.push(Part4.Node(456456456))
        # node.push(Part4.Node(99))
        # node.push(Part4.Node(999888777))
        # self.assertEqual(node.has_cycle(), False)
        # node1 = Part4.Node(10)
        # node1.push(node1)
        # self.assertEqual(node1.has_cycle(), True)
        
        node2 = Part4.Node(0)
        node2.push(Part4.Node(1))
        node2.push(Part4.Node(2))
        node2.push(node2)
        node2.push(Part4.Node(3))
        #node2.push(Part4.Node(4))
        self.assertEqual(node2.has_cycle(), True)

if __name__ == '__main__':
    unittest.main()