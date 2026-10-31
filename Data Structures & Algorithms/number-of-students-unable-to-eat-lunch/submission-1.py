class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = {
            0: students.count(0),
            1: students.count(1)
        }
        
        for s in sandwiches:
            if counts[s] > 0:
                counts[s] -= 1
            else:
                break

        return counts[0] + counts[1]