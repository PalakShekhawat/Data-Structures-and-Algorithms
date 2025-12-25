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

print("Diamond Star Pattern")
n=5
for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(0,(2*i)+1):
        print("*", end=" ")
    for j in range(0,n-i-1):
        print(" ",end=" ")
    print()

for i in range(0,n+1):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(0,2*n+1-2*i):
        print("* ", end="")
    for j in range(0,i):
        print(" ",end="")
    print()


print(" Half Diamond Star Pattern")
for i in range(0,n+1):
    for k in range(0,i+1):
        print("*", end=" ")
    print()
for i in range(1,n+1):
    for k in range(0,n+1-i):
        print("* ", end="")

    print()

print("Binary Number Triangle Pattern")
for i in range(0,n+1):
    if(i%2==0):
        k=0
    else:k=1
    for j in range(0,i):
        print (k, end=" ")
        if(k==0):k=k+1
        else:k=k-1
    print()

print("Number Crown Pattern")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    for a in range(2*(n-i)-1,-1,-1):
        print(" ", end="")
    for k in range(i,0,-1):
        print(k, end="")

    print()
