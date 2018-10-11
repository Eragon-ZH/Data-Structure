class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 不能
        string = str(x)
        rev = string[::-1]
        return string == rev
