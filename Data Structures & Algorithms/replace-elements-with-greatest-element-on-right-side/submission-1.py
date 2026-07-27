class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax = -1
        ans = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            ans[i] = rmax
            rmax= max(arr[i], rmax)
        return ans