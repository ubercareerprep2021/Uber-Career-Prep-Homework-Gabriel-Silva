class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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
        

if __name__ == "__main__":
    phonebook = ListPhoneBook()
    phonebook.insert({"name": "ABC", "phoneNumber": 1111111111})
    phonebook.insert({"name": "XYZ", "phoneNumber": 9999999999})
    phonebook.insert({"name": "DEF", "phoneNumber": 2222222222})

    print(phonebook.find("ABC"))
    print(phonebook.find("XYZ"))
    print(phonebook.find("DEF"))
    print(phonebook.find("PQR"))