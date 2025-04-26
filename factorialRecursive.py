def factorialRecursive(n):
    if n <= 1:  #functn can't call when number is 1 or below 1
        return n
    else:
        return n * factorialRecursive(n - 1)    #calls functn repeatedly minusing 1

print(factorialRecursive(3))    #testing