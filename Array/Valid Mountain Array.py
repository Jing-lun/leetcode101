# Given an array of integers arr, return true if and only if it is a valid mountain array.
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_num = max(arr)
        print(max_num)
        max_index = 0

        for i in range(len(arr)):
            if arr[i] == max_num:
                max_index = i
                if max_index == 0 or max_index == len(arr)-1:
                    return False    
            if i+1 < len(arr) and arr[i] == arr[i+1]:
                return False
            if arr[i] < max_num and max_index == 0 and arr[i+1] < arr[i]:
                return False
            if i+1 < len(arr) and max_index > 0 and arr[i+1] > arr[i]:
                return False
        
        return True
                