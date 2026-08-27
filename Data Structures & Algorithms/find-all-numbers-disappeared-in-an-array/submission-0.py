class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        store = set()
        for i in range(1 , n+1):
            store.add(i)
        
        for num in nums:
            store.discard(num)

        return list(store)