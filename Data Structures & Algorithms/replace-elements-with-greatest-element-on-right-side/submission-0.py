class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax = -1
        for i in range(len(arr)-1,-1,-1):
            newMax = max(rmax, arr[i])
            arr[i] = rmax
            rmax=newMax
        return arr