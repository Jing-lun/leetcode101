#Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            if len(list(str(nums[i])))%2 == 0:
                count = count + 1
        
        
        return count