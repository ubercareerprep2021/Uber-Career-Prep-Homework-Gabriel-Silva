class BinarySeaerchTreePhoneBook:
    def __init__(self, number_phone_dict):
        self.name = number_phone_dict['name']
        self.phone_number = number_phone_dict["phoneNumber"]
        self.left = None
        self.right = None

    def size(self) -> int:
        counter = 1
        if self.left:
            counter += self.left.size() 
        if self.right:
            counter += self.right.size()
        return counter

    def insert(self, number_phone_dict):
        if self.phone_number:
            node = BinarySeaerchTreePhoneBook(number_phone_dict)
            if node.phone_number > self.phone_number:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(number_phone_dict)
            else:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(number_phone_dict)

    def find(self, name):
        if name == self.name:
            return self.phone_number

        elif name > self.name:
            if self.right is None:
                return -1
            else:
                return self.right.find(name)     
        else:
            if self.left is None:
                return -1
            else:
                return self.left.find(name)


if __name__ == "__main__":
    tree = BinarySeaerchTreePhoneBook({"name": "ABC", "phoneNumber": 1111111111})
    tree.insert({"name": "XYZ", "phoneNumber": 9999999999})
    tree.insert({"name": "DEF", "phoneNumber": 2222222222})

    print(tree.find("ABC"))
    print(tree.size())