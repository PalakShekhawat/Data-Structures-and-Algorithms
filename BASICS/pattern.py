for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print()
print()
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()

print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

print()

print("Star Pyramid")
n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for k in range(0,(2*i)+1):
        print("*", end=" ")
    for j in range(0,n-i-1):
        print(" ",end=" ")
    print()
print()
print("Inverted Star Pyramid")
n=5
for i in range(0,n+1):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(0,2*n+1-2*i):
        print("* ", end="")
    for j in range(0,i):
        print(" ",end="")
    print()





