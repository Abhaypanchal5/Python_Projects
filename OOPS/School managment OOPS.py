class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def contact_info(self):
        print(f"{self.name} : {self.phone}")

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}"


class Student(Person):
    def __init__(self, name, age, phone, roll_no, grade):
        super().__init__(name, age, phone)
        self.roll_no = roll_no
        self.grade = grade
        self.subjects = {}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def get_average(self):
        return round(sum(self.subjects.values()) / len(self.subjects), 2)

    def get_rank_score(self):
        return self.get_average()

    def __str__(self):
        base = super().__str__()
        return f"{base} | Roll No: {self.roll_no} | Grade: {self.grade} | Avg: {self.get_average()}"

    def __eq__(self, other):
        return self.roll_no == other.roll_no       

    def __lt__(self, other):
        return self.get_average() < other.get_average()   


class Teacher(Person):
    def __init__(self, name, age, phone, subject, salary):
        super().__init__(name, age, phone)
        self.subject = subject
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        base = super().__str__()
        return f"{base} | Subject: {self.subject} | Salary: ₹{self.salary}"


class Classroom:
    total_classrooms = 0

    def __init__(self, class_name, teacher):
        self.class_name = class_name
        self.teacher = teacher
        self.students = []
        Classroom.total_classrooms += 1

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                print(f"Student {roll_no} removed.")
                return
        print("Student not found.")

    def show_students(self):
        if not self.students:
            print("No students in class.")
            return
        print(f"\nStudents in {self.class_name}:")
        for s in self.students:
            print(s)                                

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average())  

    def class_average(self):
        if not self.students:
            return 0
        return round(sum(s.get_average() for s in self.students) / len(self.students), 2)  

    def find_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s
        print("Student not found.")
        return None

    def __str__(self):
        return (f"Class: {self.class_name} | "
                f"Teacher: {self.teacher.name} | "
                f"Students: {len(self.students)}")


class School:
    total_schools = 0

    def __init__(self, school_name):
        self.school_name = school_name
        self.classrooms = []
        School.total_schools += 1

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def show_classrooms(self):
        if not self.classrooms:
            print("No classrooms available.")
            return
        print(f"\nClassrooms in {self.school_name}:")
        for c in self.classrooms:
            print(c)

    def best_classroom(self):
        if not self.classrooms:
            return None
        return max(self.classrooms, key=lambda c: c.class_average())

    def __str__(self):
        return (f"School: {self.school_name} | "
                f"Total Classrooms: {len(self.classrooms)}")
        
# Teachers
t1 = Teacher("Mr. Sharma", 40, "9111111111", "Mathematics", 65000)
t2 = Teacher("Ms. Priya", 35, "9222222222", "Science", 60000)

# Classrooms
c1 = Classroom("Class 10A", t1)
c2 = Classroom("Class 10B", t2)

# Students
s1 = Student("Abhay", 16, "9999999999", "R001", "10A")
s2 = Student("Yash", 16, "8888888888", "R002", "10A")
s3 = Student("Raj", 16, "7777777777", "R003", "10A")
s4 = Student("Sara", 15, "6666666666", "R004", "10B")
s5 = Student("Mehul", 15, "5555555555", "R005", "10B")

# Add subjects
s1.add_subject("Maths", 92)
s1.add_subject("Science", 88)
s1.add_subject("English", 95)

s2.add_subject("Maths", 70)
s2.add_subject("Science", 65)
s2.add_subject("English", 72)

s3.add_subject("Maths", 55)
s3.add_subject("Science", 60)
s3.add_subject("English", 58)

s4.add_subject("Maths", 80)
s4.add_subject("Science", 85)
s4.add_subject("English", 78)

s5.add_subject("Maths", 45)
s5.add_subject("Science", 50)
s5.add_subject("English", 48)

# Add students to classrooms
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

c2.add_student(s4)
c2.add_student(s5)

# Add classrooms to school
school = School("Delhi Public School")
school.add_classroom(c1)
school.add_classroom(c2)

# Display
print(school)
school.show_classrooms()
c1.show_students()

# Top student
top = c1.top_student()
print(top)

# Class average
print(c1.class_average())

# Find student
found = c1.find_student("R001")
print(found)
c1.find_student("R999")

# Remove student
c1.remove_student("R002")
c1.show_students()

# Dunder methods
print(s1 == s2)    # False — different roll_no
print(s1 > s2)     # True — s1 has higher average

# Best classroom
best = school.best_classroom()
print(best)

# Teacher salary property
print(t1.salary)

# Class variable
school2 = School("Kendriya Vidyalaya")
print(School.total_schools)   # 2
print(Classroom.total_classrooms)  # 2