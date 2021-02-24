# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything from your function.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []
        length = len(arr)
        
        for i in arr:
            if i == 0:
                new_arr.append(i)
                new_arr.append(0)
            else:
                new_arr.append(i)
        
        arr[:] = new_arr[:length]