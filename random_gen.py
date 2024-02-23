import random
from db import fruit_db, shuffle_list

def select_item(fruit_list):
    shuffled_list = shuffle_list(fruit_list)
    r_num = random.randint(0, 9)
    selected_item = shuffled_list[r_num]
    return selected_item

def hash(selected_item):
    item_bytes = selected_item.encode()
    hash_code = sum(item_bytes)
    return hash_code

def compressor(hash_code):
    hash_comp = hash_code % 10
    return hash_comp

def menu():
    # print("Press any key to shuffle the list of fruits.")
    # str(input())

    shuffled_list = shuffle_list(fruit_db)
    print("This is the new list:\n")
    print(shuffled_list)
    print("Selecting random item from list...")
    selected_item = select_item(shuffled_list)
    print("The selected item was: " + str(selected_item))
    hash_item = hash(selected_item)
    hash_comp = compressor(hash_item)
    print(shuffled_list[hash_comp])

menu()