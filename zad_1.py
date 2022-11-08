from magazine.Student import Student

s1 = Student("Jan", [1, 2, 3, 4, 5])
s2 = Student("Adam", [5, 6, 6, 6, 6])

print(s1.is_passed())
print(s2.is_passed())
