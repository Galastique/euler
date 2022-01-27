#Variables
longest = 0
number = 0
length = 0
answer = 0

#Finds longest chain
for n in range(1, 1000000, 2):
    length = 0
    number = n

    #Execute until chain length has been found
    while number > 1:

        #if number is even
        if number % 2 == 0:
            number = number / 2
            length += 1

        #if number is odd
        else:
            number = 3 * number + 1
            length += 1
        
        #Checks if new chain is bigger
        if length > longest:
            longest = length
            answer = n

#Shows answers
print(answer) #Expected 837799