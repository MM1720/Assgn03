n=int(input("Enter the no of elements in the list"))
L1=[]
for i in range(0,n):
    a=int(input("Enter the number in the list"))
    L1.append(a)
L=[]
for i in L1:
    L.append((i,i**2))
print(L)
