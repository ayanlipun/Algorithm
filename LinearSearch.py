# Input : arr[] = {10, 20, 80, 30, 60, 50,
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6
# Element x is present at index 6
#
# Input : arr[] = {10, 20, 80, 30, 60, 50,
#                      110, 100, 130, 170}
#            x = 175;
# Output : -1
# Element x is not present in arr[].

def LinerSearch(arr, data):

    for i in range(len(arr)):
        if arr[i] == data:
            return i
    return -1


array  = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
data=110

result =LinerSearch(array,data)

if (result == -1):
    print("Element is not found!")
else:
    print(("Elment found at index:",result))


