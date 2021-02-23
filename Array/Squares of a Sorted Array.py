#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        new_list = length * [0]
        head = 0
        rear = length -1
        count = 0
        
        while head <= rear:
            count = count + 1
            if abs(nums[head])>abs(nums[rear]):
                new_list[length-count] = nums[head] * nums[head]
                head = head + 1
            else:
                new_list[length-count] = nums[rear] * nums[rear]
                rear = rear-1
                
        return new_list