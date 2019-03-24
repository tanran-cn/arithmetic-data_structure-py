# _*_ coding: utf-8 _*_
# 2019/3/23 14:11

__auther__ = "tanran"
"""
Partition:选择基准分割数组为两个子数组，小于基准和大于基准的

对两个子数组分别快排

合并结果
"""


def quicksort(array):
    # 递归出口
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index+1:] if i <= pivot]
        great_part = [i for i in array[pivot_index+1:] if i > pivot]
        return quicksort(less_part) + [pivot] + quicksort(great_part)


def test_quicksort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    assert quicksort(ll) == sorted(ll)
    print(quicksort(ll))

if __name__ == '__main__':
    test_quicksort()
