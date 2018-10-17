"""
借用了 56. Merge Intervals 的代码
"""
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        intervals = []
        for i in timeSeries:
            intervals.append([i, i+duration])
        ans_list = []
        ans_list.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans_list[-1][-1]:
                if ans_list[-1][-1] < intervals[i][-1]:
                    ans_list[-1][-1] = intervals[i][-1]
            else:
                ans_list.append(intervals[i])
        ans = 0
        for i in ans_list:
            ans += (i[-1] - i[0])
        return ans
