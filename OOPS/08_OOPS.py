class Student:
    student_count = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.student_count += 1      # ✅ count every new student

    @classmethod
    def get_count(cls):                 # ✅ cls not self
        return cls.student_count

    @staticmethod
    def is_passing(marks):              # ✅ no self, no cls
        return sum(marks) / len(marks) >= 40

    def display(self):
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")


s1 = Student("Abhay", [80, 75, 90])
s2 = Student("Yash", [30, 25, 20])
s3 = Student("Raj", [50, 60, 55])

print(Student.get_count())              # 3
print(Student.is_passing([80, 75, 90])) # True
print(Student.is_passing([30, 25, 20])) # False
s1.display()