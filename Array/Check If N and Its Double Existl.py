# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         length = len(arr)
#         arr = sorted(arr)
#         for i in range(length):
#             for j in range(i+1, length, 1):
#                 if arr[j] == 2*arr[i] or arr[i] == 2*arr[j]:
#                     return True
                
#         return False  

#     def checkIfExist(self, arr: List[int]) -> bool:
#         length = len(arr)
#         arr = sorted(arr)
#         # count = set()
#         for i in range(length):
#             if 2*arr[i] in arr[i+1:] or (arr[i]/2 in arr[i+1:] and arr[i]%2 ==0 ):
#                 return True
#             # count.add(arr[i])
                
#         return False
    
    def checkIfExist(self, arr: List[int]) -> bool:
        length = len(arr)
        count = set()
        for i in range(length):
            if 2*arr[i] in count or (arr[i]/2 in count and arr[i]%2 ==0 ):
                return True
            count.add(arr[i])
                
        return False    