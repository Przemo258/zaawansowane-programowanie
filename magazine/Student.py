class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_sum = 0
        for mark in self.marks:
            marks_sum += mark
        return marks_sum / len(self.marks) > 5

    def __str__(self):
        return f'{self.name}'
