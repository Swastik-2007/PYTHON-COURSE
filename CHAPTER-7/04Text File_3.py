file=open("Mynotes.txt","r")
for line in file:
    if line.startswith("k"):
         print(line)