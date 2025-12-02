class Employee:
    company = "ITC"
    salary=2000000
    def show(self):
        print(f"The name of the company is {self.company} and the salary is {self.salary}")



class Coder:
    language="Python"
    def printLanguages(self):
        print(f"Out of all language here is your language {self.language}")


class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showlanguage(self):
        print(f"The name of the company is {self.company} and he is good with {self.language} language")


a=Employee()
b=Programmer()
b.showlanguage()
b.printLanguages()
b.show()
