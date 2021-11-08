#Variables
answer = 0
divisors = 0 #amount of divisors a number has
number = 0 #triangular number

#Loop
for x in range(1,100000):
    divisors = 0 #resets amount
    number+=x #gets new value of triangular number
    
    #Adds numbers to list
    for y in range(1,number+1):
        if number % y == 0:
            divisors+=1

    #Checks if answer has been found
    if divisors > 500:
        answer = number

        #Displays answers
        print(answer) #Expected 76576500
        exit()