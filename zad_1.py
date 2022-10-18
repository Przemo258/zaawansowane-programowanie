class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_sum = 0
        for mark in self.marks:
            marks_sum += mark
        return marks_sum / len(self.marks) > 5


s1 = Student("Jan", [1, 2, 3, 4, 5])
s2 = Student("Adam", [5, 6, 6, 6, 6])

print(s1.is_passed())
print(s2.is_passed())
