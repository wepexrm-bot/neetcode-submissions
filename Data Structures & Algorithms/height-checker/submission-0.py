class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expect[i]:
                count += 1
        return count