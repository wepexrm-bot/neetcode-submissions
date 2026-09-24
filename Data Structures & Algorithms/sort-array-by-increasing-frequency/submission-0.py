class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt_nums = Counter(nums)

        nums.sort(key = lambda n:(cnt_nums[n] , -n))

        return nums