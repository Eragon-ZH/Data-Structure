class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str is "":
            return 0
        is_nega = False
        i = 0
        if str[0] == '-':
            is_nega = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        while i < len(str):
            if (ord(str[i]) >= 48) and (ord(str[i]) <= 57):
                i += 1
            else:
                break
        if i == 0:
            return 0
        num = int(str[:i])
        if is_nega:
            num = -num
        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num
