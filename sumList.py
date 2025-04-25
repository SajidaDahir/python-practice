#finding sum for certain numbers in a list

def sum(list):        #define a function called sum
    sum = 0           #initially sum = 0
    for i in list:
        sum += i      #for every number i, the sum will be sum + i
    return sum

print(sum([5,6,7,8,9]))