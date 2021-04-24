import Part3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def push(self, node) -> None:
        """ Adds the node to the end of the list """
        while self.next is not None:
            self = self.next
        self.next = node

    def reverse_list(self):
    """ Function that reverses a linked list iteratively """
        before = None
        while(self is not None):
            # next from the actual node
            next = self.next
            # actual next will point to the node before
            self.next = before
            # next "while loop" before node will be the actual node
            before = self
            # next "while loop" actual node will be the next node
            self = next            
        self = before
        return self

    def stack_reverse_list(self):
        """ Function that reverses a linked list with a stack """
        # instantiates a stack
        stack = Part3.Stack()
        # add elements from the linked list to the stack
        while self is not None:
            stack.push(self.value)
            self = self.next
        # pops elements from the stack and add them to a linked list
        reversed_node = Node(stack.pop())
        copy_node = reversed_node
        while len(stack.stack) > 0:
            reversed_node.next = Node(stack.pop())
            reversed_node = reversed_node.next
        return copy_node

    def print(self):
        while self is not None:
            print(self.value)
            self = self.next


if __name__ == "__main__":
    node = Node(1)
    node.push(Node(5))
    node.push(Node(-10))
    node.push(Node(12))
    node.push(Node(20))
    node.print()
    print('--------------')
    reverse_list_node = node.stack_reverse_list()
    #print('--------------')
    reverse_list_node.print()

