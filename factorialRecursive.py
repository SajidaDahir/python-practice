def factorialRecursive(n):
    if n <= 1:
        return n
    else:
        return n * factorialRecursive(n - 1)

print(factorialRecursive(3))