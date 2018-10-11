class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closet = float('inf')
        for current in range(len(nums)-2):
            if current == 0 or nums[current] > nums[current-1]:
                left = current + 1
                right = len(nums) - 1
                while left < right:
                    sum_num = nums[current] + nums[left] + nums[right]
                    if abs(target - sum_num) < closet:
                        closet = abs(target - sum_num)
                        closet_sum = sum_num
                    if sum_num < target:
                        left += 1
                    elif sum_num > target:
                        right -= 1
                    else:
                        return sum_num
        return closet_sum
