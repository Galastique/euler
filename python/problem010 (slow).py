import math

#Variable
sumPrimes = 2

#Finds prime numbers
for x in range(3,2000000,2):
    temp = 0

    #Tests if each number in list is prime
    for i in range(3, round(math.sqrt(x))+1):
        if x % i == 0:
            temp = 1
            break

    #Adds prime number to list
    if temp == 0:
        sumPrimes += x

#Displays answer
print(sumPrimes) #Expected 142913828922