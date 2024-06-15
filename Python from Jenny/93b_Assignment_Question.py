# Date: 22th January 2024 Monday
# Start Time: 05 : 52 PM
# End Time: 08 : 51 PM

class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name

    def showDetails(self):
        print(f"University Name: {self.uni_name}")
        
class Course(University):
    def __init__(self, course_name, uni_name):
        University.__init__(self, uni_name)
        self.course_name = course_name

    def showDetails(self):
        University.showDetails(self)
        print(f"Course Name: {self.course_name}")


class Branch(University):
    def __init__(self, branch_name, uni_name):
        University.__init__(self, uni_name)
        self.branch_name = branch_name

    def showDetails(self):
        University.showDetails(self)
        print(f"Branch Name: {self.branch_name}")

class Student:
    def __init__(self, student_name, uni_name, course_name, branch_name):
        self.student_name = student_name
        University.uni_name = uni_name
        Course.course_name  = course_name
        Branch.branch_name  = branch_name

    def showDetails(self):
        print(f"Student Name: {self.student_name}")
        print(f"University Name: {University.uni_name}")
        print(f"Course Name: {Course.course_name}")
        print(f"Branch Name: {Branch.branch_name}")
        
student_1 = Student("Taimur", "University of America", "AI", "Washington")
student_1.showDetails()
print("------------------------------------------------------------------")

course_1 = Course("Software Engineering","USA")
course_1.showDetails()
print("------------------------------------------------------------------")
branch_1 = Branch("Lahore","Pakistan")
branch_1.showDetails()