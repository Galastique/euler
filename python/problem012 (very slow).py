#Variables
divisors = 0
number = 0

#Finds triangular number
for x in range(1, 100000):
    divisors = 0
    number += x

    #Counts divisors
    for y in range(1, round(number/2)+1):
        if number % y == 0:
            divisors += 1

    #Checks if answer has been found
    if divisors > 500:
        #Displays answers
        print(number) #Expected 76576500
        exit()