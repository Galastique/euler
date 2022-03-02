from math import floor

#Variables
factors = 1
number = 600851475143

#Finds prime factors of 600851475143
for prime in range(1, floor(number/2)):

    #Multiplies number to total if its prime
    if number % prime == 0:
        factors *= prime

        #Check if all prime factors have been found
        if factors == number:
            print(prime)  #Expected 6857
            exit()