class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        while len(s) > 0:
            if s[0] in "([{":
                stack.append(s[0])
            elif s[0] in ")]}":
                if len(stack) > 0 and stack.pop() == brackets[s[0]]:
                    pass
                else:
                    return False
            s = s[1:]
        if len(stack) == 0:
            return True
        else:
            return False
