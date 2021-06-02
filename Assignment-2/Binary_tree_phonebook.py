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
            
class ListPhoneBook:
    def __init__(self):
        self.list = list()

    def size(self) -> int:
        return len(self.list)

    def insert(self, name_phone_dictionary: dict):
        self.list.append(name_phone_dictionary)

    def find(self, name) -> int:
        for item in self.list:
            if item.get("name") == name:
                return item.get("phoneNumber")
        return -1


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
    phonebook = ListPhoneBook()
    phonebook.insert({"name": "ABC", "phoneNumber": 1111111111})
    phonebook.insert({"name": "XYZ", "phoneNumber": 9999999999})
    phonebook.insert({"name": "DEF", "phoneNumber": 2222222222})

    print(phonebook.find("ABC"))
    print(phonebook.find("XYZ"))
    print(phonebook.find("DEF"))
    print(phonebook.find("PQR"))