#This class is used to store the financial aid information of a student and calculate the total amount of financial aid.
class FinancialAid:
    def __init__(self, income, expenses, aid):
        self.income = income
        self.expenses = expenses
        self.aid = aid
    #Get the student income
    def view_income(self):
        return self.income
    #Get the student expenses including tuition, books, and living expenses
    def view_expenses(self):
        return self.expenses
    #Get the student financial aid
    def view_aid(self):
        return self.aid
    