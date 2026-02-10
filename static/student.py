class Student:

    college_name = "ABC College"

    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name


    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("------------------")

s1 = Student("Rithu", 101)
s2 = Student("Anu", 102)


s1.display()
s2.display()
Student.change_college("XYZ College")


s1.display()
s2.display()


print(Student.is_pass(40))   # Pass
print(Student.is_pass(20))   # Fail
