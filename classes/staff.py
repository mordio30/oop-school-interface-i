# staff.py
import csv
from classes.person import Person


class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        container = [] # list of staff instances
        with open("./data/staff.csv", "r") as file:
            reader = csv.DictReader(file) # list of dictionaries
            for row in reader:
                # print(row)
                new_staff = Staff(**row)
                # print(new_staff)
                container.append(new_staff)
                # print('container:   ',len(container))
        return container