def number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c

a=10
b=6
c=2
print(number(a,b,c))
