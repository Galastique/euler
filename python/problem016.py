#Variables
bigNumber = str(2**1000)
sum = 0

#Adds every digit of number to sum
for x in bigNumber:
    sum += int(x)

#Displays answer
print(sum) #Expected 1366