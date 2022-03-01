import math

#Variables
factorial = str(math.factorial(100))
sum = 0

#Add every number to total
for x in factorial:
    sum += int(x)

#Displays answers
print(sum) #Expected 648