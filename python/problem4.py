#Variables
a = 100
b = 100
greatest = 0


#Checks first multiplier
while (a <= 999):

    #Checks second multiplier
    while (b <= 999):

        product = a * b
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