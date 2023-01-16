d={}
d['name']=input("Enter name")
d['SID']=int(input("Enter SID"))
while True:
    print("Do you want to add more record",end=" ")
    c=input("Enter your choice - Y/N")
    if c in 'Yy':
        d['name']=input("Enter name")
        d['SID']=int(input("Enter SID"))
    elif c in 'Nn':
        break
    else:
        print("ERROR")
        break
print(d)
