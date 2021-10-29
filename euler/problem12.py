#Variables
numbers = []
primeNumbers = []
answer = 0
temp = 0


#Loop
for x in range(1, 4000):
    #Clears list of numbers
    numbers.clear()
    primeNumbers.clear()

    #Adds numbers to list
    for y in range (1, x):
        numbers.append(y)

        #ugh
        for z in numbers:
            #Checks if numbers are prime
            if not(y % z == 0):
                primeNumbers.append(z)
            


    #Checks if answer has been found
    if len(primeNumbers) > 500 and temp == 0:
        answer = sum(primeNumbers)
        temp = 1


#Displays answers
#print(primeNumbers)
print(answer)