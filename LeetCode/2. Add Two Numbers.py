# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = self.chainToNumber(l1) + self.chainToNumber(l2)
        return self.numberToChain(sum)

    def chainToNumber(self, chain):
        num = chain.val
        digit = 1
        while chain.next is not None:
            chain = chain.next
            digit *= 10
            num += chain.val * digit
        return num

    def numberToChain(self, num):
        chain = ListNode(num%10)
        current = chain
        num = num // 10
        while num != 0:
            current.next = ListNode(num%10)
            current = current.next
            num = num // 10
        return chain
