# Power of a Number using Recursion in Python :
'''
# Its normal way :
import math

n= int(input("Enter a value number : "))
p = int(input("Enter a power number : "))

print(n,"power of",p," is : ",pow(n,p))
'''

# using recursion :
def power(n,p):
    if p != 0:
        return  n * power(n,p -1)
    else:
        return 1
    
n= int(input("Enter a value number : "))
p = int(input("Enter a power number : "))
print(n,"power of",p," is : ",power(n,p))
