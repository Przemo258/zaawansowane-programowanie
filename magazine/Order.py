from magazine.Employee import Employee
from magazine.Student import Student


class Order:
    def __init__(self, employee: Employee, student: Student, order_date: str):
        self.order_date = order_date
        self.student = student
        self.employee = employee

    def __str__(self):
        return f'This is an order from {self.student}' \
               f' realized by {self.employee}'
