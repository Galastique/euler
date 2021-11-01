#Variables
answer = 0
divisors = 0


#Loop
for x in range(1, 1000000):
    divisors = 0

    #Adds numbers to list
    for y in range (1, x+1):
        if x % y == 0:
            divisors+=1


    #Checks if answer has been found
    if divisors > 500:
        answer = x
        print(answer)
        break


#Displays answers
print(answer)