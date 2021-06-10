import Binary_tree_phonebook as tree_phonebook
import csv, time

def insert_list() -> list:
    start_time = time.time()
    first_node = True
    with open('/home/gabriel/Repositories/Uber-Career-Prep-Homework-Gabriel-Silva/Assignment-2/data.csv', 'r') as file:
        all_phone = csv.reader(file)
        phone_dict = {}
        for row in all_phone:
            phone_dict = {}
            phone_dict['name'] = row[0]
            phone_dict['phoneNumber'] = int(row[1])
            # print("AAAAAAAAAAAA\n")
            # print("AAAAAAAAAAAA\n")
            # print("AAAAAAAAAAAA\n")
            # print("AAAAAAAAAAAA\n")
            # print("AAAAAAAAAAAA\n")
            # print(time.time() - start_time)
            if first_node:
                phonebook = tree_phonebook.BinarySeaerchTreePhoneBook(phone_dict)
                first_node = False
            else:
                phonebook.insert(phone_dict)
    
    run_time = time.time() - start_time
    if phonebook.size() != 1000000:
        print("Error, phonebook size is not 1000000")
        return
    print("Insert took {:.0f} miliseconds.".format(run_time * 1000))
    print("The size of the phonebook is {}.".format(phonebook.size()))
    return phonebook

def find(phonebook):
    start_time = time.time()    
    find_counter = 0
    with open('/home/gabriel/Repositories/Uber-Career-Prep-Homework-Gabriel-Silva/Assignment-2/search.csv', mode='r') as search_file:
        search = csv.reader(search_file)
        for row in search:
            phone = phonebook.find(row[0])
            if phone == -1:
                print("Error finding number")
                return
            else:
                find_counter += 1

    run_time = time.time() - start_time
    print("find() was called {}.".format(find_counter))
    print("Search took {:.0f} miliseconds.".format(run_time * 1000))
    

if __name__ == '__main__':
    # insert took 25598 and 30348 miliseconds
    phonebook = insert_list()
    # find took between 15 and 33 miliseconds in 5 runs
    find(phonebook)

    # 3: there is a difference in the running times for the two implementations 
    # because it is easier to insert an item in a list and it is faster to find
    # one in a binary tree, because in a tree you don't have to go past most of
    # the itens, while in the list you need it.