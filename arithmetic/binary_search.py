# _*_ coding: utf-8 _*_
# 2019/3/23 16:06

__auther__ = "tanran"


def binary_search(sorted_array, val):
    if not sorted_array:
        return -1
    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1
