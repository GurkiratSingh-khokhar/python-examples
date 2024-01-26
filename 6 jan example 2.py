print("welcome to pu")
# a="kirat"
name=input('enter user name')
print("welcome", name)
chemistry=int(input('enter chemistry marks'))
maths=int(input('enter maths marks'))
physics=int(input('enter physics marks'))
english=int(input('enter english marks'))
punjabi=int(input('enter punjabi marks'))
marks=chemistry+maths+physics+english+punjabi
print("total marks obtained by",name ,"is", marks,"/500")
total =500
marks1=marks/total
marks2=marks1*100
print("percentage",marks2)
