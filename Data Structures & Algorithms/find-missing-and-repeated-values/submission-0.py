class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
            
        twice = miss = 0

        for num in range(1, n*n +1):
            if count[num] == 0:
                miss = num
            if count[num] == 2:
                twice = num
        
        return [twice, miss]