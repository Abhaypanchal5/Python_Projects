class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_subject(self, subject, marks):
        self.marks[subject] = marks

    def get_average(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return (f"Name        : {self.name}\n"
                f"Roll No     : {self.roll_no}\n"
                f"Average     : {self.get_average()}\n"
                f"Grade       : {self.get_grade()}")


class ReportCard:
    total_enrolled = 0

    def __init__(self, school_name):
        self.school = school_name
        self.students = []

    def enroll(self, student):
        self.students.append(student)
        ReportCard.total_enrolled += 1

    def show_all(self):
        print(f"\n--- {self.school} Report Card ---")
        for i, s in enumerate(self.students, 1):
            print(f"\nStudent {i}:\n{s}")

    def topper(self):
        return max(self.students, key=lambda s: s.get_average())  # ✅ return it


# Test
lib = ReportCard("Delhi Public School")

s1 = Student("Abhay", 101)
s1.add_subject("Maths", 92)
s1.add_subject("English", 88)
s1.add_subject("Science", 95)

s2 = Student("Yash", 102)
s2.add_subject("Maths", 60)
s2.add_subject("English", 55)
s2.add_subject("Science", 58)

s3 = Student("Raj", 103)
s3.add_subject("Maths", 75)
s3.add_subject("English", 80)
s3.add_subject("Science", 70)

lib.enroll(s1)
lib.enroll(s2)
lib.enroll(s3)

lib.show_all()

print(f"\nTotal Enrolled : {ReportCard.total_enrolled}")
print(f"\nTopper : {lib.topper().name} with avg {lib.topper().get_average()}")