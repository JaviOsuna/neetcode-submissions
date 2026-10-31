class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0) # dequeue
                sandwiches.pop(0)
                count = 0
            else:
                aux = students.pop(0)
                students.append(aux) #enqueue
                count += 1

        return len(students)