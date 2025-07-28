def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def printprime(n):
    print(f"Printing primes upto {n}")
    for i  in range(2,n+1):
        if isprime(i):
            print(i,end=' ')
limit=int(input("Print all prime numbers upto"))
printprime(limit)