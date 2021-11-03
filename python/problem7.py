#Variables
primeNumbers = []

#Loop
for prime in range(2,200000):
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