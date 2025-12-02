import pickle
file=open("marks.dat","wb")
marks=int(input("Enter the marks:"))
name=input("Enter the name")
store={'name':name,"marks":marks}
pickle.dump(store,file)
file.close()
file=open("marks.dat","rb")
rec=pickle.load(file)
if rec['marks']>95:
    print(rec)
file.close()
