class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt_students = Counter(students)
        for s in sandwiches:
            if cnt_students[s] > 0:
                res = res -1 
                cnt_students[s] -= 1
            else: 
                break
        return res