#Lab8-Q8(b)
x=[int(y) for y in input().split()] 
total_product=1
for element in x:
    total_product*=element
print(total_product)