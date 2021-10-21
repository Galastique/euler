#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


#Variables
primeNumbers = []
prime = 1

#Loop
for x in range(0,200000):
    prime += 1
    temp = 0

    #Stops loop if list has 10001 items
    if len(primeNumbers) == 10001:
        break

    #Tests if each number in list is prime
    for i in primeNumbers:
        if prime % i == 0:
            temp = 1
            break

    #Adds prime number to list
    if temp == 0:
        primeNumbers.append(prime)


#Displays answer
print(primeNumbers[-1])