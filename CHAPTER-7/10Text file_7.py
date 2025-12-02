file=open("Sample.txt","r")
for line in file:
    words=line.split()
    formatted_line="#".join(words)
    print(formatted_line)