class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum = 0
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        for cnt in count.values():
            sum = sum + (cnt*(cnt-1)) // 2
            
        return sum