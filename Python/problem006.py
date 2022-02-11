#Variables
sum = 0
squares = 0

#Finds sum and sum of squares
for i in range(1,101):
    sum += i
    squares += i**2

#Finds square of sum
sum = sum**2

#Displays answers
print(sum - squares) #Expected 25164150