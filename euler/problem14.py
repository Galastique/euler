#Variables
n = 0
biggest = 0 #biggest chain
number = 0 #number that produces biggest chain
answer = 0

#Loop
for n in range(1, 1000000, 2):
    temp = 0
    number = n

    #your mom
    while n>1:

        #if number is even
        if n % 2 == 0:
            n = n/2
            temp+=1

        #if number is odd
        else:
            n = 3*n+1
            temp+=1
        
        #Checks if new chain is bigger
        if temp > biggest:
            biggest = temp
            answer = number


#Shows answers
print(answer)