def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i     #for any given number in a range, add 1
    return result       #multiply the numbers in the range

print(factorial(3))