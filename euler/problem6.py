#Variables
numbers = []            #list of numbers
numbersSquared = []     #square of every number in list
x = 1                   #temp value
squareSum = 0           #square of "sum"

#Adds numbers from 1 to 100 to list
for x in range(1,101):
    numbers.append(x)

#Adds numbers from list together
sumList = sum(numbers)

#Finds square of sum
squareSum = sumList ** 2

#Adds square of every number to list
for i in numbers:
    y = i ** 2
    numbersSquared.append(y)

#Gets sum of every squared number from list
squareNumbers = sum(numbersSquared)

#Gets final answer
answer = squareSum - squareNumbers

#Displays answer
print(answer)
