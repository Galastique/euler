#Variables
a = 0
b = 0
c = 0
answer = 0


#Gets value of a
for a in range(1,400):

    #Gets value of b
    for b in range(a+1,400):

        #Assigns value to c
        c = 1000-a-b

        #Checks if pythagorean triplet has been found
        if ((answer == 0) and ((a < b) < c) and (a + b + c == 1000) and (a*a + b*b == c*c)):

            #Assigns answer
            answer = a*b*c


#Displays answer
print(answer)