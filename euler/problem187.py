#shit

#1. get list of primes from problem 7
#2. for loop to check if number in range 1, 10^8 can be divided by numbers from prime list
#3. if so, try it again
#4. add number to other list unless it can be divided again
#5. count amount of items in list
#100,000,000


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