def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
x=int(input("Enter a value : "))
y=int(input("Enter b value : "))
print(lcm(x,y))
