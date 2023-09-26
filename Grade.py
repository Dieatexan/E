#Get the student grades and able to display the grades, calculate the GPA, and convert the grade to points.
class Grade:
    def __init__(self, grade, course, date):
        self.grade = grade
        self.grade = course
        self.grade = date
    #Get the student grades
    def getGrade(self):
        return self.grade
    #Set the student grades
    def setGrade(self, grade):
        self.grade = grade
    #Calculate GPA based on grades recorded 
    def calculate_gpa(self):
        return self.grade
    #Calculate GPA based on grades recorded and total number of points
    def display_grade(self):
        return self.grade

    def __str__(self):
        return str(self.grade)