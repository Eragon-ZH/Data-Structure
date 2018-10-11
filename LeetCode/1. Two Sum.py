class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap.keys():
                return [hashMap.get(nums[i]), i]
            complement = target - nums[i]
            hashMap[complement] = i
