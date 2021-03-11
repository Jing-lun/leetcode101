# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ansHead = ListNode(0)
        ans = ansHead
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            if val > 9:
                val = val%10
                carry = 1
            else:
                carry = 0
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            ans.next = ListNode(val)
            ans = ans.next
        return ansHead.next