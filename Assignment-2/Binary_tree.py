class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def print(self):
        print(self.key)
        if self.right is not None:
            self.right.print()
        if self.left is not None:
            self.left.print()
            

def insert(root, key):
    if key > root.key:
        if root.right is None:
            node = Node(key)
            root.right = node
        else:
            insert(root.right, key)
    else:
        if root.left is None:
            node = Node(key)
            root.left = node
        else:
            insert(root.left, key)

def find(root, key):
    if key == root.key:
        return True

    elif key > root.key:
        if root.right is None:
            return False
        else:
            return find(root.right, key)     
    else:
        if root.left is None:
            return False
        else:
            return find(root.left, key)
        

if __name__ == "__main__":
    tree = Node(16)
    insert(tree, 10)
    insert(tree, 21)
    insert(tree, 7)
    insert(tree, 18)
    insert(tree, 29)
    insert(tree, 99)
    insert(tree, 13)
    for i in range(9, 100):
        result = find(tree, i)
        print(i, result)