import csv
def add():
   
    fid=int(input("Enter the furniture id number:"))
    fname=input("Enter the furniture name:")
    fprice=int(input("Enter the furniture price:"))
    data=[fid,fname,fprice]
    file=open("furdata.csv","a",newline='')
    wr=csv.writer(file)
    wr.writerow(data)

def search():
    found=False
    file=open("furdata.csv","r")
    rd=csv.reader(file)
    for i in rd:
        if int(i[2])>1000:
            found=True
            print(i[0])
            print(i[1])
            print(i[2])
    if found == False:
        print("FURNITURE ARE OUT OF STOCK")
    file.close()
add()
search()
 