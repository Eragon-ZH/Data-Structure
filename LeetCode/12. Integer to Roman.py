class Solution:
    def __init__(self):
        self.alpha = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC",
                        50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        self.roma = ""

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in n:
            self.addStr(num, i)
            num = num % i
        return self.roma

    def addStr(self, num, n):
        self.roma += num // n * self.alpha[n]
