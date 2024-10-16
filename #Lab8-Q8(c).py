#Lab8-Q8(c)
x=[int(y) for y in input().split()]
for i in range(len(x)):
    mini=x[0]
    if mini>x[i]:
        mini=x[i]
print(mini)