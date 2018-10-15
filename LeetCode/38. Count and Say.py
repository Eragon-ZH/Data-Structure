"""
当然题目既然说了 n < 30， 直接写个前三十项的字典给它找更快
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        for i in range(n - 1):
            num = self.nextNum(num)
        return num

    def nextNum(self, n):
        n += 'a'
        start = 0
        strs = ""
        while start < len(n) - 1:
            current = start
            while n[current] == n[current + 1]:
                current += 1
            count = current - start + 1
            strs += str(count)
            strs += n[start]
            start += count
        return strs
