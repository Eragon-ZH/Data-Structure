class Solution:
    def __init__(self):
        self.alpha = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90,
                      "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        self.num = 0

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma = ["M", "CM", "D", "CD", "C", "XC", "L",
                "XL", "X", "IX", "V", "IV", "I"]
        while len(s) > 0:
            if s[:2] in roma:
                self.addNum(s[:2])
                s = s[2:]
            elif s[:1] in roma:
                self.addNum(s[:1])
                s = s[1:]
        return self.num

    def addNum(self, i):
        self.num += self.alpha[i]
