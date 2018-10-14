"""
时间复杂度 O(n)，开了一个不知道多大的数组
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        n = max(nums)
        shows = [False] * n
        for i in nums:
            if i - 1 >= 0:
                shows[i - 1] = True
        for i in range(len(shows)):
            if shows[i] == False:
                return i + 1
        return len(shows) + 1
