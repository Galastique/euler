#Variables
numbers = []            #list of numbers
numbersSquared = []     #square of every number in list
x = 1                   #temp value
#squareNumbers = 0       #sum of the squares of every number in list
#sum = 0                 #sum of every number in list
squareSum = 0           #square of "sum"

#Adds numbers from 1 to 100 to list
for i in range(1,101):
    numbers.append(i)


#Adds numbers from list together
sumList = sum(numbers)

#Finds square of sum
squareSum = sumList**2


#Adds square of every number to list
for i in numbers:
    y = i ** 2
    numbersSquared.append(y)

#Gets sum of every squared number from list
squareNumbers = sum(numbersSquared)

#Gets final answer
answer = squareSum - squareNumbers


#Displays answers
'''
print("\n")
print(numbers)      #list
print("\n")
print(sum)          #sum of list
print("\n")
print(squareSum)    #square of sum
print("\n")
print(numbersSquared)
print("\n")
'''
print(answer)