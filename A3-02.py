day=int(input("Enter date"))
month=int(input("Enter month"))
year=int(input("Enter Year")) 
if 1800<=year<2025:
    if 1<=month<12:
        if 1<=day<31:
            print(day+1,"/",month,"/",year)
        elif day==31:
            print("1/",month+1,"/",year)
        else:
            print("Invalid Input")
    elif month==12:
        if 1<=day<31:
            print(day+1,"/",month,"/",year)
        else:
            print("1/1",year+1)
    else:
       print("Invalid Input") 
elif year==2025:
    if 1<=month<12:
        if 1<=day<31:
            print(day+1,"/",month,"/",year)
        elif day==31:
            print("1/",month+1,"/",year)
        else:
            print("Invalid Input")
    elif month==12:
        if 1<=day<31:
            print(day+1,"/",month,"/",year)
        else:
            print("1/1",year+1)
    else:
       print("Invalid Input") 
else:
    print("Date is out of given range")
