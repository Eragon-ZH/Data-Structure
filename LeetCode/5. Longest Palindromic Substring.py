class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_str = ""
        for i in range(len(s)):
            current_str = s[i]
            k = 1
            # 奇数回文
            while (i - k >= 0) and (i + k < len(s)):
                if (s[i-k] == s[i+k]):
                    current_str = s[i-k:i+k+1]
                    k += 1
                else:
                    break
            if len(current_str) > max_length:
                max_length = len(current_str)
                max_str = current_str

            current_str = s[i]
            k = 0
            # 偶数回文
            while (i - k >= 0) and (i + k + 1 < len(s)):
                if (s[i-k]) == s[i+k+1]:
                    current_str = s[i-k:i+k+2]
                    k += 1
                else:
                    break
            if len(current_str) > max_length:
                max_length = len(current_str)
                max_str = current_str
        return max_str
