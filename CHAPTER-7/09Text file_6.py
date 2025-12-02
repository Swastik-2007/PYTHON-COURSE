def rec():
    file=open("Story2.txt","r")
    count=0
    for line in file:
        words=line.split()
        for word in words:
            if word.lower() in {"me","my"}:
                count+=1
    print(f"{count}")
rec()