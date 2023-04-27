
def SumFunc(a, b):
    if b == 0:
        return a
    return SumFunc(a + 1, b - 1)


print(" Enter first number:")
firstNum = int(input())

print(" Enter second number:")
secNum = int(input())

print(SumFunc(firstNum, secNum))
