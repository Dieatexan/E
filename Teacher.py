#Base class for the teacher
#Includes the ability to upload assignments, grade assignments, and view assignments
class Teacher:
    def __init__(self, teacher_name, ID, email):
        self.teacher_name = teacher_name
        self.degree_plan = ID
        self.degree_plan = email
        self.grades = {}
    #Courses that the teacher teaches  
    def courses_teached(self, course):
        self.grades[course] = None
    #Upload assignments
    def upload_assignments(self, course):
        self.grades[course] = None
    #Grade assignments
    def grade_assignments(self, course):
        self.grades[course] = None
    #View assignments
    def view_assignments(self, course):
        self.grades[course] = None
        