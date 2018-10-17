class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = []
        for i in range(len(nums)):
            nums1.append(nums[i] + i)
        max_jump = 0
        for i in range(len(nums1)):
            max_jump = max(max_jump, nums1[i])
            if max_jump >= len(nums1) - 1:
                return True
            if nums[i] == 0:
                if max_jump <= i:
                    return False
        return True
