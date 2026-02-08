#Ask the user for a string and print out whether this string is a palindrome or not. A palindrome is a string
#that reads the same forwards and backwards.

text = input("enter the text")
text2 = text.lower()
Rtext = text2[::-1]

if(text2 == Rtext):
    print("It is a palindrome")
else:
    print("not a palindrome")