import math

#Variables
permutables = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
target = 1000000
answer = ""

#For every digit
for digit in range(1, 10):
    #Finds number of possible permutations for current digits
    number = math.factorial(10 - digit)

    #Finds digit of answer
    for index in range(0, 10):
        #Checks if value of digit goes over target index
        if number * index > target:
            target -= number * (index - 1)
            answer += str(permutables[index - 1])
            permutables.pop(index - 1)
            break

#Displays answer
print(answer) #Expected 2783915460