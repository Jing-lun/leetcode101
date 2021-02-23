# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        max_count = 0
        for i in range(length):
            if nums[i] == 1:
                count = count + 1
            else:
                max_count = max(max_count, count)
                count = 0
        
        return max(max_count, count)