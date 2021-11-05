#Variables
fibonacciNumbers = [0,1]
answer = 0

#Loop
for i in range(0,4000000,2):

    #Finds value of next number
    x = fibonacciNumbers[-2] + fibonacciNumbers[-1]

    #Adds number to the list
    if x < 4000000:
        fibonacciNumbers.append(x)

        #Adds even fibonacci number
        if x % 2 == 0:
            answer+=x


#Displays answer
print(answer)