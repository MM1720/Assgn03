n=int(input("Enter the number of terms for Fibonacci "))
a=0
b=1
d=0
print(a,end=" ")
for i in range(1,n):
    c=a+b
    d=d+b
    print(str(b),end=" ")
    a=b
    b=c
    if i==n-1:
        print()
        print("Average of input no of terms in fibonacci is ",d/n)
