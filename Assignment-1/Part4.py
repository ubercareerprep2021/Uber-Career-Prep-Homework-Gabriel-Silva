class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def push(self, node) -> None:
        """ Adds the node to the end of the list """
        while self.next != None:
            self = self.next
        self.next = node

    def pop(self):
        """ Removes the last node at the end of the linked list, returns that data """
        node_before = None
        while self.next != None:
            node_before = self
            self = self.next
        if node_before is not None:
            node_before.next = None
        return self

    def insert(self, index: int, node):
        """ Adds a single node containing data to a chosen location in the list. 
        If the index is above the size of the list, do nothing """
        # counter to check if index is bigger than linked list size
        linked_list_counter = 0
        if (type(index) == int) and (index >= 0):
            for i in range(index - 1):
                linked_list_counter += 1
                if self != None:
                    self = self.next
            
            if linked_list_counter <= index:
                if self == None:
                    self = node
                else:
                    if index == 0:
                        # inserted node points to next node of the list
                        node.next = self
                        # node is inserted at index 0 
                        self = node
                    else:    
                        # inserted node points to next node of the list
                        node.next = self.next
                        # node is inserted next to the actual node 
                        self.next = node

    def remove(self, index: int):
        """ remove/delete a single node at the index location in the list. 
        If the node doesn’t exist at the index, do nothing """
        # counter to check if index is bigger than linked list size
        linked_list_counter = 0
        node_before = self
        if (type(index) == int) and (index >= 0):
            for i in range(index):
                linked_list_counter += 1
                if self != None:
                    node_before = self
                    self = self.next
            
            if linked_list_counter <= index:
                if index == 0:
                    # removes first element
                    self = self.next
                else:    
                    # removes index element
                    node_before.next = self.next
                    self.next = None

    def element_at(self, index: int):
        """  Returns a pointer to the node at the index location in the list. 
        If the node doesn’t exist at the index, return nil/null """
        if (type(index) == int) and (index >= 0):
            for i in range(index):
                if self != None:
                    self = self.next
            if self is None:
                return None
            else:
                return self
    
    def size(self):
        """  Returns the length of the list. """
        lenght_counter = 1
        while self.next != None:
            self = self.next
            lenght_counter += 1
        return lenght_counter

    def print_list(self):
        """ Returns a string representation of the linked list """
        string_representation = ''
        while self != None:
            string_representation += str(self.value)
            self = self.next
        return string_representation

    def has_cycle(self):
        """ returns a boolean denoting whether a cycle exists """
        copy_node = self
        while copy_node.next != None: 
            memory_location_string = str(copy_node)
            print("copy ", copy_node.value)
            while self.next != None:
                self = self.next
                print("node ", self.value)
                #print("node    ", str(self))
                #print("memory ", memory_location_string)
                print(str(self) == memory_location_string)
                if str(self) == memory_location_string:
                    return True
            copy_node = copy_node.next
        return False

