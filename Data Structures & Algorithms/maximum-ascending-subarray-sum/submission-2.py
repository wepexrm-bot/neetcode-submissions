class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = cursum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                cursum = 0
            cursum += nums[i]
            res = max(res , cursum)
        return res
