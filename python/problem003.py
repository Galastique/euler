#Imports
import math

#Variables
factors = []
number = 600851475143

#Finds prime factors of 600851475143
for prime in range(1, number):

    #Adds number to list if its prime
    if number % prime == 0:
        factors.append(prime)

        #Check if all prime factors have been found
        if math.prod(factors) == number:
            print(prime)  # Expected 6857
            exit()