#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

# https://stackoverflow.com/questions/6037973/project-euler-problem-number-4
'''
#List
palindromes = []

#Variables
maxX = 999
maxY = 999
#number = 998001
palindrome = 998001

#Function that checks for palindromes
def checkPalindome():
    #Convert number into string
    checkPalindrome = str(palindrome)
    #Checks if number is palindrome
    if (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3]): 
        #Adds palindrome to list
        palindromes.append(palindrome)

#Finds all palindromes between 100x100 and 999x999
#for x in range(100000, 998001):            

#Checks palindromes for multipliers
a = 100
b = 100
for a in range(99, 999):
    for b in range(99, 999):
        checkPalindome
        product = a * b
        biggest = product
        print(biggest)
        #b += 1
    b = 100
    #a += 1

#Finds more palindromes
#palindrome -= 1

#Displays answers
print("\n")
print(palindromes)
print(biggest)
'''
#Checks if number is a palindrome
def Palindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False

#Variables
a = 100
b = 100
greatest = 0

#Checks multipliers
while (a <= 999):

    while (b <= 999):
        #Multiplies numbers
        product = a * b
        #Converts number to string
        checkPalindrome = str(product)

        #Check if number is palindrome
        if (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3]):

            #Checks if product is the biggest palindrome so far
            if product > greatest:
                greatest = product

        b += 1
    b = 100
    a += 1

#Displays answer
print(greatest)