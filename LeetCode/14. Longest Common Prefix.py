class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        if len(strs[0]) == 1:
            for j in strs[1:]:
                if j[0] != strs[0]:
                    return ""
            return strs[0]
        for i in range(1, len(strs[0])+1):
            for j in strs[1:]:
                if j[:i] == strs[0][:i]:
                    pass
                else:
                    return strs[0][:i-1]
        return strs[0]
