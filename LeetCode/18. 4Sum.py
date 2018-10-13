"""
思路同 3Sum，只是把当前检查的数字从一个变成了两个，再滑动窗口进行检查
第一次通过了，后面提交都超时
时间复杂度O(n^3)
"""
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for target_1 in range(len(nums)-3):
            for target_2 in range(target_1+1, len(nums)-2):
                if target_1 == 0 or nums[target_1] > nums[target_1-1]:
                    left = target_2 + 1
                    right = len(nums) - 1
                    while left < right:
                        sums = nums[target_1] + nums[target_2] + \
                                   nums[left] + nums[right]
                        if sums < target:
                            left += 1
                        elif sums > target:
                            right -= 1
                        else:
                            four_nums = [nums[target_1], nums[target_2],
                                        nums[left], nums[right]]
                            if four_nums not in ans:
                                ans.append(four_nums)
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left-1]:
                                left += 1
                            while left < right and nums[right] == nums[right+1]:
                                right -= 1
        return ans
