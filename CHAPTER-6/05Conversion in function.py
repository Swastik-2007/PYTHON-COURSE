def conversion(f):
    return 5*(f-32)/9
f=int(input("Enter the temperature in F:"))
temp=conversion(f)
print(f"{round(temp,2)}")

