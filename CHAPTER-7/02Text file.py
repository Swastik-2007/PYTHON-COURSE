file=open("Article.txt","r")
text=file.read()
count=0
for char in text:
    if char.isupper():
        count+=1
print(count)
