def BinarySearchAlgo(arr, startIndex, endIndex , x):

    # check base case
    if endIndex>=1 :
        mid = startIndex + (endIndex-1) /2

        # If element is present at the middle itself
        if arr[mid]==x:
            return x
        #element present left subArray
        elif arr[mid]>x:
            return BinarySearchAlgo(arr,startIndex, mid-1,x)
        # element present right subArray
        else:
            return BinarySearchAlgo(arr,mid+1,endIndex,x)
    #Element is not exist.
    else:
        return -1


arr = [12,13,14,15,16,17,18]
x=14

result=  BinarySearchAlgo(arr,0,len(arr)-1,x)

if result !=-1 :
    print("The element is present in index %d of array"%result)
else:
    print("The element is not present in array")






