# _*_ coding: utf-8 _*_
# 2019/3/23 14:19


__auther__ = "tanran"


def merge_sorted_list(sorted_a, sorted_b):
    """
    合并两个有序数列
    :param sorted_a:有序数列a
    :param sorted_b: 有序数列b
    :return: 合并后的有序数列
    """
    length_a, length_b = len(sorted_a), len(sorted_b)
    index_a = index_b = 0
    new_sorted = []
    while index_a < length_a and index_b < length_b:
        # 合并
        if sorted_a[index_a] <= sorted_b[index_b]:
            new_sorted.append(sorted_a[index_a])
            index_a += 1
        else:
            new_sorted.append(sorted_b[index_b])
            index_b += 1
    # 处理剩余
    if index_a < length_a:
        new_sorted.extend(sorted_a[index_a:])
    else:
        new_sorted.extend(sorted_b[index_b:])
    return new_sorted


def merge_sort(seq):
    """
    合并排序递归部分，不断递归拆分为最小，之后开始合并
    :param seq: 数列
    :return: 排序好的数列
    """
    if len(seq) <= 1:
        return seq
    else:
        mid = len(seq)//2
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
        new_seq = merge_sorted_list(left_half, right_half)
        return new_seq


def merge_sorted_list_text():
    a = [1, 2, 5]
    b = [4, 6, 8]
    print(merge_sorted_list(a, b))


def merge_sort_test():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    assert merge_sort(ll) == sorted(ll)
    print(ll)


if __name__ == '__main__':
    # merge_sorted_list_text()
    merge_sort_test()
