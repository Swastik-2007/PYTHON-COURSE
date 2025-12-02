import pickle
def Createfile():
    file=open("Book.dat","wb")
    BookNo=int(input("Enter the book number:"))
    Book_Name=input("Enter the book name:")
    Author=input("Enter the author name:")
    Price=int(input("Enter the amount:"))
    Store=[BookNo,Book_Name,Author,Price]
    pickle .dump(Store,file)
    file.close()
def CountRec(Author):
    count =0
    found=False
    try:
        file=open("Book.dat","rb")
        while True:
            Record=pickle.load(file)
            if Record[2]==Author:
                count+=1
                found=True
    except EOFError:
        if found==False:
            print("no books found")
        else:
            print("book successfully founded")
        file.close()
        return count
Createfile()
author=input("Enter the name of the author which you want to search:")
print("Number of books by",author,":",CountRec(author))