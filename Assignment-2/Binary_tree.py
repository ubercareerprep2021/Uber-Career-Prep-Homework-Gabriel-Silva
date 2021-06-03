class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key:
            if key > self.key:
                if self.right is None:
                    node = BinaryTree(key)
                    self.right = node
                else:
                    self.right.insert(key)
            else:
                if self.left is None:
                    node = BinaryTree(key)
                    self.left = node
                else:
                    self.left.insert(key)

    def find(self, key):
        if key == self.key:
            return True

        elif key > self.key:
            if self.right is None:
                return False
            else:
                return self.right.find(key)     
        else:
            if self.left is None:
                return False
            else:
                return self.left.find(key)

                
if __name__ == "__main__":
    tree = BinaryTree(16)
    tree.insert(10)
    tree.insert(21)
    tree.insert(7)
    tree.insert(18)
    tree.insert(29)
    tree.insert(99)
    tree.insert(13)
    print(tree.find())