class Employee:
    language = "Python"#This is an class attribute
    salary = 12000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod  #it converts greet into a function,no need to write the object i.e self
    def greet():
        print("Good morning")


rik=Employee()
#rik.language="Javascript"#This is an instance attribute
rik.greet()
rik.getInfo()
