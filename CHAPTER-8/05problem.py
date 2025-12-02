class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p=Programmer("Swastik",1200000,200719)
print(p.name,p.salary,p.pin,p.pin)
r=Programmer("Rahul",1200000,200719)
print(r.name,r.salary,r.pin,r.pin)