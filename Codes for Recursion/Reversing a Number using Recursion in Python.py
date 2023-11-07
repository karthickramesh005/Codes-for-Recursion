# Reversing a Number using Recursion in Python :

def reverse_digit(arr, l, n=0):
    if n == l:
        return arr
    arr[n], arr[-1*(n+1)] = arr[-1*(n+1)], arr[n]
    return reverse_digit(arr, l, n + 1)


num = int(input("Enter a values : "))
arr = list(str(num))
arr = reverse_digit(arr, len(arr)//2)
s = ""
print("Reverse is : ",(int(s.join(arr))))
