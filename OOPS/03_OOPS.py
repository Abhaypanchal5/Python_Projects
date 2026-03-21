class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value          # ✅ replace, not add
        else:
            print("Salary must be greater than 0.")

    def display(self):
        print(f"Name: {self.name}, Salary: ₹{self.__salary}")


emp1 = Employee('Abhay', 60000)

print(emp1.salary)       # triggers getter → 60000

emp1.salary = 80000      # triggers setter → valid, updates
emp1.display()

emp1.salary = -5000      # triggers setter → invalid, prints warning
emp1.display()           # salary stays 80000