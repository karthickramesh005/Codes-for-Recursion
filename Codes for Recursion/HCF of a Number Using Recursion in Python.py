# HCF of a Number Using Recursion in Python :

def HCF(a,b):
    if b == 0 :
        return a
    else :
        return HCF(b,a % b)


first = int(input("Enter a first number : "))
end = int(input("Enter a end number : "))

print('HCF of', first, 'and', end, 'is', HCF(first, end))
