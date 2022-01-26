import math

#Variables
primeNumbers = [2]
answer = 0

#Finds every prime number
for prime in range(3,200000,2):
    temp = 0

    #Stops loop if answer has been found
    if len(primeNumbers) == 10001:
        break

    #Tests if each number in list is prime
    for i in range(3, round(math.sqrt(prime))+1):
        if prime % i == 0:
            temp = 1
            break

    #Adds prime number to list
    if temp == 0:
        primeNumbers.append(prime)

#Displays answer
print(primeNumbers[-1]) #Expected 104743