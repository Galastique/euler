#Variables
product = 0
greatest = 0


#Checks first multiplier
for a in range(100,1000):

    #Checks second multiplier
    for b in range(100,1000):

        #Gets product of multipliers and converts them to string
        product = a * b
        checkPalindrome = str(product)

        #Check if number is palindrome
        if (checkPalindrome[0] == checkPalindrome[-1]) and (checkPalindrome[1] == checkPalindrome[-2]) and (checkPalindrome[2] == checkPalindrome[-3]):

            #Checks if product is the biggest palindrome so far
            if product > greatest:
                greatest = product


#Displays answer
print(greatest) #Expected 906609