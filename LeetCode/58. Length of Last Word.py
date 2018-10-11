class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')
        i = -1
        while words[i] == '' and -i < len(words):
            i -= 1
        return len(words[i])
