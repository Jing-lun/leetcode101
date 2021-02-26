# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        longest = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
                
            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            longest = max(longest, right-left+1)
            right += 1
        return longest