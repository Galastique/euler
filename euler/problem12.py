#Variables
answer = 0
divisors = 0 #amount of divisors a number has
number = 0 #triangular number

#Loop
for x in range(1,10000000):
    divisors = 0 #resets amount
    number+=x #gets new value of triangular number

    #Adds numbers to list
    for y in range(1,number+1):
        if number % y == 0:
            divisors+=1

    #Checks if answer has been found
    if divisors > 500:
        answer = number
        break


#Displays answers
print(x) #2031455
print(answer) #682512600 (wrong)