#checking if a given number is even or odd

def evenOdd(num):
    if num % 2 == 0:    #if a num is divisible by 2 with no remainder = even
        return "Even"
    else:               #if a num divides by 2 with a remainder = odd
        return "Odd"

print(evenOdd(5))