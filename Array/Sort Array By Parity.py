# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        count = 0
        B = len(A) * [0]
        for i in range(len(A)):
            if A[i] % 2 == 0:
                B[count] = A[i]
                count += 1
        
        for i in range(len(A)):
            if A[i] % 2 != 0:
                B[count] = A[i]
                count += 1 
                
        return B

    def sortArrayByParity2(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A