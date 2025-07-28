def factorial(n):
    if n<0:
        return "Factorial of negative number doesn't exist" 
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number : "))
print("Factorial of ",num,"is",factorial(num))