# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
                
        return count+1