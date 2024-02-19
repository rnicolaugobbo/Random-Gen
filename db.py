import random

fruit_db = ["apple", "banana", "orange", "grape", "strawberry", "pear", "lime", "nectarine", "pineapple", "avocado"]

def shuffle_list(list):
    shuffled_list = []
    for item in list:
        shuffled_list.append(item)
    random.shuffle(shuffled_list)
    return shuffled_list

s_list = shuffle_list(fruit_db)
print(s_list)