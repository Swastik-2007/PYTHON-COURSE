def series(first,last):
    step=(last-first)//3
    series=[first,first+step,first+2*step,last]
    return series
first=int(input("Enter the first number:"))
last=int(input("Enter the last number:"))
calc=series(first,last)
print(calc) 
  