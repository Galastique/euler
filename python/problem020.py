#Plugins
import math


#Variables
factorial = math.factorial(100)
digits = []
answer = 0


#Converts number to string
temp = str(factorial)

#For every digit in string
for x in temp:
    #Add digit to list
    numX = int(x)
    digits.append(numX)

#Assigns answer to variable
answer = sum(digits)


#Displays answers
print(answer) #Expected 648