#Lists
fibonacciNumbers = [1,2]
evenFibonacciNumbers = []

#Variables
x = 0

#Finds fibonacci numbers
for x in range(0,4000000,2):

    #Gets sum of last 2 numbers
    x = fibonacciNumbers[-2] + fibonacciNumbers[-1]

    #Adds sum to the list
    if x < 4000000:
        fibonacciNumbers.append(x)


#Finds even numbers from list
for y in fibonacciNumbers:
    if y % 2 == 0:
        evenFibonacciNumbers.append(y)

#Gets answer
answer = sum(evenFibonacciNumbers)

#Displays answer
print(answer)