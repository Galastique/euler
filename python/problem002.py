#Variables
fibonacciNumbers = [0,1]
answer = 0

#Finds fibanacci numbers
for i in range(0,4000000,2):

    #Finds value of next number
    x = fibonacciNumbers[-2] + fibonacciNumbers[-1]

    #Adds number to the list
    if x < 4000000:
        fibonacciNumbers.append(x)

        #Gets sum of even fibonacci number
        if x % 2 == 0:
            answer+=x

#Displays answer
print(answer) #Expected 4613732