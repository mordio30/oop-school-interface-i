from classes.person import Person
import csv
# student.py
class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        container = []
        with open('./data/students.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # print(row)
                container.append(cls(**row))
        return container