def Displaywords(file_name):
    file=open(file_name,"r")
    for line in file:
        words=line.split()
        for word in words:
            if len(word)<4:
                print(word)
Displaywords("Story.txt")

