#Largest element using max()
li=[1,2,4,5,7,8]
maxli=max(li)
print(" ")
print(maxli)
#using reduce()
from functools import reduce
numbers=[2,4,5,67,8]
largest=reduce(lambda a,b:a if a>b else b,numbers)
print(largest)
 #using for
largest=li[0]
for val in li:
    if val>largest:
        largest=val
print(val)