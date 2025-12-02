class Employee:
    company = "ITC"
    salary=2000000
    def show(self):
        print(f"The name of the company is {self.company} and the salary is {self.salary}")


class Programmer(Employee):
    company="ITC Infotech"
    def showlanguage(self):
        print(f"The name of the company is {self.company} and the salary is {self.salary}")


a=Employee()
b=Programmer()
b.showlanguage()
a.show()
