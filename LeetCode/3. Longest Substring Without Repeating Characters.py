class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 1
        max_length = 0
        if len(s) == 1:
            max_length = 1
        while (l < len(s) and r <= len(s)):
            current_str = s[l:r]
            max_length = max(max_length, len(current_str))
            if (r < len(s)) and (s[r] in current_str):
                l = s.index(s[r], l) + 1
            else:
                r += 1
        return max_length
