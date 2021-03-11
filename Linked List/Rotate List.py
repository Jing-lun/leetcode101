# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        length = 0
        temp = head
        while temp:
            length = length+1
            temp = temp.next
        if k>length:
            k = k%length
        n = length-k
        
        if k == 0 or n == 0:
            return head
        print(n)
        curr = head
        p1head, p2head = ListNode(0), None
        p1 = p1head
        while n:
            n -= 1
            p1.next = curr
            curr = curr.next
            p1 = p1.next      
        
        p1.next = None
        p2head = curr
        p2 = p2head
        print(p2head)
        while p2.next:
            p2 = p2.next
        p2.next = p1head.next
        print(p2head)
        return p2head
        
     
        