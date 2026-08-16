class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c , res = 0 , 0
        for i in nums:
            if i == 0:
                res = max(c,res)
                c = 0
            else:
                c += 1
        return max(c, res)