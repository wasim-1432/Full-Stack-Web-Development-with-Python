class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showName(self):
        print("Name=",self.name)
    def showAge(self):
        print("Age=",self.age)
class Employee(Person):
    def __init__(self,name,age,salary):
        self.salary=salary
        super().__init__(name,age)
    def showSalary(self):
        print("Salary=",self.salary)
e1=Employee("Mohd Wasim",22,23000000)
e1.showName()
e1.showAge()
e1.showSalary()