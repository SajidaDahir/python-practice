def reverseString(s):       #define function
    reverseString = ""
    for char in s:      #for a character in a string
        reverseString = char + reverseString    #reverse the characters
    return reverseString    #return the reversed string

print(reverseString("Hello and Welcome"))   #testing