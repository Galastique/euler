#Variables
factorials = [1]
factorial = 1
sumFactorialDigits = 0
curiousList = []

#Adds factorial of digits from 1 to 9 to list
for x in range(1, 10):
    factorial *= x
    factorials.append(factorial)

#Finds curious numbers
for curious in range(3, 50000):
    sumFactorialDigits = 0
    
    #For every digit
    for digit in str(curious):
        sumFactorialDigits += factorials[int(digit)]
    
    #Checks if number is curious
    if sumFactorialDigits == curious:
        curiousList.append(curious)

#Displays answer
print(sum(curiousList)) #Expected 40730