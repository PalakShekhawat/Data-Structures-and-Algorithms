x=int(input("Enter the Number Pattern: "))
f = 0
if (x < 0):
    f = 1
    x = abs(x)
# l=len(x)
l = len(str(x))
num = 0
for i in range(1, l + 1):
    n = x % 10
    num = num * 10 + n
    x = x // 10
if (f == 1):
    num = num * (-1)
if num < -2147483648 or num > 2147483647:
   print("0")

print(num)