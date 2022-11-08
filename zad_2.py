from magazine.Library import Library
from magazine.Book import Book
from magazine.Employee import Employee
from magazine.Student import Student
from magazine.Order import Order

lib1 = Library('Katowice', 'Katowicka', '40-000', "9-21",
               "+48123456789")
lib2 = Library('Gliwice', 'Gliwice', '40-000', "7-22",
               "+48987654321")

book1 = Book(lib1, '2022-10-18T16:02:04+0000', 'Jan', 'Nowak', 69)
book2 = Book(lib1, '2021-9-18T16:02:04+0000', 'Jan', 'Nowak', 420)
book3 = Book(lib2, '2020-8-18T16:02:04+0000', 'Jan', 'Nowak', 9001)
book4 = Book(lib2, '2019-7-18T16:02:04+0000', 'Jan', 'Nowak', 360)
book5 = Book(lib2, '2018-6-18T16:02:04+0000', 'Jan', 'Nowak', 200)

emp1 = Employee('Anna', 'Kempa', '1999-1-18T16:02:04+0000',
                '1978-2-18T16:02:04+0000', 'Katowice', 'Centralna',
                '40-001', '192837465')
emp2 = Employee('Kuba', 'Rozpruwacz', '2005-6-18T16:02:04+0000',
                '1989-4-18T16:02:04+0000', 'Gliwice', 'Inna',
                '40-105', '567891234')
emp3 = Employee('Joanna', 'Nowak', '2013-1-18T16:02:04+0000',
                '1994-2-18T16:02:04+0000', 'Katowice', 'Centralna',
                '40-505', '192837465')

stud1 = Student('Kuba', [1, 2, 3, 4])
stud2 = Student('Jan', [5, 5, 5, 5])
stud3 = Student('Jacek', [4, 4, 4, 5])

order1 = Order(emp1, stud1, '2022-8-19T16:02:04+0000', )
order2 = Order(emp3, stud2, '2022-9-17T16:02:04+0000')

print(order1)
print(order2)
