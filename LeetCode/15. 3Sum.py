"""
O(n^2)， 先排序， 对 nums 中的每一个数字(target)，遍历数组滑动窗口寻找是否有和为零的。
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for target in range(len(nums)-2):
            # 重要优化，如果这个target已经确认过了直接跳过，不然就超时
            if target == 0 or nums[target] > nums[target-1]:
                left = target + 1
                right = len(nums) - 1
                while left < right and nums[target] * nums[right] <= 0:
                    if nums[left] + nums[right] < -nums[target]:
                        left += 1
                    elif nums[left] + nums[right] > -nums[target]:
                        right -= 1
                    else:
                        ans.append([nums[left], nums[right], nums[target]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return ans
