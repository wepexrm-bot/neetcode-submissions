class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        countdec = countinc = 1
        for i in range(1 , len(nums)):
            if nums[i] >= nums[i-1]:
                countdec += 1
            if nums[i] <= nums[i-1]:
                countinc += 1
        return countdec == len(nums) or countinc == len(nums)