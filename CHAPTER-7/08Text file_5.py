file=open("data.txt","r")
vowels=["a","e","i","o","u"]
for line in file:
    word = line.split()
    for words in word:
        if words[0] in vowels:
         print(words)