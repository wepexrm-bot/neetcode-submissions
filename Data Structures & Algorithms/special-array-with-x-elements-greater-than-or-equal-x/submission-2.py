class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for num in nums:
            index = min(num, len(nums))
            count[index] += 1

        total_right = 0
        for i in range(len(nums), -1, -1):
            total_right += count[i]
            if i == total_right:
                return total_right
        return -1