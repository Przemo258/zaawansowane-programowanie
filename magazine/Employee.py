class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: str, birth_date: str, city: str, street: str,
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
