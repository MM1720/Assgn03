a="Python is a case sensitive language"
print(len(a))
print(a[::-1])
x=a[slice(10,26)]
y=a.replace('a case sensitive','object oriented')
print(y)
print(a.find('a'))
b=''
for i in a:
    if i!=" ":
        b=b+i
    else:
        continue
print(b)
