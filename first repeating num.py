arr=[1,3,4,5,3,6]
def firstRepeating(arr):
    seen=set() #initialize an empty set called seen to store seen elements
    for num in arr: #iterating over an array
        if num in seen:#if the number we are checking is already in the seen
            return num #then return that number
        seen.add(num)#or else add that number to the seen
    return None #if there is no numbers in the array then return none
print(firstRepeating(arr))