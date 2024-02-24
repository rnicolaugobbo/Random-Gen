import random
from matplotlib import pyplot as plt
import hashlib
from datetime import datetime, timedelta

def select_number():
    selected_number = random.randint(0, 9)
    return selected_number

def hash(selected_number):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(str(selected_number).encode())
    hash_code = int(sha256_hash.hexdigest(), 16)
    return hash_code

def compressor(hash_code):
    hash_comp = hash_code % 997
    return hash_comp

def save_results(results_list):
    numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0

    for item in results_list:
        if item == numbers_list[0]:
            count_0 += 1
        if item == numbers_list[1]:
            count_1 += 1
        if item == numbers_list[2]:
            count_2 += 1
        if item == numbers_list[3]:
            count_3 += 1
        if item == numbers_list[4]:
            count_4 += 1
        if item == numbers_list[5]:
            count_5 += 1
        if item == numbers_list[6]:
            count_6 += 1
        if item == numbers_list[7]:
            count_7 += 1
        if item == numbers_list[8]:
            count_8 += 1
        if item == numbers_list[9]:
            count_9 += 1
    results_dict = \
        {"Number 0:": count_0, 
         "Number 1:": count_1, 
         "Number 2:": count_2, 
         "Number 3:": count_3, 
         "Number 4:": count_4, 
         "Number 5:": count_5, 
         "Number 6:": count_6, 
         "Number 7:": count_7, 
         "Number 8:": count_8, 
         "Number 9:": count_9}
    return results_dict

def plot(results_dict):
    plt.bar(results_dict.keys(), results_dict.values(), width = 0.5)
    plt.show()

def menu():
    results = []
    saved_values = []
    start_time = datetime.now()
    duration = timedelta(milliseconds = 1)
    end_time = start_time + duration

    while datetime.now() < end_time:

        # print("Press any key to shuffle the list of fruits.")
        # str(input())

        selected_number = select_number()
        print("The selected number was: " + str(selected_number))
        hash_number = hash(selected_number)
        hash_comp = compressor(hash_number)
        results.append(selected_number)

        start_time += timedelta(microseconds = 1)

    saved_results = save_results(results)
    for value in  saved_results.values():
        saved_values.append(value)
    print(saved_values)
    plot(saved_results)

menu()