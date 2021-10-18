#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

# https://stackoverflow.com/questions/6037973/project-euler-problem-number-4

#List
palindromes = []

#Variables
maxX = 999
maxY = 999
number = 998001
palindrome = number

#Function that checks for palindromes
def checkPalindome():
    #Convert number into string
    checkPalindrome = str(palindrome)
    #Checks palindromes
    if (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3]): 
        #Adds palindrome to list
        palindromes.append(palindrome)

#Finds all palindromes between 100x100 and 999x999
for x in range(100000, number):            

    #Checks palindromes for multipliers
    a = 100
    b = 100
    biggest = 0
    for a in range(a, 999):
        for b in range(b, 999):
            product = a * b
            if checkPalindome:
                biggest = product
            #b += 1
        b = 100
        #a += 1
    
    #Finds more palindromes
    #palindrome -= 1

#Displays answers
print("\n")
print(palindromes)
print(biggest)
