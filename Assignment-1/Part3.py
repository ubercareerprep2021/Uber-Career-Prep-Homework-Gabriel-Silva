class Stack:
    def __init__(self):
        self.stack = []

    def push(self, integer: int):
        """ Pushes integer to the top of the stack """
        
        if type(integer) != int:
            return('Stack only accepts integer values')
        else:
            self.stack = self.stack + [integer] 

    def pop(self):
        """ Removes what is on the top of the stack, and returns that value to the caller """
        if len(self.stack) < 1 :
            return None
        else:
            # last element of the stack
            return_value = self.stack[-1]
            # gets the index before the last element
            index_before_last_element = len(self.stack) - 1 
            # removes the last element from the list by index
            self.stack = self.stack[:index_before_last_element] 
            return return_value

    def top(self):
        """ Looks at the top value, and returns it. Does not manipulate the stack """
        if len(self.stack) < 1 :
            return None
        else:
            # returns the last element of the list
            return self.stack[-1]

    def isEmpty(self):
        """ Returns True or False if the stack is Empty or not, respectively """
        if len(self.stack) < 1 :
            return True
        else:
            return False

    def size(self):
        """ Returns an integer value with the count of elements in the stack """
        if len(self.stack) < 1 :
            return 0
        else:
            return len(self.stack)


class Queue:
    """ Queue that handles any type of object """
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        """ adds an item to the queue """
        self.queue = self.queue + [element] 

    def dequeue(self):
        """ removes an item from the queue """
        if len(self.queue) < 1 :
            pass
        else:
            # removes the first element from the list by index
            self.queue = self.queue[1:] 

    def rear(self):
        """ returns the item at the end of the queue """
        if len(self.queue) < 1 :
            return None
        else:
            # returns the last element of the queue
            return self.queue[-1]

    def front(self):
        """ returns the item at the front of the queue """
        if len(self.queue) < 1 :
            return None
        else:
            # returns the first element of the queue
            return self.queue[0]

    def size(self):
        """ returns the size of the queue """
        if len(self.queue) < 1 :
            return 0
        else:
            return len(self.queue)

    def isEmpty(self):
        """ returns whether or not the queue is empty """
        if len(self.queue) < 1 :
            return True
        else:
            return False

