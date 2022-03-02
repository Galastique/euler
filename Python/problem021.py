#Variables
amicable = 0
a = 0
b = 0

#For every number under ten thousand
for number in range(1, 10000):
    a = 0
    b = 0

    #Find proper divisors of number
    for divisorA in range(1, round(number/2) + 1):
        if number % divisorA == 0:
            a += divisorA

    #Find proper divisors of a
    for divisorB in range(1, round(a/2) + 1):
        if a % divisorB == 0:
            b += divisorB

    #Checks if numbers are amicable
    if(b == number) and (not a == b):
        amicable += a

#Displays answer
print(amicable) #Expected 31626