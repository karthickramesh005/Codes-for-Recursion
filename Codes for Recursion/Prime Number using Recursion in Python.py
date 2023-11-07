# Prime Number using Recursion in Python :

def prime(n,i = 2):
    if n == i :
        return True
    elif n % i == 0 :
        return False
    return prime(n,i + 1)


n = int(input("Enter a number : "))

if prime(n):
    print("Yes",n," is a prime number.")
else:
    print("No",n," was not prime number.")
