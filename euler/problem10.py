#Variables
primeNumbers = [2]
prime = 0
sumPrimes = 0

#Run loop as long as list has less than 10,001 items
for x in range(1, 100000, 2):
    prime = x

    #Tests if each number in list is prime
    for i in primeNumbers:
        if prime % i == 0:
            break
        else:
            primeNumbers.append(prime)
            sumPrimes = sum(primeNumbers)
            print(primeNumbers)



#Displays answer
print(sumPrimes)