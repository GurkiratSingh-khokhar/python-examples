space=4
for i in range(5):
    for j in range(space,0,-1):
        print(" ",end=" ")
    space-=1
    for j in range(i+1):
        print("*  ",end=" ")
    print(" ")