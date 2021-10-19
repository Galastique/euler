#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#Variables
answer = 0
done = 0
primes = 2*3*5*7*11*13*17*19 #Makes things faster by multiplying primes together

#Loop
for i in range(primes, 1000000000, primes):

    #Exits loop if answer has been found
    if done == 1:
        break
    
    #Runs code if answer hasnt been found yet
    elif done == 0:
        temp = 0
        done = 0

        #Checks if numbers are divisable by numbers from 2 to 20
        for j in range(2,21):
            if i % j == 0:
                temp+=1

                #If number can be divided by all numbers
                if temp == 19:
                    done = 1
                    answer = i


#Displays answers
print(answer)