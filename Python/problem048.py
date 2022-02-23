#Variables
number = 0
answer = 0

#Ads x to the power of x to the total
for x in range(1, 1000):
    number += x**x

#Gets last 10 numbers of big number
answer = number % 10000000000

#Displays answer
print(answer) #Expected 9110846700