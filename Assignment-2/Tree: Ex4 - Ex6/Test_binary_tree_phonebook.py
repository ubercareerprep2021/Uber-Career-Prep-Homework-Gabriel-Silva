import Binary_tree_phonebook as t, unittest

class TestPart1(unittest.TestCase):

    def test_binarytree_insert_ex1(self):
        phonebook = t.BinarySeaerchTreePhoneBook({"name": "ABC", "phoneNumber": 1111111111})
        phonebook.insert({"name": "XYZ", "phoneNumber": 9999999999})
        phonebook.insert({"name": "DEF", "phoneNumber": 2222222222})

        self.assertEqual(phonebook.find("ABC"), 1111111111)
        self.assertEqual(phonebook.find("XYZ"), 9999999999)
        self.assertEqual(phonebook.size(), 3)
        self.assertEqual(phonebook.find("PQR"), -1)

if __name__ == '__main__':
    unittest.main()