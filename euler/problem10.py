#Variables
primeNumbers = [2]
limit = 2000000

#Loop
for x in range(3,limit,2):
    temp = 0

    #Tests if each number in list is prime
    for i in primeNumbers:
        if x % i == 0:
            temp = 1
            break

    #Adds prime number to list
    if temp == 0:
        primeNumbers.append(x)

answer = sum(primeNumbers)

#Displays answer
print(answer)