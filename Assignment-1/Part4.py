class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def push(self, value: int) -> None:
        """ Adds the node to the end of the list """
        node_to_add = Node(value)
        while self.next != None:
            self = self.next
        self.next = node_to_add

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