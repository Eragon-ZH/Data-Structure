"""
用两个相隔为 n 的指针，只遍历一遍链表
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left = head
        right = head
        # right 先走 n 步
        for i in range(n):
            if right.next is not None:
                right = right.next
            else:
                # 链表只有一个结点
                if head.next is None:
                    return
                # 删除的是头结点
                else:
                    head = head.next
                    return head
        # right 走到尾， left 指向的就是要删除的结点
        while right.next is not None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
