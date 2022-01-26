import math

#Variables
factorial = str(math.factorial(100))
sum = 0

#For every digit add it to list
for x in factorial:
    sum += int(x)

#Displays answers
print(sum) #Expected 648