#Variables
numbers = []
number = 0

#Finds number
for x in range(2, 200000):
    number = 0
    digits = []

    #For every digit in number
    for digit in range(0, len(str(x))):

        #Find value of the powers of 5 of the digits
        number += int(str(x)[digit])**5

    #Adds number to list
    if number == x:
        numbers.append(x)

#Displays answers
print(sum(numbers)) #Expected 443839