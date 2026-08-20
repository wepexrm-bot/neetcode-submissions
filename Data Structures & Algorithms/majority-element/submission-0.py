class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c ,res = 0 , 0
        for num in nums:
            if c == 0:
                res = num
            c += (1 if res == num else -1)
        return res