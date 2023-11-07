# Largest Element in an Array using Recursion in Python : 


def findMaxRec(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))
 
# Driver Code
if __name__ == "__main__":
     
    A = list(map(int,input("Enter a array items : ").split()))
    n = len(A)
    print("The largest element of array is ",findMaxRec(A, n))
