
def Rec(a, b):
    if b == 1:
        return a
    return a * Rec(a, b-1)


print(" Enter first number:")
firstNum = int(input())

print(" Enter second number:")
secNum = int(input())

print(Rec(firstNum, secNum))
