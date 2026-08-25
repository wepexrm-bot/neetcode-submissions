class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = {}
        for i in arr:
            if i not in c:
                c[i] = 0
            c[i] += 1

        for i in c:
            if c[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""