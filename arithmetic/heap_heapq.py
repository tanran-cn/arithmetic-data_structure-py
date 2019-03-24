# _*_ coding: utf-8 _*_
# 2019/3/23 15:59

__auther__ = "tanran"


def heapsort_use_heapq(iterable):
    """
    使用heapq简单的实现堆排序
    :param iterable: 可迭代的对象
    :return: 堆排序的结果
    """
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items, value)

    return [heappop(items) for i in range(len(items))]
