import time
from datetime import datetime


def bubble_sort(list):
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        nxt_element = list[i]

        while (list[j] > nxt_element) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = nxt_element


def is_sorted(lst):
    previous = lst[0]
    for element in lst[1:]:
        if element < previous:
            return False
        previous = element

    return True


def measure_sort_time(sorting_function, list):
    start = datetime.now()
    sorting_function(list)
    end = datetime.now()
    dif = end - start
    return dif


if __name__ == '__main__':
    my_list = [1, 5, 43, 7, 432, 675, 3, 2]

    first = measure_sort_time(bubble_sort, my_list)
    print(f"First sorting took {first.total_seconds():0.20f} s")

    second = measure_sort_time(insertion_sort, my_list)
    print(f"Second sorting took {second.total_seconds():0.20f} s")

    print(is_sorted(my_list))

