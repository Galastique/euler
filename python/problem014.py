#Variables
longest = 0
number = 0
answer = 0

#Finds longest chain
for n in range(1, 1000000, 2):
    length = 0
    number = n

    #Execute until chain length has been found
    while n>1:

        #if number is even
        if n % 2 == 0:
            n = n/2
            length+=1

        #if number is odd
        else:
            n = 3*n+1
            length+=1
        
        #Checks if new chain is bigger
        if length > longest:
            longest = length
            answer = number

#Shows answers
print(answer) #Expected 837799