class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library {self.city} on the {self.street} street'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.phone = phone
        self.zip_code = zip_code
        self.street = street
        self.city = city
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name} from {self.city}'


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'This is a book by {self.author_name} {self.author_surname} published {self.publication_date} from {self.library}'


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


class Order:
    def __init__(self, employee: Employee, student: Student, order_date: str):
        self.order_date = order_date
        self.student = student
        self.employee = employee

    def __str__(self):
        return f'This is an order from {self.student} realized by {self.employee}'


lib1 = Library('Katowice', 'Katowicka', '40-000', "9-21", "+48123456789")
lib2 = Library('Gliwice', 'Gliwice', '40-000', "7-22", "+48987654321")

book1 = Book(lib1, '2022-10-18T16:02:04+0000', 'Jan', 'Nowak', 69)
book2 = Book(lib1, '2021-9-18T16:02:04+0000', 'Jan', 'Nowak', 420)
book3 = Book(lib2, '2020-8-18T16:02:04+0000', 'Jan', 'Nowak', 9001)
book4 = Book(lib2, '2019-7-18T16:02:04+0000', 'Jan', 'Nowak', 360)
book5 = Book(lib2, '2018-6-18T16:02:04+0000', 'Jan', 'Nowak', 200)

emp1 = Employee('Anna', 'Kempa', '1999-1-18T16:02:04+0000', '1978-2-18T16:02:04+0000', 'Katowice', 'Centralna',
                '40-001', '192837465')
emp2 = Employee('Kuba', 'Rozpruwacz', '2005-6-18T16:02:04+0000', '1989-4-18T16:02:04+0000', 'Gliwice', 'Inna',
                '40-105', '567891234')
emp3 = Employee('Joanna', 'Nowak', '2013-1-18T16:02:04+0000', '1994-2-18T16:02:04+0000', 'Katowice', 'Centralna',
                '40-505', '192837465')

stud1 = Student('Kuba', [1, 2, 3, 4])
stud2 = Student('Jan', [5, 5, 5, 5])
stud3 = Student('Jacek', [4, 4, 4, 5])

order1 = Order(emp1, stud1, '2022-8-19T16:02:04+0000', )
order2 = Order(emp3, stud2, '2022-9-17T16:02:04+0000')

print(order1)
print(order2)
