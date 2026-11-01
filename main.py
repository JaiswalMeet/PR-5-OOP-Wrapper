class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_id(self): return self.__emp_id
    def get_sal(self): return self.__salary

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.__emp_id}, Salary: {self.__salary}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, dept):
        super().__init__(name, age, emp_id, salary)
        self.dept = dept

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.get_id()}, Salary: {self.get_sal()}, Dept: {self.dept}")

p = None
e = None
m = None

while True:
    print("\n1. Make Person\n2. Make Employee\n3. Make Manager\n4. Show Data\n5. Exit")
    opt = input("Select: ")

    if opt == "1":
        p = Person(input("Name: "), input("Age: "))
    elif opt == "2":
        e = Employee(input("Name: "), input("Age: "), input("ID: "), input("Salary: "))
    elif opt == "3":
        m = Manager(input("Name: "), input("Age: "), input("ID: "), input("Salary: "), input("Dept: "))
    elif opt == "4":
        if p: p.show()
        if e: e.show()
        if m: m.show()
    elif opt == "5":
        break