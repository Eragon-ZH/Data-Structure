class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        str_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []
        tmp = []
        if len(ans) == 0 and len(digits) >= 1:
            ans.extend(str_dict[digits[0]])
            digits = digits[1:]
        while len(digits) > 0:
            tmp.clear()
            while len(ans) > 0:
                current = ans[0]
                ans = ans[1:]
                for j in str_dict[digits[0]]:
                    tmp.append(current+j)
            ans.extend(tmp)
            digits = digits[1:]
        return ans
