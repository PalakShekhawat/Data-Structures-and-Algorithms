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
print("\nAlpha-Triangle Pattern")
N=5
ascii_code = 65+N-1

for i in range(0,N+1):
    for j in range(0,i):
        start_char=ascii_code-i+1
        print(chr(start_char+j), end="")

    print()

print("Symmetric-Void Pattern")
#Upper pattern
for i in range(0,N):
    for j in range(i,N):
        print("*", end="")
    for k in range(0,i):
        print(" ", end="")
    for l in range(0, i):
        print(" ", end="")
    for j in range(i,N):
        print("*", end="")
    print()
#lower pattern
for i in range(0,N):
    for j in range(0, i+1):
        print("*", end="")
    for k in range(N-i, 1, -1):
        print(" ", end="")
    for l in range(N-i, 1, -1):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()
N=4
print("Hollow Rectangle Pattern")
for i in range(0,N):
    for j in range(0,N):
        if((i==0) or (j==0) or (j==N-1) or (i==N-1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
N=6

print("The Number Pattern")
for i in range(0,2*N-1):
    for j in range(0,2*N-1):
        top = i
        left = (2*N - 2) - i
        bottom = j
        right = (2*N - 2) - j
        minDistance = min(top, left, bottom, right)
        print(N-minDistance, end="")
        print(" ", end="")
    print()