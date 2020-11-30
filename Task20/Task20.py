import time
from typing import List, Callable


def first_sorting(lst: List):
    lst.sort()


def second_sorting(lst: List):
    lst.sort(reverse=True)


def measure_sort_time(sorting_function: Callable[[List], None], lst: List):
    start = time.time()
    sorting_function(lst)
    end = time.time()
    dif = end - start
    return dif


if __name__ == '__main__':
    my_arr = [1, 5, 43, 7, 432, 675, 3, 2]

    first_run_time = measure_sort_time(first_sorting, my_arr)
    print(f"First sorting took {first_run_time:0.9f} s")

    second_run_time = measure_sort_time(second_sorting, my_arr)
    print(f"Second sorting took {second_run_time:0.9f} s")

