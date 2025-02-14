class Person:
    
    def __init__(self, name, age, role, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role

    def __repr__(self):
        return f"{self.name} is a {self.role}"