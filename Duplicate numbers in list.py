def duplicate_numbers(numbers):
    duplicate=[]
    for num in numbers:
        if numbers.count(num)>1 and num not in duplicate:
            duplicate.append(num)
    return duplicate
numbers=[10,20,50,30,20,30]
print("Duplicate numbers in list :",duplicate_numbers(numbers))