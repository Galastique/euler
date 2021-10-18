#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


#List
palindromes = []
test = []

#Variables
maxX = 999
maxY = 999
number = 998001
x = 0
y = 0
palindrome = number

#Finds all palindromes
while palindrome >= 100000:

    #Converts palindrome to string
    checkPalindrome = str(palindrome)

    #Checks if number is palindrome
    if (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3]):
            
        #Adds palindrome to list
        palindromes.append(palindrome)
        
        """
        #Checks palindromes for multipliers
        for x in palindromes:
            if palindrome % maxX == 0:
                test.append(maxX)
            if maxX > 1:
                maxX -= 1
        """
        
    #Finds more palindromes
    palindrome -= 1

#Displays answers
print("\n")
print(palindromes)
