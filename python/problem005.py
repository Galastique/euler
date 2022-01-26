#Variables
answer = 0
primes = 2*3*5*7*11*13*17*19  #Makes things faster by multiplying primes together

#Finds smallest divisible number
for i in range(primes, 1000000000, primes):

    temp = 0

    #Checks if numbers are divisable by numbers from 2 to 20
    for j in range(2, 21):
        if i % j == 0:
            temp += 1

            #If number can be divided by all numbers
            if temp == 19:
                answer = i

                #Displays answer
                print(answer)  #Expected 232792560
                exit()