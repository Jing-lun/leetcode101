# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):            
        l = head
        r = head
        count = 0
        while r is not None:
            r = r.next
            count += 1
            if count > n+1:
                l = l.next
                # print(l)
        if count == n:
            return head.next
        else:
            l.next = l.next.next
            return head