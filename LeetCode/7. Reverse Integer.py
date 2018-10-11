class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # python的//是向下取整不是整数，因此-1//10=-1
        is_nega = False
        rev = 0
        if x < 0:
            is_nega = True
            x = -x
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        if is_nega:
            rev = -rev
        if (rev >= -2**31) and (rev <= 2**31):
            return rev
        else:
            return 0
