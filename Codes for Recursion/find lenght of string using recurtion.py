# find lenght of string using recurtion :

def length(str):
    if str == "":
        return 0
    return 1 + length(str[1:])


str =input("Enter a string : ")
print("length of", str, "is", length(str))
