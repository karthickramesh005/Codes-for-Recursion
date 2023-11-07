# Smallest Element in an Array in Python :
def smallitem(arr,l):
    if l == 1 :
        return arr[0]
    else :
        return min(arr[l - 1],smallitem(arr,l - 1))

arr = list(map(int,input("Enter a array items : ").split()))
l = len(arr)
print("Small element  in array is : ",smallitem(arr,l))
