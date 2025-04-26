def sumDigits(n):      #defines functn to add digits
    total = 0       #variable stores the total
    while n>0:      #loop continues provided n>0
        total += n%10   #no. is divided by 10 to know the last no.
        n = n//10
    return total

print(sumDigits(567))    #testing