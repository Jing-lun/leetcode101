# Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        prev_node = head
        next_node = head.next
        while True:
            if next_node.val >= insertVal >= prev_node.val:
                # print(1)
                break
            if prev_node.val > next_node.val and (insertVal > prev_node.val or insertVal < next_node.val):
                # print(2)
                break
            prev_node = next_node
            next_node = next_node.next
            if prev_node == head:
                # print(3)
                break
        new_node = Node(insertVal)
        prev_node.next = new_node
        new_node.next = next_node
        return head