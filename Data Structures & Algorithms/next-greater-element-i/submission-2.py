class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res= []
        for i in nums1:
            nextg = -1
            for j in range(len(nums2)-1,-1,-1):
                if nums2[j] > i:
                    nextg = nums2[j]
                elif nums2[j] == i:
                    break
            res.append(nextg)
        return res