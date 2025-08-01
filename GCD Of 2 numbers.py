def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
x=int(input("Enter the value of a : "))
y=int(input("Enter the value of b : "))
print(gcd(x,y))