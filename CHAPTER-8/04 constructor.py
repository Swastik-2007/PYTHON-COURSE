class Employee:
    language = "Python"#This is an class attribute
    salary = 12000000

    def __init__(self,name,salary,language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

        
    @staticmethod  #it converts greet into a function,no need to write the object i.e self
    def greet():
        print("Good morning")


rik=Employee("Swastik",1300000,"JavaScript")
#rik.name="Robinson"
print(rik.name,rik.salary,rik.language)
