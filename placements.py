lines=[line.strip() for line in open("D:\\_MCA\\$Sem 5\\Python\\placement.txt")]

nlist=[]
flag=1
#Nested List
for i in range(len(lines)):
    rec=lines[i].split(" ")
    nlist.append(rec)
print(nlist)
def sortApti(val):
    return val[1]
def sortTech(val):
    return val[2]
def sortHR(val):
    return val[3]
def sortFinal(val):
    return val[4]
ch="y"
while ch=="y" or ch=="Y":
    print("1.Top 3 in aptitude")
    print("2.Top 3 in technical")
    print("3.Top 3 in hr")
    print("4.Top 3 in final")
    print("5.Search by name")
    
    choice=int(input("Enter your choice:"))
    if choice==1:
        nlist.sort(key=sortApti,reverse=True)
        print(nlist[:3])
    elif choice==2:
        nlist.sort(key=sortTech,reverse=True)
        print(nlist[:3])
    elif choice==3:
        nlist.sort(key=sortHR,reverse=True)
        print(nlist[:3])
    elif choice==4:
        nlist.sort(key=sortFinal,reverse=True)
        print(nlist[:3])
    elif choice==5:
        name=input("Enter name of the student:")
        for i in range(len(nlist)):
            if name == nlist[i][0]:
                print(nlist[i])
                flag=0
                break
            else:
                flag=1
        if flag==1:
            print("Username is not present in the list")
    else:
        print("Enter values between 1 to 5")
    ch=input("Do you want to continue?")
