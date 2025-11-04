class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def manage(self):
        print (f"I'm Manager, my name is {self.name}, and my monthly salary {self.salary} dollar")

class Developer(Employee):
    def write_code(self):
        print (f"I'm Developer, my name is {self.name}, and my monthly salary {self.salary} dollar")

a = Developer('Eli', 8000)
b = Manager('Avi', 7000)

a.write_code()
b.manage()

