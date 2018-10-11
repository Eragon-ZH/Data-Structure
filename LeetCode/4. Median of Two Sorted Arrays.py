class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 直接sort时间复杂度为nlog(m+n)
        sum_nums = nums1 + nums2
        sum_nums = sorted(sum_nums)
        if len(sum_nums) % 2 == 0:
            print(len(sum_nums))
            a = sum_nums[len(sum_nums) // 2 - 1]
            b = sum_nums[len(sum_nums) // 2]
            return (a + b) / 2
        else:
            return sum_nums[len(sum_nums) // 2]
