#Variables
numbers = []
bigNumber = 2**1000


#Converts number into a string
checkNumber = str(bigNumber)

#For every digit in string
for x in checkNumber:
    #Add digit to list
    numX = int(x)
    numbers.append(numX)


#Gets answer
answer = sum(numbers)


#Displays answer
print(answer) #Expected 1366