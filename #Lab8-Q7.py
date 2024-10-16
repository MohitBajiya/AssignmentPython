#Lab8-Q7
n=str(input("Enter the string:"))
x=""
for i in range(len(n)-1,-1,-1):
    x+=n[i]
if(x==n):
    print("it is palindrome")
else:
    print("not palindrome")
print(x)
