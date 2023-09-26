#This is the base class to create a student object.
#It includes the student name, degree plan, ID, and email.
class Student:
    id = 0
    name =""
    course=[]
    grade=[]
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.course = []
        self.grade = []
        
    def __str__(self):
        return self.
        
        
        
        
        
        
    def __init__(self, student_name, degree_plan, ID, email):
        self.student_name = student_name
        self.degree_plan = degree_plan
        self.degree_plan = ID
        self.degree_plan = email
        self.grades = {}
        
        
        
        
    #Get the student to register for classes
    def register(self, course):
        self.grades[course] = None
    #Get the sudent to add a course
    def add_course(self, course):
        self.grades[course] = None
    #Drop a course
    def drop_course(self, course):
        del self.grades[course]
    #Look up a course
    def lookup_course(self, course):
        return self.grades.get(course, None)
    