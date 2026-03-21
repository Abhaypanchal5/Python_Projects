class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def display_info(self):
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")
        print(f"Marks : {self.marks}")


stu1 = Student("Abhay", 19, [80, 83, 80, 70, 60])
stu1.display_info()
print("Average:", stu1.get_average())

stu2 = Student("Yash", 20, [60, 50, 20, 30, 40, 30])
stu2.display_info()
print("Average:", stu2.get_average)