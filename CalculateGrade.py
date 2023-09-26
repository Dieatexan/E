#Calculate Grade Class
class CalculateGrade:
    def __init__(self, student_name, degree_plan):
        self.student_name = student_name
        self.degree_plan = degree_plan
        self.grades = {}
    
    #View degree plan
    def view_degree_plan(self):
        return self.degree_plan
    
    #Recond grade
    def record_grade(self, course, grade):
        self.grades[course] = grade
        
    #Calculate GPA based on grades recorded
    def calculate_gpa(self):
        total = 0
        for grade in self.grades.values():
            total += grade
        return total / len(self.grades)
    
    #Calculate GPA based on grades recorded and total number of points
    def grade_to_point(grade):
        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        return grade_points.get(grade, 0.0)


    
    
    