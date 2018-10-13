class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.findAns('', n, 0, 0)
        return self.ans

    def findAns(self, s, n, left, right):
        if len(s) == 2 * n:
            self.ans.append(s)
        if left < n:
            self.findAns(s+'(', n, left+1, right)
        if right < left:
            self.findAns(s+')', n, left, right+1)
        
