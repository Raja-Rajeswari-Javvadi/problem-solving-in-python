arr=[2,4,1,6,4,8,3]
def secondLargest(arr):
    arr=list(set(arr))#Removes duplicates from the array and will arrange in ascending order
    arr.sort(reverse=True) #arranges in decending order
    return arr[1] if len(arr)>1 else None #returns the second largest element
print(arr)
print(list(set(arr)))
print(secondLargest(arr))