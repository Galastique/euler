#Variables
fibonacciNumbers = [0,1]
evenFibonacciNumbers = []


#Loop
for x in range(0,4000000,2):

    #Finds value of next number
    x = fibonacciNumbers[-2] + fibonacciNumbers[-1]

    #Adds number to the list
    if x < 4000000:
        fibonacciNumbers.append(x)


#For every number in list
for y in fibonacciNumbers:

    #Finds even numbers from list
    if y % 2 == 0:
        evenFibonacciNumbers.append(y)


#Gets answer
answer = sum(evenFibonacciNumbers)

#Displays answer
print(answer)