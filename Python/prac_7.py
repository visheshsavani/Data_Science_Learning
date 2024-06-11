class Student:
    def __init__(self,name,marks_s1,marks_s2,marks_s3) -> None:
        self.name = name
        self.marks_s1 = marks_s1
        self.marks_s2 = marks_s2
        self.marks_s3 = marks_s3
    def avg(self):
        return (self.marks_s1+self.marks_s2+self.marks_s3)/3

s1 = Student("Vishesh",55,66,67)
s2 = Student("Rohan",54,66,67)
s3 = Student("Karthik",53,66,67)
print(s1.avg())
print(s2.avg())
print(s3.avg())
