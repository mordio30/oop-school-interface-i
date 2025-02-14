from classes.staff import Staff
from classes.student import Student

class School:
    # school.py

    def __init__(self, name):
        self.name = name   
        self.students = Student.all_students() #[<>]
        self.staff = Staff.all_staff() #[<>]