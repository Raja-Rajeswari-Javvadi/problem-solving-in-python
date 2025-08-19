def Second_Largest(numbers):
    unique_number=list(set(numbers))
    unique_number.sort(reverse=True)
    if len(unique_number)>=2:
        return unique_number[1]
    else:
        return "No Second largest number"
numbers=[1,3,5,9,4]
print("Second Largest number in list is : ",Second_Largest(numbers))