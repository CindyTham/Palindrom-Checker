
#Takes in a word and says whether or not it is a palindrome


word = input ("Hello User, enter the word you would like to check: ")
a=word[::-1]
if (a==word):
    print("This is a Palindrome")
else:
   print("This is NOT a Palindrome")
