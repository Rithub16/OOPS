class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary
e1 = Employee("Rithu", 50000)
e2 = Employee("Anu", 60000)

print(e1 > e2)  # False
print(e1 < e2)  # True
