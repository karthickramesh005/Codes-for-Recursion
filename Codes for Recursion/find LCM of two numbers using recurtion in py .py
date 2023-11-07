# find LCM of two numbers using recurtion in py :

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


def lcm(a, b):
    return (a * b) // hcf(a, b)


first = int(input("Enter a first number : "))
second =  int(input("Enter a second number : "))

print("Lcm of", first, "and", second, "is", lcm(first, second))
