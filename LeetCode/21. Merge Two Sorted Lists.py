# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = l1
        second = l2
        # 初始化 ans 并处理特殊情况
        if first is not None and second is not None:
            if first.val <= second.val:
                ans = ListNode(first.val)
                first = first.next
            else:
                ans = ListNode(second.val)
                second = second.next
        elif first is None and second is not None:
            return second
        elif first is not None and second is None:
            return first
        else:
            return None

        head = ans
        while first is not None and second is not None:
            if first.val <= second.val:
                ans.next = ListNode(first.val)
                ans = ans.next
                first = first.next
            else:
                ans.next = ListNode(second.val)
                ans = ans.next
                second = second.next
        if first is not None:
            ans.next = first
        if second is not None:
            ans.next = second
        return head
