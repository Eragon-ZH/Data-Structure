class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        i = 0
        while i < len(nums):
            if nums[i] > target:
                break
            i += 1
        return i
