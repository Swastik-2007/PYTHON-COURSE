import random
def num(n):
   lower_limit=10**(n-1)
   upper_limit=(10**n)-1
   return random.randint(lower_limit,upper_limit)
n=int(input("Enter the digit:-"))
calc=num(n)
print(calc)

