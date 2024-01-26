print("student result checker")
marks=int(input('enter student total marks from 500'))
total=500
marks1=marks/total
n=marks1*100
print(n)
a=90
b=80
c=70
d=60
e=50
if(n>=a):
    print("a+")
elif(n>=b and n<=a):
    print("a")
elif(n>=c and n<=b):
    print("b+")
elif(n>=d and n<=c):
    print("b")
elif (n>=e and n<=d):
    print("c")
elif(n<=e):
    print("d")
pf=50
if(n>=pf):
    print("pass")
else:
    print("fail")