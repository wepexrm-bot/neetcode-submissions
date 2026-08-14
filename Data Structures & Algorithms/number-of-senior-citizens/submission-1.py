class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            age = int(i[-4:])
            if age > 6099:
                count += 1
        return count