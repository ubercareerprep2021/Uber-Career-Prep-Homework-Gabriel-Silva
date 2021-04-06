import Part3, unittest

class TestPart3(unittest.TestCase):

    def test_stack_instantiation(self):
        stack = Part3.Stack()
        self.assertEqual(type(stack.stack), list)
        self.assertEqual(len(stack.stack), 0)

    def test_stack_push(self):
        stack = Part3.Stack()
        stack.push(5)
        self.assertEqual(stack.stack[-1], 5)
        self.assertEqual(len(stack.stack), 1)
        stack.push(-10)
        self.assertEqual(stack.stack[-1], -10)
        self.assertEqual(len(stack.stack), 2)
        stack.push(999)
        self.assertEqual(stack.stack[-1], 999)
        self.assertEqual(len(stack.stack), 3)
        self.assertEqual(stack.stack, [5, -10, 999])

    def test_stack_pop(self):
        stack = Part3.Stack()
        stack.push(5)
        stack.push(-10)
        stack.push(999)
        pop_value = stack.pop()
        self.assertEqual(pop_value, 999)
        pop_value = stack.pop()
        self.assertEqual(pop_value, -10)
        pop_value = stack.pop()
        self.assertEqual(pop_value, 5)
        pop_value = stack.pop()
        self.assertEqual(pop_value, None)
        stack.push(-999999)
        stack.push(151515)
        pop_value = stack.pop()
        self.assertEqual(pop_value, 151515)
        stack.push(21212121)
        pop_value = stack.pop()
        self.assertEqual(pop_value, 21212121)
        # pops 100 times
        for i in range(0, 100):
            pop_value = stack.pop()
        self.assertEqual(pop_value, None)
    
    def test_stack_top(self):
        stack = Part3.Stack()
        top_value = stack.top()
        self.assertEqual(top_value, None)
        
        stack.push(5)
        stack.push(-10)
        stack.push(999)
        top_value = stack.top()
        self.assertEqual(top_value, 999)
        stack.pop()
        top_value = stack.top()
        self.assertEqual(top_value, -10)

        stack.push(-999999)
        top_value = stack.top()
        self.assertEqual(top_value, -999999)
        stack.push(151515)
        top_value = stack.top()
        self.assertEqual(top_value, 151515)

    def test_stack_emptyness(self):
        stack = Part3.Stack()
        self.assertTrue(stack.isEmpty())        
        stack.push(5)
        stack.push(-10)
        stack.push(999)
        self.assertFalse(stack.isEmpty())
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_stack_size(self):
        stack = Part3.Stack()
        self.assertEqual(stack.size(), 0)        
        stack.push(5)
        stack.push(-10)
        stack.push(999)
        self.assertEqual(stack.size(), 3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)

# -------------------------------------------------------------------------------
    def test_queue_instantiation(self):
        queue = Part3.Queue()
        self.assertEqual(type(queue.queue), list)
        self.assertEqual(len(queue.queue), 0)

    def test_enqueue(self):
        queue = Part3.Queue()
        queue.enqueue(5)
        self.assertEqual(queue.queue[-1], 5)
        self.assertEqual(len(queue.queue), 1)
        queue.enqueue(-10)
        self.assertEqual(queue.queue[-1], -10)
        self.assertEqual(len(queue.queue), 2)
        queue.enqueue(999)
        self.assertEqual(queue.queue[-1], 999)
        self.assertEqual(len(queue.queue), 3)
        self.assertEqual(queue.queue, [5, -10, 999])

    def test_dequeue(self):
        queue = Part3.Queue()
        queue.enqueue(5)
        queue.enqueue(-10)
        queue.enqueue(999)
        queue.dequeue()
        self.assertEqual(queue.queue, [-10, 999])
        queue.dequeue()
        self.assertEqual(queue.queue, [999])
        queue.dequeue()
        self.assertEqual(queue.queue, [])

        queue.enqueue(-999999)
        queue.enqueue(151515)
        queue.dequeue()
        self.assertEqual(queue.queue, [151515])
        queue.enqueue('string')
        queue.dequeue()
        self.assertEqual(queue.queue, ['string'])
        # dequeues 100 times
        for i in range(0, 100):
            queue.dequeue()
        self.assertEqual(queue.queue, [])
    
    def test_queue_front(self):
        queue = Part3.Queue()
        front_value = queue.front()
        self.assertEqual(front_value, None)
        
        queue.enqueue(5)
        queue.enqueue('string test')
        queue.enqueue(999)
        queue.enqueue(0)

        front_value = queue.front()
        self.assertEqual(front_value, 5)
        queue.dequeue()
        front_value = queue.front()
        self.assertEqual(front_value, 'string test')

        queue.dequeue()
        front_value = queue.front()
        self.assertEqual(front_value, 999)
        
    def test_queue_rear(self):
        queue = Part3.Queue()
        rear_value = queue.rear()
        self.assertEqual(rear_value, None)
        
        queue.enqueue(5)
        queue.enqueue('string test')
        queue.enqueue(999)
        rear_value = queue.rear()
        self.assertEqual(rear_value, 999)
        queue.dequeue()
        rear_value = queue.rear()
        self.assertEqual(rear_value, 999)
        queue.dequeue()
        rear_value = queue.rear()
        self.assertEqual(rear_value, 999)
        for i in range(0, 100):
            queue.dequeue()
        rear_value = queue.rear()
        self.assertEqual(rear_value, None)

    def test_queue_size(self):
        queue = Part3.Queue()
        self.assertEqual(queue.size(), 0)        
        queue.enqueue(5)
        queue.enqueue(-10)
        queue.enqueue(999)
        self.assertEqual(queue.size(), 3)
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.size(), 1)
        queue.dequeue()
        self.assertEqual(queue.size(), 0)

    def test_queue_emptyness(self):
        queue = Part3.Queue()
        self.assertTrue(queue.isEmpty())        
        queue.enqueue(5)
        queue.enqueue(-10)
        queue.enqueue(999)
        self.assertFalse(queue.isEmpty())
        queue.dequeue()
        queue.dequeue()
        self.assertFalse(queue.isEmpty())
        queue.dequeue()
        self.assertTrue(queue.isEmpty())


if __name__ == '__main__':
    unittest.main()