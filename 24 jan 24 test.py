# import math
#
# r=int(input("enter radius no"))
# area=math.pi*r**2
# print(area)

#
# name=(input("enter your name"))
# no=int(input("enter consumer no"))
# if name=="admin" and no==1234:
#     print("found")
# elif name=="qwerty" and no==2345:
#     print("found")
# elif name=="abcd" and no==3456:
#     print("found")
# elif name=="bcde" and no==4567:
#     print("found")
# elif name=="cdef" and no==5678:
#     print("found")
# else:
#     print("not found")
# units=int(input("enter units"))
# total=units*10
# print(total)

# pay=input("enter bill type")
# if pay == "comercial":
#




from tabulate import tabulate
data =[["first name"] , ["last name"] , ["contact no"] , ["email id"]]
print(tabulate(data, headers="firstrow",tablefmt="grid"))



#
