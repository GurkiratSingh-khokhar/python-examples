print("welcome to atm")
name=input("enter your name")
user={"admin","qwerty","demo"}
if name in user:
    print("welcome",name)
else:
    print(name,"not found")
password={"admin" == 1235,"qwerty" == 1987 ,"demo" == 5674 }
checkpas=int(input("enter password"))
if checkpas in password:
    print(password.get(checkpas))
else:
    print("wrong password")