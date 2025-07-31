def reverse_number(n):
    reversed_number=0
    while n>0:
        digit=n%10
        reversed_number=reversed_number*10+digit
        n//=10
    return reversed_number
number=int(input("Enter a number to reverse : "))
print(reverse_number(number))