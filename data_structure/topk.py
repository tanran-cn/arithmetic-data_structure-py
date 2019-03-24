# _*_ coding: utf-8 _*_
# 2019/3/24 15:05
import heapq

__auther__ = "tanran"


class TopK:
    """
    获取大量元素 topK 大个元素，固定内存
    思路：
    1、先放入元素前k个建立最小堆
    2、迭代剩余元素：
        如果当前元素小于堆顶元素，跳过该元素
        否则替换堆顶元素为当前元素，并重新调整堆
    """

    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap


def test():
    import random
    i = list(range(1000))
    random.shuffle(i)
    _ = TopK(i, 10)
    print(_.get_topk())

test()