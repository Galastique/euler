#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


#List
palindromes = []

#Variables
maxX = 999
maxY = 999
number = 998001
palindrome = number

#Finds all palindromes bigger then 100000
for palindrome in range(100000, number):

    #Converts number to string
    checkPalindrome = str(palindrome)

    #Checks if number is palindrome
    if (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3]):
            
        #Adds palindrome to list
        palindromes.append(palindrome)
        
        
        #Checks palindromes for multipliers
        a = 100
        b = 100
        biggest = 0
        for a in range(a, 999):
            for b in range(b, 999):
                product = a * b
                if (product > biggest and (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3])):
                    biggest = product
                b += 1
            b = 100
            a += 1
        
        
    #Finds more palindromes
    palindrome -= 1

#Displays answers
print("\n")
print(palindromes)
print(biggest)
