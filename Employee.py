class Employee:

    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}' .format(self.first_name, self.last_name)
#if u @property for something like fullname u wont have to add ()
        
    @property
    def email(self):
        return '{}.{}@gmail.com' .format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return "'{}' - '{}'".format(self.fullname, self.email)
    
    def __add__(self, other):
        return self.pay + other.pay

    @classmethod

    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod

    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        
        self.prog_lang = prog_lang
    
class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def no_of_emps(self):
        for emp in self.employees:
            print(emp.fullname())
    
    

emp1 = Employee('Gagan', 'Naidu', 50000)
emp2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-40000'
emp_str_2 = 'Jane-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

dev_1 = Developer('gagan', 'naidu', 90000, 'Python')
dev_2 = Developer('test', 'user_2', 80000, 'Java Script')

man_1 = Manager('Keanu', 'Reevs', 696969, [dev_1])

#print(emp1 + emp2)

#emp1.fullname = 'Keanu Reevs'

print(emp1.__repr__())
print(emp1.__str__())

#man_1.no_of_emps()
#man_1.add_emp(dev_2)
#man_1.no_of_emps()

#print(isinstance(man_1, Manager))
#print(issubclass(Manager, Employee))

#print(new_emp_1.fullname())
#print(new_emp_2.fullname())

#emp1.set_raise_amount(1.06)
#print(emp1.raise_amount)
#emp1.apply_raise()
#print(emp1.pay)

#print(emp1.fullname())



