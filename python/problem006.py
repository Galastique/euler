#Variables
sum = 0
squares = 0

#Adds numbers from 1 to 100 together
for i in range(1,101):
    sum+=i #Adds numbers together
    squares+=i**2 #Adds square of numbers together

#Finds square of sum
sum = sum**2

#Gets final answer
answer = sum-squares

#Displays answers
print(answer)