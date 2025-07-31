def ispalindrome(n):
    original=n
    reversed_num=0
    while n>0:
        digit=n%10
        reversed_num=reversed_num*10+digit
        n//=10
    return original==reversed_num
number=int(input("Enter a number : "))
if ispalindrome(number):
    print(number,"is a palindrome number")
else:
    print(number,"is not a palindrome number")