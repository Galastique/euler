#Variables
primeNumbers = []
prime = 1

#Run loop as long as list has less than 10,001 items
for n in range(1,50000000):
    prime += 1
    temp = 0

    #Tests if each number in list is prime
    for i in primeNumbers:
        if prime % i == 0:
            temp = 1
            break

    #Adds prime number to list
    if temp == 0:
        primeNumbers.append(prime)


for n in range(1, 100000000):
    for a in primeNumbers:
        if n % a == 0:
            b = n % a
            for a in primeNumbers:
                if b % a == 0:
                    print()



#Displays answer
print(prime)