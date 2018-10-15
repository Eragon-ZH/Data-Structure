"""
1. 从后往前找第一个不是升序的位置i
2. 从i往后找比nums[i]大的数字中最小的数并与nums[i]交换
3. 原地对nums[i+1:]进行排序
因为后半部分肯定是降序，所以直接翻转就行
用sorted()超过了 3%， 直接翻转超过了 99.3%
注意：要用 >= 和 <=
例：
6 5 4 8 7 5 1
从后往前第一个不是升序的是 4
4 后比 4 大的数字最小的是 5
交换，此时原数组变成了 6 5 5 8 7 4 1
对数组后四个数翻转 6 5 5 1 4 7 8
"""
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            nums.reverse()
            return
        min_big = float('inf')
        min_big_index = i
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i] and nums[j] <= min_big:
                min_big_index = j
                min_big = nums[j]
        nums[i], nums[min_big_index] = nums[min_big_index], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
