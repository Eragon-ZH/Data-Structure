class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        ans = []
        n = len(words[0])
        length = len(words) * n
        for i in range(len(s) - length + 1):
            check_s = [s[i:i+length][j:j+n] for j in range(0, length, n)]
            for word in words:
                if word not in check_s:
                    break
                else:
                    check_s.remove(word)
            if len(check_s) == 0:
                ans.append(i)
        return ans
