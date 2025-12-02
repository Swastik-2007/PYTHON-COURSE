import pickle
def search():
    company1={'CompId':'1005','CName':"Rjadhani",'Turnover':"Howrah"}
    company2={'CompId':'2005','CName':"Garibrath",'Turnover':"Howrah"}
    company3={'CompId':'3005','CName':"Bhande varat",'Turnover':"Howrah"}
    company4={'CompId':'1005','CName':"Lalgola",'Turnover':"Howrah"}
    file=open("Company.dat","wb")
    pickle.dump(company1,file)
    pickle.dump(company2,file)
    pickle.dump(company3,file)
    pickle.dump(company4,file)
    file.close()

def display():
    found = False
    try:
        file=open("Company.dat","rb")
        while True:
            Record=pickle.load(file)
            if Record['CompId']=='1005':
                print(Record)
                found=True
    except EOFError:
        if found==False:
            print("Discarded")
        else:
            print("Successfully founded")
        file.close()
search()
display()    