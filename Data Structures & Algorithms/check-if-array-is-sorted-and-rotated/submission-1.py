class Solution:
    def check(self, nums: List[int]) -> bool:
        A = sorted(nums)
        B= [0] * len(A)

        for x in range(len(A)):
            for i in range(len(A)):
                B[i] = A[(i+x)% len(A)]
                if B == nums:
                    return True
        
        return False
        
        