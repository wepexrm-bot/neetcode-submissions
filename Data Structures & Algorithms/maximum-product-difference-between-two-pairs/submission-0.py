class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_prodiff = (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        return max_prodiff