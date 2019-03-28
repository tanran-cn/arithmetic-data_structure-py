# _*_ coding: utf-8 _*_
# 2019/3/28 16:01

__auther__ = "tanran"
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums: list) -> list:
        result_list = []
        for i in range(len(nums)):
            temp_num = nums[i]
            temp_list1 =nums[i+1:]
            for n in range(len(temp_list1)):
                temp_num2 = temp_list1[n]
                temp_list2 = temp_list1[n+1:]
                target = 0 - (temp_num + temp_num2)
                if target in temp_list2:
                    temp_result = [
                        temp_num,
                        temp_num2,
                        target
                    ]
                    result_list.append(temp_result)
        res_list = []
        for res in result_list:
            res.sort()
            if res in res_list:
                pass
            else:
                res_list.append(res)

        return res_list


class Solution2:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return res


s = Solution()
s.threeSum([-1,0,1,2,-1,-4])