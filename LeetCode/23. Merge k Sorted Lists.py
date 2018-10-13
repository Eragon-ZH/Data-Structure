"""
直接将所有值 sort 然后拼一个新列表= =
更好的解法是分治法和最小堆
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = []
        for i in lists:
            while i is not None:
                vals.append(i.val)
                i = i.next
        vals.sort()
        if len(vals) > 0:
            ans = ListNode(vals[0])
            vals = vals[1:]
            head = ans
        else:
            return None
        while len(vals) > 0:
            ans.next = ListNode(vals[0])
            vals = vals[1:]
            ans = ans.next
        return head
