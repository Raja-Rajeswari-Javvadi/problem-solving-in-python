def is_armstrong(n):
    temp=n
    count=len(str(n))
    sum_of_powers=0
    while n>0:
        digit=n%10
        sum_of_powers+=digit**count
        n//=10
    return temp==sum_of_powers
num=int(input("Enter a number : "))
if is_armstrong(num):
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")