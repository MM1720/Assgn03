Set1=[1,2,3,4,5]
Set2=[2,4,6,8]
Set3=[1,5,9,13,17]
#a
L1=[]
for i in Set1:
    if i not in Set2:
        L1.append(i)
for i in Set2:
    if i not in Set1:
        L1.append(i)
print(L1)
#b
L2=[]
for i in Set1:
    if i not in Set2 and i not in Set3:
        L2.append(i)
for i in Set2:
    if i not in Set1 and i not in Set3:
        L2.append(i)
for i in Set3:
    if i not in Set2 and i not in Set1:
        L2.append(i)
print(L2)
#c
L3=[]
for i in Set1:
    if i in Set2 or i in Set3 and i not in Set2 and Set2:
        L3.append(i)
for i in Set3:
    if i in Set2 or i in Set1 and i not in Set1 and Set2:
        L3.append(i)
print(L3)
#d
L4=[]
for i in range(1,11):
    if i not in Set1:
        L4.append(i)
print(L4)
#e
L5=[]
for i in range(1,11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        L5.append(i)
print(L5)
