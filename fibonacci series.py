def fibonacci_series(n):
    a,b=0,1
    count=0
    if n<=0:
        print("Enter positive integer.")
    elif n==1:
        print("The fibonacci sequence upto ",n,"term")
        print(a)
    else:
        print("The fibonacci sequence upto ",n,"term")
        while count< n:
            print(a,end=' ')
            a,b=b,a+b
            count+=1
num = int(input("Enter a number : "))
fibonacci_series(num)