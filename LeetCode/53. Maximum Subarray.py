class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        if max_sum <= 0:
            return max_sum
        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                break
            i += 1
        nums = nums[i:]
        left = 0
        right = 1
        current_sum = nums[0]
        while left < len(nums) and right < len(nums):
            current_sum += nums[right]
            if  current_sum <= 0:
                left = right + 1
                right = left
                current_sum = 0
            else:
                right += 1
                max_sum = max(current_sum, max_sum)
        return max_sum
