def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "b should not be 0"
    return a/b
print("Enter the choice : ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")
choice=int(input("Enter your choice : "))
num1=float(input("Enter the 1st num : "))
num2=float(input("Enter the 2nd num : "))
if choice==1:
    print("Addition of a,b = ",add(num1,num2))
elif choice==2:
    print("Addition of a,b = ",subtract(num1,num2))
elif choice==3:
    print("Addition of a,b = ",multiply(num1,num2))
elif choice==4:
    print("Addition of a,b = ",divide(num1,num2))
else:
    print("Invalid input")
