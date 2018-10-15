class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if '(' not in s:
            return 0
        s = s[s.index('('):]
        max_length = 0
        stack = []
        start = 0
        while start < len(s):
            current = start
            stack = []
            while current < len(s):
                if s[current] == '(':
                    stack.append(current)
                else:
                    if len(stack) > 0:
                        stack.pop()
                        if len(stack) == 0:
                            max_length = max(max_length, current - start + 1)
                        else:
                            max_length = max(max_length, current - stack[-1])
                    else:
                        start = current
                        break
                current += 1
            start += 1
            if current == len(s):
                return max_length
        return max_length
