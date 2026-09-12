class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums11 = set(nums1)
        for i in nums11:
            if i in nums2:
                res.append(i)
        return res