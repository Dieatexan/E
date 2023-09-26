#This class will allow you to search for classes, enroll, drop, withdraw and view classes.
class SearchFunction:
    def __init__(self, class_name, search):
        self.search = search
        self.class_name = class_name
        self.search = {}
    #Search for classes
    def search_class(self, class_name):
        return self.class_name
    #Enroll in classes
    def enroll_class(self, class_name):
        self.search[class_name] = class_name
    #Drop classes
    def drop_class(self, class_name):
        del self.search[class_name]
    #View classes
    def view_class(self):
        return self.search
    #Withdraw from classes
    def withdraw_class(self, class_name):
        self.search[class_name] = class_name